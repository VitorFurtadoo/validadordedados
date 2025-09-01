#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎓 Validador de Dados Formal - UEPA
Arquivo de execução principal

Execute este arquivo para abrir a interface visual moderna!
"""

import sys
import tkinter as tk
from tkinter import messagebox

def verificar_dependencias():
    """Verifica se todas as dependências estão disponíveis"""
    try:
        from validador_dados import ValidadorDados
        return True
    except ImportError as e:
        messagebox.showerror("Erro de Dependência", 
                           f"Erro ao importar módulos necessários:\n{e}")
        return False

def main():
    """Função principal de execução"""
    try:
        print("🎓 Validador de Dados Formal - UEPA")
        print("=" * 50)
        print("Iniciando interface visual...")
        
        # Verificar dependências
        if not verificar_dependencias():
            print("❌ Erro: Dependências não encontradas!")
            input("Pressione Enter para sair...")
            return
        
        try:
            # Tentar interface visual completa primeiro
            from interface_visual import ValidadorGUI
            
            print("✅ Módulos carregados com sucesso!")
            print("🚀 Abrindo interface visual completa...")
            print("\n💡 Dica: Use Ctrl+Enter para validar todos os campos rapidamente!")
            
            app = ValidadorGUI()
            app.run()
            
        except Exception as e:
            print(f"⚠️  Interface visual completa não disponível: {e}")
            print("Tentando interface visual simples...")
            
            try:
                from interface_simples import ValidadorSimples
                print("🚀 Abrindo interface visual simples...")
                app = ValidadorSimples()
                app.run()
                
            except Exception as e2:
                print(f"⚠️  Interface visual simples não disponível: {e2}")
                print("Tentando abrir interface de linha de comando...")
            
            try:
                from interface_validador import InterfaceValidador
                interface = InterfaceValidador()
                interface.executar()
            except ImportError as e2:
                print(f"❌ Interface de linha de comando não disponível: {e2}")
                print("Executando teste básico...")
                
                try:
                    from validador_dados import ValidadorDados
                    validador = ValidadorDados()
                    
                    print("\n=== TESTE RÁPIDO ===")
                    print("Testando: 'Alan Turing'")
                    valido, msg = validador.validar_nome("Alan Turing")
                    print(f"Resultado: {'✅' if valido else '❌'} {msg}")
                    
                except Exception as e3:
                    print(f"❌ Erro ao executar teste básico: {e3}")
                    
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            print(f"Tipo do erro: {type(e).__name__}")
            import traceback
            traceback.print_exc()
            
    except Exception as e:
        print(f"❌ Erro crítico: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        print("\n👋 Obrigado por usar o Validador de Dados Formal!")
        input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()