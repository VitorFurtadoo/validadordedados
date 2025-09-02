#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from validador_dados import ValidadorDados

def testar_validadores():
    validador = ValidadorDados()
    
    print("="*70)
    print("            TESTE COMPLETO DOS VALIDADORES")
    print("="*70)
    
    # Casos de teste válidos
    casos_validos = {
        'nome': ["Alan Turing", "Noam Chomsky", "Ada Lovelace"],
        'email': ["a@a.br", "bes@uepa.br", "test@domain.br"],
        'senha': ["518R2r5e", "F1234567", "1234567T", "ropsSoq0"],
        'cpf': ["123.456.789-09", "000.111.222-33"],
        'rg': ["875467-2", "123456-7"],
        'telefone': ["(91) 99999-9999", "(11) 98765-4321"],
        'cep': ["66.645-225", "01234-567"],
        'data_horario': ["02/09/2025 23:59:59", "01/01/2024 00:00:00"],
        'numero_flutuante': ["-25.467", "1", "-1", "+1", "+64,2", "64,2", "123.456"]
    }
    
    # Casos de teste inválidos
    casos_invalidos = {
        'nome': ["alan turing", "ALAN TURING", "Alan", "Alan123", "Alan@Turing"],
        'email': ["@domain.br", "user@.br", "user@domain", "user@domain.com"],
        'senha': ["12345678", "abcdefgh", "ABCDEFGH", "123abc", "12345Ab@"],
        'cpf': ["12345678909", "123.456.789.09", "123-456-789-09"],
        'rg': ["1234567", "123456-", "12345-67"],
        'telefone': ["91999999999", "(91)99999-9999", "(91) 9999-99999"],
        'cep': ["66645225", "66.645.225", "66-645-225"],
        'data_horario': ["2/9/2025 23:59:59", "02/09/25 23:59:59", "02-09-2025 23:59:59"],
        'numero_flutuante': ["", "abc", "1.2.3", "++1", "--1"]
    }
    
    total_testes = 0
    total_sucessos = 0
    
    # Testar casos válidos
    print("\n📋 TESTANDO CASOS VÁLIDOS:")
    print("-" * 70)
    
    for campo, casos in casos_validos.items():
        metodo = getattr(validador, f'validar_{campo}')
        print(f"\n{campo.upper()}:")
        
        for caso in casos:
            total_testes += 1
            valido, mensagem = metodo(caso)
            status = "✅" if valido else "❌"
            
            if valido:
                total_sucessos += 1
                print(f"  {status} '{caso}' -> {mensagem}")
            else:
                print(f"  {status} '{caso}' -> {mensagem} (DEVERIA SER VÁLIDO!)")
    
    # Testar casos inválidos
    print("\n\n📋 TESTANDO CASOS INVÁLIDOS:")
    print("-" * 70)
    
    for campo, casos in casos_invalidos.items():
        metodo = getattr(validador, f'validar_{campo}')
        print(f"\n{campo.upper()}:")
        
        for caso in casos:
            total_testes += 1
            valido, mensagem = metodo(caso)
            status = "✅" if not valido else "❌"
            
            if not valido:
                total_sucessos += 1
                print(f"  {status} '{caso}' -> {mensagem}")
            else:
                print(f"  {status} '{caso}' -> {mensagem} (DEVERIA SER INVÁLIDO!)")
    
    # Testar casos especiais (espaços, vazio)
    print("\n\n📋 TESTANDO CASOS ESPECIAIS:")
    print("-" * 70)
    
    casos_especiais = ["", " ", "  ", " teste", "teste ", " teste "]
    
    for campo in casos_validos.keys():
        metodo = getattr(validador, f'validar_{campo}')
        print(f"\n{campo.upper()}:")
        
        for caso in casos_especiais:
            total_testes += 1
            valido, mensagem = metodo(caso)
            
            if not valido:
                total_sucessos += 1
                print(f"  ✅ '{caso}' -> {mensagem}")
            else:
                print(f"  ❌ '{caso}' -> {mensagem} (DEVERIA SER INVÁLIDO!)")
    
    # Resultado final
    print("\n" + "="*70)
    print("                    RESULTADO FINAL")
    print("="*70)
    
    percentual = (total_sucessos / total_testes) * 100 if total_testes > 0 else 0
    
    print(f"Total de testes: {total_testes}")
    print(f"Sucessos: {total_sucessos}")
    print(f"Falhas: {total_testes - total_sucessos}")
    print(f"Taxa de sucesso: {percentual:.1f}%")
    
    if percentual == 100:
        print("\n🎉 TODOS OS TESTES PASSARAM!")
    else:
        print(f"\n⚠️  {total_testes - total_sucessos} TESTES FALHARAM")
    
    return total_sucessos == total_testes

if __name__ == "__main__":
    testar_validadores()