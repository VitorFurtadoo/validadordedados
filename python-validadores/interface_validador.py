#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from validador_dados import ValidadorDados
import os

class InterfaceValidador:
    def __init__(self):
        self.validador = ValidadorDados()
        self.campos = {
            '1': ('nome', 'Nome'),
            '2': ('email', 'E-mail'),
            '3': ('senha', 'Senha'),
            '4': ('cpf', 'CPF'),
            '5': ('rg', 'RG'),
            '6': ('telefone', 'Telefone'),
            '7': ('cep', 'CEP'),
            '8': ('data_horario', 'Data e Horário'),
            '9': ('numero_flutuante', 'Número de Ponto Flutuante')
        }
    
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_menu(self):
        print("\n" + "="*60)
        print("           VALIDADOR DE DADOS FORMAL")
        print("="*60)
        print("\nEscolha o tipo de validação:")
        print("-" * 40)
        
        for num, (_, nome) in self.campos.items():
            print(f"{num}. {nome}")
        
        print("10. Validar todos os campos")
        print("11. Mostrar exemplos válidos")
        print("0. Sair")
        print("-" * 40)
    
    def mostrar_exemplos(self):
        exemplos = {
            'Nome': '"Alan Turing", "Noam Chomsky"',
            'E-mail': '"a@a.br", "bes@uepa.br"',
            'Senha': '"518R2r5e", "F1234567A", "1234567T"',
            'CPF': '"123.456.789-09"',
            'RG': '"875467-2"',
            'Telefone': '"(91) 99999-9999"',
            'CEP': '"66.645-225"',
            'Data e Horário': '"02/09/2025 23:59:59"',
            'Número de Ponto Flutuante': '"-25.467", "1", "+64,2"'
        }
        
        print("\n" + "="*60)
        print("                EXEMPLOS VÁLIDOS")
        print("="*60)
        
        for campo, exemplo in exemplos.items():
            print(f"\n{campo}:")
            print(f"  {exemplo}")
        
        input("\nPressione Enter para continuar...")
    
    def validar_campo_individual(self, tipo_campo: str, nome_campo: str):
        print(f"\n=== VALIDAÇÃO DE {nome_campo.upper()} ===")
        
        while True:
            valor = input(f"\nDigite o {nome_campo} (ou 'voltar' para menu): ")
            
            if valor.lower() == 'voltar':
                break
            
            metodo = getattr(self.validador, f'validar_{tipo_campo}')
            valido, mensagem = metodo(valor)
            
            status = "✓ VÁLIDO" if valido else "✗ INVÁLIDO"
            cor = '\033[92m' if valido else '\033[91m'
            reset = '\033[0m'
            
            print(f"\nResultado: {cor}{status}{reset}")
            print(f"Mensagem: {mensagem}")
            
            continuar = input("\nDeseja testar outro valor? (s/n): ")
            if continuar.lower() != 's':
                break
    
    def validar_todos_campos_interativo(self):
        print("\n=== VALIDAÇÃO DE TODOS OS CAMPOS ===")
        
        dados = {}
        for _, (tipo, nome) in self.campos.items():
            valor = input(f"\n{nome}: ")
            if valor:
                dados[tipo] = valor
        
        if not dados:
            print("\nNenhum campo foi preenchido!")
            input("Pressione Enter para continuar...")
            return
        
        resultados = self.validador.validar_todos_campos(dados)
        
        print("\n" + "="*60)
        print("                 RESULTADOS")
        print("="*60)
        
        todos_validos = True
        for campo, (valido, mensagem) in resultados.items():
            status = "✓" if valido else "✗"
            cor = '\033[92m' if valido else '\033[91m'
            reset = '\033[0m'
            
            nome_campo = next(nome for _, (tipo, nome) in self.campos.items() if tipo == campo)
            
            print(f"\n{cor}{status} {nome_campo}{reset}")
            print(f"  Valor: {dados[campo]}")
            print(f"  Status: {mensagem}")
            
            if not valido:
                todos_validos = False
        
        print("\n" + "="*60)
        if todos_validos:
            print("🎉 TODOS OS CAMPOS SÃO VÁLIDOS!")
        else:
            print("❌ ALGUNS CAMPOS POSSUEM ERROS")
        
        input("\nPressione Enter para continuar...")
    
    def executar(self):
        while True:
            self.limpar_tela()
            self.mostrar_menu()
            
            try:
                opcao = input("\nEscolha uma opção: ")
                
                if opcao == '0':
                    print("\nObrigado por usar o Validador de Dados Formal!")
                    break
                elif opcao == '10':
                    self.validar_todos_campos_interativo()
                elif opcao == '11':
                    self.mostrar_exemplos()
                elif opcao in self.campos:
                    tipo_campo, nome_campo = self.campos[opcao]
                    self.validar_campo_individual(tipo_campo, nome_campo)
                else:
                    print("\nOpção inválida! Tente novamente.")
                    input("Pressione Enter para continuar...")
            
            except KeyboardInterrupt:
                print("\n\nSaindo...")
                break
            except Exception as e:
                print(f"\nErro: {e}")
                input("Pressione Enter para continuar...")

if __name__ == "__main__":
    interface = InterfaceValidador()
    interface.executar()