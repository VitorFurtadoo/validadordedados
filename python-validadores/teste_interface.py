#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

def teste_simples():
    try:
        print("🔍 Testando importações...")
        
        # Testar tkinter
        root = tk.Tk()
        root.withdraw()  # Esconder janela temporariamente
        print("✅ Tkinter OK")
        
        # Testar validador
        sys.path.append(os.path.dirname(__file__))
        from validador_dados import ValidadorDados
        validador = ValidadorDados()
        print("✅ ValidadorDados OK")
        
        # Criar janela simples de teste
        root.deiconify()  # Mostrar janela
        root.title("🧪 Teste - Validador de Dados")
        root.geometry("600x400")
        
        # Centralizar
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (300)
        y = (root.winfo_screenheight() // 2) - (200)
        root.geometry(f'600x400+{x}+{y}')
        
        # Interface simples
        frame = ttk.Frame(root, padding=20)
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="🎓 Validador de Dados Formal", 
                 font=('Arial', 16, 'bold')).pack(pady=20)
        
        ttk.Label(frame, text="Teste de Nome:", font=('Arial', 12)).pack(pady=5)
        
        entry = ttk.Entry(frame, font=('Arial', 12))
        entry.pack(pady=5, fill='x')
        entry.insert(0, "Alan Turing")
        
        result_label = ttk.Label(frame, text="", font=('Arial', 10))
        result_label.pack(pady=10)
        
        def validar():
            try:
                nome = entry.get()
                valido, mensagem = validador.validar_nome(nome)
                
                if valido:
                    result_label.config(text=f"✅ {mensagem}", foreground='green')
                else:
                    result_label.config(text=f"❌ {mensagem}", foreground='red')
            except Exception as e:
                result_label.config(text=f"Erro: {e}", foreground='red')
        
        ttk.Button(frame, text="🔍 Validar Nome", 
                  command=validar).pack(pady=10)
        
        def abrir_interface_completa():
            try:
                root.destroy()
                from interface_visual import ValidadorGUI
                app = ValidadorGUI()
                app.run()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao abrir interface completa:\n{e}")
                
        ttk.Button(frame, text="🚀 Abrir Interface Completa", 
                  command=abrir_interface_completa).pack(pady=20)
        
        ttk.Label(frame, text="🧪 Teste básico funcionando!", 
                 foreground='blue').pack(pady=10)
        
        print("✅ Interface de teste criada!")
        print("🎯 Janela deve estar aberta agora...")
        
        # Testar validação
        validar()
        
        root.mainloop()
        
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        import traceback
        traceback.print_exc()
        input("Pressione Enter para sair...")

if __name__ == "__main__":
    teste_simples()