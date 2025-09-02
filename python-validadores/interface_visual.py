#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from validador_dados import ValidadorDados
import threading
import time

class ValidadorGUI:
    def __init__(self):
        self.validador = ValidadorDados()
        
        # Inicializar dicionários ANTES de criar widgets
        self.entries = {}
        self.result_labels = {}
        
        self.root = tk.Tk()
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        self.setup_bindings()
        
    def setup_window(self):
        self.root.title("Validador de Dados Formal - UEPA")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # Centralizar janela
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Ícone e configurações
        try:
            self.root.iconbitmap(default='icon.ico')
        except:
            pass
            
    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Cores personalizadas
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), foreground='#2c3e50')
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), foreground='#34495e')
        style.configure('Valid.TLabel', font=('Arial', 9), foreground='#27ae60')
        style.configure('Invalid.TLabel', font=('Arial', 9), foreground='#e74c3c')
        style.configure('Info.TLabel', font=('Arial', 8), foreground='#7f8c8d')
        
        # Botões personalizados
        style.configure('Action.TButton', font=('Arial', 10, 'bold'))
        style.configure('Help.TButton', font=('Arial', 8))
        
    def create_widgets(self):
        # Frame principal com scroll
        main_canvas = tk.Canvas(self.root, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        self.scrollable_frame = ttk.Frame(main_canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )
        
        main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Header
        self.create_header()
        
        # Campos de validação
        self.create_validation_fields()
        
        # Botões de ação
        self.create_action_buttons()
        
        # Área de resultados
        self.create_results_area()
        
        # Pack canvas e scrollbar
        main_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel
        def _on_mousewheel(event):
            main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        main_canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
    def create_header(self):
        header_frame = ttk.Frame(self.scrollable_frame)
        header_frame.pack(fill='x', padx=20, pady=20)
        
        ttk.Label(header_frame, text="🎓 Validador de Dados Formal", 
                 style='Title.TLabel').pack()
        ttk.Label(header_frame, text="Universidade do Estado do Pará - Linguagens Formais", 
                 style='Info.TLabel').pack(pady=(5, 15))
        
        ttk.Separator(header_frame, orient='horizontal').pack(fill='x', pady=10)
        
    def create_validation_fields(self):
        fields_frame = ttk.Frame(self.scrollable_frame)
        fields_frame.pack(fill='both', expand=True, padx=20)
        
        # Configurar grid
        fields_frame.columnconfigure(1, weight=1)
        
        # Definir campos com exemplos e dicas
        self.field_configs = {
            'nome': {
                'label': 'Nome Completo',
                'placeholder': 'Ex: Alan Turing',
                'help': 'Nome e sobrenome, primeira letra maiúscula'
            },
            'email': {
                'label': 'E-mail',
                'placeholder': 'Ex: usuario@dominio.br',
                'help': 'Formato: usuario@dominio.br (apenas .br)'
            },
            'senha': {
                'label': 'Senha',
                'placeholder': 'Ex: F1234567',
                'help': '8 caracteres, 1 maiúscula, 1 número, sem símbolos',
                'show': '*'
            },
            'cpf': {
                'label': 'CPF',
                'placeholder': 'Ex: 123.456.789-09',
                'help': 'Formato: 123.456.789-09'
            },
            'rg': {
                'label': 'RG',
                'placeholder': 'Ex: 1234567-8',
                'help': 'Formato: 1234567-8'
            },
            'telefone': {
                'label': 'Telefone',
                'placeholder': 'Ex: (91) 99999-9999',
                'help': 'Formato: (DD) 99999-9999'
            },
            'cep': {
                'label': 'CEP',
                'placeholder': 'Ex: 66.645-225',
                'help': 'Formato: 12.345-678'
            },
            'data_horario': {
                'label': 'Data e Horário',
                'placeholder': 'Ex: 02/09/2025 23:59:59',
                'help': 'Formato: dd/mm/aaaa hh:mm:ss'
            },
            'numero_flutuante': {
                'label': 'Número Decimal',
                'placeholder': 'Ex: -25.467 ou +64,2',
                'help': 'Números com sinal opcional, . ou , como separador'
            }
        }
        
        row = 0
        for field_key, config in self.field_configs.items():
            # Frame para cada campo
            field_frame = ttk.LabelFrame(fields_frame, text=f"📋 {config['label']}", 
                                       padding=10)
            field_frame.grid(row=row//2, column=row%2, padx=10, pady=5, 
                           sticky='ew', columnspan=1 if row%2==1 else 1)
            field_frame.columnconfigure(0, weight=1)
            
            # Entry com validação em tempo real
            entry_var = tk.StringVar()
            entry_var.trace('w', lambda *args, key=field_key: self.validate_field_realtime(key))
            
            entry = ttk.Entry(field_frame, textvariable=entry_var, 
                            font=('Consolas', 10),
                            show=config.get('show', ''))
            entry.pack(fill='x', pady=(0, 5))
            
            # Placeholder
            self.set_placeholder(entry, config['placeholder'])
            
            # Label de resultado
            result_label = ttk.Label(field_frame, text="⌨️ Digite para validar...", 
                                   style='Info.TLabel')
            result_label.pack(anchor='w')
            
            # Dica
            help_label = ttk.Label(field_frame, text=f"💡 {config['help']}", 
                                 style='Info.TLabel')
            help_label.pack(anchor='w', pady=(2, 0))
            
            # Armazenar referências
            self.entries[field_key] = entry
            self.result_labels[field_key] = result_label
            
            row += 1
            
    def set_placeholder(self, entry, placeholder):
        entry.insert(0, placeholder)
        entry.config(foreground='gray')
        
        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(foreground='black')
                
        def on_focus_out(event):
            if not entry.get():
                entry.insert(0, placeholder)
                entry.config(foreground='gray')
                
        entry.bind('<FocusIn>', on_focus_in)
        entry.bind('<FocusOut>', on_focus_out)
        
    def create_action_buttons(self):
        button_frame = ttk.Frame(self.scrollable_frame)
        button_frame.pack(fill='x', padx=20, pady=20)
        
        # Frame para botões centralizados
        center_frame = ttk.Frame(button_frame)
        center_frame.pack()
        
        ttk.Button(center_frame, text="🔍 Validar Todos", 
                  command=self.validate_all, style='Action.TButton').pack(side='left', padx=5)
        
        ttk.Button(center_frame, text="🗑️ Limpar Campos", 
                  command=self.clear_all, style='Action.TButton').pack(side='left', padx=5)
        
        ttk.Button(center_frame, text="📋 Exemplos Válidos", 
                  command=self.show_examples, style='Action.TButton').pack(side='left', padx=5)
        
        ttk.Button(center_frame, text="📊 Relatório", 
                  command=self.generate_report, style='Action.TButton').pack(side='left', padx=5)
        
    def create_results_area(self):
        results_frame = ttk.LabelFrame(self.scrollable_frame, text="📈 Área de Resultados", 
                                     padding=10)
        results_frame.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        
        self.results_text = scrolledtext.ScrolledText(results_frame, height=8, 
                                                     font=('Consolas', 10),
                                                     wrap=tk.WORD)
        self.results_text.pack(fill='both', expand=True)
        
        # Configurar tags para cores
        self.results_text.tag_configure('valid', foreground='#27ae60', font=('Consolas', 10, 'bold'))
        self.results_text.tag_configure('invalid', foreground='#e74c3c', font=('Consolas', 10, 'bold'))
        self.results_text.tag_configure('info', foreground='#3498db', font=('Consolas', 10, 'bold'))
        self.results_text.tag_configure('header', foreground='#8e44ad', font=('Consolas', 12, 'bold'))
        
        # Mensagem inicial
        self.results_text.insert(tk.END, "🎯 Bem-vindo ao Validador de Dados Formal!\n\n", 'header')
        self.results_text.insert(tk.END, "💡 Dicas:\n", 'info')
        self.results_text.insert(tk.END, "• Digite nos campos acima para validação em tempo real\n")
        self.results_text.insert(tk.END, "• Use 'Validar Todos' para um relatório completo\n")
        self.results_text.insert(tk.END, "• Clique em 'Exemplos Válidos' para ver formatos aceitos\n\n")
        
    def validate_field_realtime(self, field_key):
        try:
            if field_key not in self.entries or field_key not in self.result_labels:
                return
                
            entry = self.entries[field_key]
            result_label = self.result_labels[field_key]
            
            value = entry.get()
            
            if not hasattr(self, 'field_configs') or field_key not in self.field_configs:
                return
                
            placeholder = self.field_configs[field_key]['placeholder']
            
            # Ignorar placeholder
            if value == placeholder or not value.strip():
                result_label.config(text="⌨️ Digite para validar...", style='Info.TLabel')
                return
                
            # Validar após pequeno delay para evitar validação excessiva
            self.root.after(300, lambda: self._delayed_validation(field_key, value))
        except Exception as e:
            print(f"Erro na validação em tempo real: {e}")
            pass
        
    def _delayed_validation(self, field_key, value):
        try:
            if field_key not in self.entries or field_key not in self.result_labels:
                return
                
            current_value = self.entries[field_key].get()
            if current_value != value:  # Valor mudou, ignorar validação antiga
                return
                
            if not hasattr(self.validador, f'validar_{field_key}'):
                return
                
            metodo = getattr(self.validador, f'validar_{field_key}')
            valido, mensagem = metodo(value)
            
            result_label = self.result_labels[field_key]
            
            if valido:
                result_label.config(text=f"✅ {mensagem}", style='Valid.TLabel')
            else:
                result_label.config(text=f"❌ {mensagem}", style='Invalid.TLabel')
        except Exception as e:
            print(f"Erro na validação atrasada: {e}")
            pass
            
    def get_field_values(self):
        valores = {}
        for field_key, entry in self.entries.items():
            value = entry.get().strip()
            placeholder = self.field_configs[field_key]['placeholder']
            
            if value and value != placeholder:
                valores[field_key] = value
                
        return valores
        
    def validate_all(self):
        valores = self.get_field_values()
        
        if not valores:
            messagebox.showwarning("Atenção", "Preencha pelo menos um campo para validar!")
            return
            
        # Limpar área de resultados
        self.results_text.delete(1.0, tk.END)
        
        # Header do relatório
        self.results_text.insert(tk.END, "🔍 RELATÓRIO DE VALIDAÇÃO COMPLETA\n", 'header')
        self.results_text.insert(tk.END, "=" * 60 + "\n\n", 'info')
        
        # Validar cada campo
        resultados = self.validador.validar_todos_campos(valores)
        
        campos_validos = 0
        total_campos = len(resultados)
        
        for field_key, (valido, mensagem) in resultados.items():
            campo_nome = self.field_configs[field_key]['label']
            valor = valores[field_key]
            
            if valido:
                self.results_text.insert(tk.END, f"✅ {campo_nome}\n", 'valid')
                campos_validos += 1
            else:
                self.results_text.insert(tk.END, f"❌ {campo_nome}\n", 'invalid')
                
            self.results_text.insert(tk.END, f"   Valor: {valor}\n")
            self.results_text.insert(tk.END, f"   Status: {mensagem}\n\n")
            
        # Resumo final
        self.results_text.insert(tk.END, "=" * 60 + "\n", 'info')
        self.results_text.insert(tk.END, f"📊 RESUMO: {campos_validos}/{total_campos} campos válidos\n", 'info')
        
        percentual = (campos_validos / total_campos) * 100
        if percentual == 100:
            self.results_text.insert(tk.END, "🎉 TODOS OS CAMPOS SÃO VÁLIDOS!\n", 'valid')
        else:
            self.results_text.insert(tk.END, f"⚠️ {total_campos - campos_validos} campos com erro\n", 'invalid')
            
    def clear_all(self):
        for field_key, entry in self.entries.items():
            entry.delete(0, tk.END)
            placeholder = self.field_configs[field_key]['placeholder']
            self.set_placeholder(entry, placeholder)
            
            self.result_labels[field_key].config(text="⌨️ Digite para validar...", 
                                               style='Info.TLabel')
            
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "🧹 Todos os campos foram limpos!\n\n", 'info')
        
    def show_examples(self):
        examples_window = tk.Toplevel(self.root)
        examples_window.title("📋 Exemplos de Entradas Válidas")
        examples_window.geometry("600x500")
        examples_window.resizable(False, False)
        
        # Centralizar janela
        examples_window.transient(self.root)
        examples_window.grab_set()
        
        frame = ttk.Frame(examples_window, padding=20)
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="📋 Exemplos de Entradas Válidas", 
                 style='Title.TLabel').pack(pady=(0, 20))
        
        # Texto com exemplos
        examples_text = scrolledtext.ScrolledText(frame, font=('Consolas', 10), 
                                                wrap=tk.WORD)
        examples_text.pack(fill='both', expand=True)
        
        examples_content = """🎯 EXEMPLOS VÁLIDOS POR CAMPO:

📝 Nome Completo:
   • Alan Turing
   • Noam Chomsky
   • Ada Lovelace

📧 E-mail:
   • a@a.br
   • bes@uepa.br
   • usuario@dominio.br

🔐 Senha:
   • 518R2r5e
   • F1234567
   • 1234567T
   • ropsSoq0

🆔 CPF:
   • 123.456.789-09
   • 000.111.222-33

📋 RG:
   • 875467-2
   • 123456-7

📞 Telefone:
   • (91) 99999-9999
   • (11) 98765-4321

📍 CEP:
   • 66.645-225
   • 01234-567

📅 Data e Horário:
   • 02/09/2025 23:59:59
   • 01/01/2024 00:00:00

🔢 Número Decimal:
   • -25.467
   • +64,2
   • 123.456
   • 1
   • -1"""
        
        examples_text.insert(tk.END, examples_content)
        examples_text.config(state='disabled')
        
        ttk.Button(frame, text="Fechar", 
                  command=examples_window.destroy).pack(pady=10)
                  
    def generate_report(self):
        valores = self.get_field_values()
        
        if not valores:
            messagebox.showwarning("Atenção", "Preencha pelo menos um campo para gerar relatório!")
            return
            
        report_window = tk.Toplevel(self.root)
        report_window.title("📊 Relatório Detalhado")
        report_window.geometry("700x600")
        
        frame = ttk.Frame(report_window, padding=20)
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="📊 Relatório Detalhado de Validação", 
                 style='Title.TLabel').pack(pady=(0, 20))
        
        report_text = scrolledtext.ScrolledText(frame, font=('Consolas', 9), 
                                              wrap=tk.WORD)
        report_text.pack(fill='both', expand=True)
        
        # Configurar tags
        report_text.tag_configure('valid', foreground='#27ae60')
        report_text.tag_configure('invalid', foreground='#e74c3c')
        report_text.tag_configure('header', foreground='#8e44ad', font=('Consolas', 11, 'bold'))
        
        # Gerar relatório
        resultados = self.validador.validar_todos_campos(valores)
        
        report_text.insert(tk.END, "📊 RELATÓRIO DETALHADO DE VALIDAÇÃO\n", 'header')
        report_text.insert(tk.END, f"📅 Gerado em: {time.strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        
        for field_key, (valido, mensagem) in resultados.items():
            campo_nome = self.field_configs[field_key]['label']
            valor = valores[field_key]
            regex_usado = str(self.validador.patterns[field_key].pattern)
            
            status_text = "VÁLIDO" if valido else "INVÁLIDO"
            tag = 'valid' if valido else 'invalid'
            
            report_text.insert(tk.END, f"{'='*60}\n")
            report_text.insert(tk.END, f"Campo: {campo_nome}\n")
            report_text.insert(tk.END, f"Valor Testado: '{valor}'\n")
            report_text.insert(tk.END, f"Status: ", '')
            report_text.insert(tk.END, f"{status_text}\n", tag)
            report_text.insert(tk.END, f"Mensagem: {mensagem}\n")
            report_text.insert(tk.END, f"Regex Usado: {regex_usado}\n\n")
            
        ttk.Button(frame, text="Fechar Relatório", 
                  command=report_window.destroy).pack(pady=10)
        
    def setup_bindings(self):
        # Atalhos de teclado
        self.root.bind('<Control-Return>', lambda e: self.validate_all())
        self.root.bind('<Control-l>', lambda e: self.clear_all())
        self.root.bind('<F1>', lambda e: self.show_examples())
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ValidadorGUI()
    app.run()