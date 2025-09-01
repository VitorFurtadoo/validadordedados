#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from validador_dados import ValidadorDados

class ValidadorSimples:
    def __init__(self):
        self.validador = ValidadorDados()
        self.root = tk.Tk()
        self.entries = {}
        self.labels = {}
        self.setup_gui()
        
    def setup_gui(self):
        self.root.title("🎓 Validador de Dados - UEPA")
        self.root.geometry("800x600")
        
        # Centralizar janela
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400)
        y = (self.root.winfo_screenheight() // 2) - (300)
        self.root.geometry(f'800x600+{x}+{y}')
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill='both', expand=True)
        
        # Título
        title = ttk.Label(main_frame, text="🎓 Validador de Dados Formal", 
                         font=('Arial', 16, 'bold'))
        title.pack(pady=(0, 20))
        
        # Frame para campos
        fields_frame = ttk.Frame(main_frame)
        fields_frame.pack(fill='x', pady=(0, 20))
        
        # Criar campos
        self.create_fields(fields_frame)
        
        # Botões
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill='x', pady=(0, 20))
        
        ttk.Button(buttons_frame, text="🔍 Validar Todos", 
                  command=self.validar_todos).pack(side='left', padx=5)
        ttk.Button(buttons_frame, text="🗑️ Limpar", 
                  command=self.limpar_campos).pack(side='left', padx=5)
        ttk.Button(buttons_frame, text="📋 Exemplos", 
                  command=self.mostrar_exemplos).pack(side='left', padx=5)
        
        # Área de resultados
        results_label = ttk.Label(main_frame, text="📊 Resultados:", 
                                 font=('Arial', 12, 'bold'))
        results_label.pack(anchor='w', pady=(10, 5))
        
        self.results_text = scrolledtext.ScrolledText(main_frame, height=10, 
                                                     font=('Consolas', 10))
        self.results_text.pack(fill='both', expand=True)
        
        # Mensagem inicial
        self.results_text.insert(tk.END, "🎯 Validador de Dados Formal - UEPA\n")
        self.results_text.insert(tk.END, "Preencha os campos acima e clique em 'Validar Todos'\n\n")
        
    def create_fields(self, parent):
        fields = [
            ('nome', 'Nome Completo', 'Ex: Alan Turing'),
            ('email', 'E-mail', 'Ex: usuario@dominio.br'),
            ('senha', 'Senha', 'Ex: F1234567'),
            ('cpf', 'CPF', 'Ex: 123.456.789-09'),
            ('rg', 'RG', 'Ex: 1234567-8'),
            ('telefone', 'Telefone', 'Ex: (91) 99999-9999'),
            ('cep', 'CEP', 'Ex: 66.645-225'),
            ('data_horario', 'Data/Horário', 'Ex: 02/09/2025 23:59:59'),
            ('numero_flutuante', 'Número', 'Ex: -25.467')
        ]
        
        # Organizar em 3 colunas
        for i, (key, label, placeholder) in enumerate(fields):
            row = i // 3
            col = i % 3
            
            # Frame para cada campo
            field_frame = ttk.Frame(parent)
            field_frame.grid(row=row*2, column=col, padx=10, pady=5, sticky='ew')
            
            # Label
            ttk.Label(field_frame, text=label, font=('Arial', 9, 'bold')).pack(anchor='w')
            
            # Entry
            entry = ttk.Entry(field_frame, font=('Arial', 9), width=25)
            entry.pack(fill='x', pady=2)
            entry.insert(0, placeholder)
            entry.bind('<FocusIn>', lambda e, p=placeholder: self.clear_placeholder(e, p))
            entry.bind('<FocusOut>', lambda e, p=placeholder: self.restore_placeholder(e, p))
            entry.config(foreground='gray')
            
            # Label de status
            status_label = ttk.Label(field_frame, text="", font=('Arial', 8))
            status_label.pack(anchor='w')
            
            self.entries[key] = entry
            self.labels[key] = status_label
            
        # Configurar grid
        parent.columnconfigure(0, weight=1)
        parent.columnconfigure(1, weight=1)
        parent.columnconfigure(2, weight=1)
        
    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, tk.END)
            event.widget.config(foreground='black')
            
    def restore_placeholder(self, event, placeholder):
        if not event.widget.get():
            event.widget.insert(0, placeholder)
            event.widget.config(foreground='gray')
            
    def get_values(self):
        placeholders = {
            'nome': 'Ex: Alan Turing',
            'email': 'Ex: usuario@dominio.br',
            'senha': 'Ex: F1234567',
            'cpf': 'Ex: 123.456.789-09',
            'rg': 'Ex: 1234567-8',
            'telefone': 'Ex: (91) 99999-9999',
            'cep': 'Ex: 66.645-225',
            'data_horario': 'Ex: 02/09/2025 23:59:59',
            'numero_flutuante': 'Ex: -25.467'
        }
        
        values = {}
        for key, entry in self.entries.items():
            value = entry.get().strip()
            if value and value != placeholders.get(key, ''):
                values[key] = value
        return values
        
    def validar_todos(self):
        values = self.get_values()
        
        if not values:
            messagebox.showwarning("Atenção", "Preencha pelo menos um campo!")
            return
            
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "🔍 RELATÓRIO DE VALIDAÇÃO\n")
        self.results_text.insert(tk.END, "="*50 + "\n\n")
        
        resultados = self.validador.validar_todos_campos(values)
        
        validos = 0
        total = len(resultados)
        
        field_names = {
            'nome': 'Nome Completo',
            'email': 'E-mail',
            'senha': 'Senha',
            'cpf': 'CPF',
            'rg': 'RG',
            'telefone': 'Telefone',
            'cep': 'CEP',
            'data_horario': 'Data/Horário',
            'numero_flutuante': 'Número'
        }
        
        for field, (valido, mensagem) in resultados.items():
            nome = field_names.get(field, field)
            valor = values[field]
            
            # Atualizar label individual
            if valido:
                self.labels[field].config(text="✅ Válido", foreground='green')
                self.results_text.insert(tk.END, f"✅ {nome}: {valor}\n   Status: {mensagem}\n\n")
                validos += 1
            else:
                self.labels[field].config(text="❌ Erro", foreground='red')
                self.results_text.insert(tk.END, f"❌ {nome}: {valor}\n   Erro: {mensagem}\n\n")
                
        # Resumo
        self.results_text.insert(tk.END, "="*50 + "\n")
        self.results_text.insert(tk.END, f"📊 Resultado: {validos}/{total} campos válidos\n")
        
        if validos == total:
            self.results_text.insert(tk.END, "🎉 TODOS OS CAMPOS SÃO VÁLIDOS!\n")
        else:
            self.results_text.insert(tk.END, f"⚠️ {total-validos} campos com erro\n")
            
    def limpar_campos(self):
        placeholders = {
            'nome': 'Ex: Alan Turing',
            'email': 'Ex: usuario@dominio.br',
            'senha': 'Ex: F1234567',
            'cpf': 'Ex: 123.456.789-09',
            'rg': 'Ex: 1234567-8',
            'telefone': 'Ex: (91) 99999-9999',
            'cep': 'Ex: 66.645-225',
            'data_horario': 'Ex: 02/09/2025 23:59:59',
            'numero_flutuante': 'Ex: -25.467'
        }
        
        for key, entry in self.entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, placeholders[key])
            entry.config(foreground='gray')
            self.labels[key].config(text="")
            
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "🧹 Campos limpos! Digite novos valores para validar.\n")
        
    def mostrar_exemplos(self):
        exemplos = """📋 EXEMPLOS DE ENTRADAS VÁLIDAS:

📝 Nome: Alan Turing, Noam Chomsky
📧 E-mail: usuario@dominio.br, test@uepa.br
🔐 Senha: F1234567, 518R2r5e (8 chars, 1 maiúscula, 1 número)
🆔 CPF: 123.456.789-09
📋 RG: 1234567-8
📞 Telefone: (91) 99999-9999
📍 CEP: 66.645-225
📅 Data/Horário: 02/09/2025 23:59:59
🔢 Número: -25.467, +64,2, 123.456, 1"""

        messagebox.showinfo("Exemplos Válidos", exemplos)
        
    def run(self):
        print("✅ Interface simples iniciada!")
        self.root.mainloop()

if __name__ == "__main__":
    try:
        app = ValidadorSimples()
        app.run()
    except Exception as e:
        print(f"Erro: {e}")
        input("Pressione Enter para sair...")