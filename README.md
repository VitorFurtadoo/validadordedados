# Validador de Dados Formal

## Descrição

Este projeto implementa um validador de dados formal usando expressões regulares para validar diferentes tipos de campos de formulário, conforme especificações acadêmicas da disciplina de Linguagens Formais.

## Campos Validados

### 1. Nome
- **Formato**: Nome Sobrenome
- **Regras**: Primeiro símbolo maiúsculo, demais minúsculos, sem números ou caracteres especiais
- **Exemplo**: "Alan Turing", "Noam Chomsky"

### 2. E-mail
- **Formato**: usuario@dominio.br
- **Regras**: Exatamente um "@", terminar com ".br", apenas letras minúsculas
- **Exemplo**: "a@a.br", "bes@uepa.br"

### 3. Senha
- **Formato**: 8 caracteres
- **Regras**: Pelo menos 1 maiúscula, 1 número, sem caracteres especiais
- **Exemplo**: "518R2r5e", "F1234567"

### 4. CPF
- **Formato**: 123.456.789-09
- **Regras**: 11 dígitos com pontos e hífen nas posições corretas
- **Exemplo**: "123.456.789-09"

### 5. RG
- **Formato**: 123456-7
- **Regras**: 7 dígitos com hífen na 6ª posição
- **Exemplo**: "875467-2"

### 6. Telefone
- **Formato**: (91) 99999-9999
- **Regras**: DDD entre parênteses, espaço, 5 dígitos, hífen, 4 dígitos
- **Exemplo**: "(91) 99999-9999"

### 7. CEP
- **Formato**: 66.645-225
- **Regras**: 2 dígitos, ponto, 3 dígitos, hífen, 3 dígitos
- **Exemplo**: "66.645-225"

### 8. Data e Horário
- **Formato**: dd/mm/aaaa hh:mm:ss
- **Regras**: Data no formato brasileiro com horário 24h
- **Exemplo**: "02/09/2025 23:59:59"

### 9. Número de Ponto Flutuante
- **Formato**: +/-123.45 ou 123,45
- **Regras**: Sinal opcional, separador decimal (. ou ,), números inteiros aceitos
- **Exemplo**: "-25.467", "1", "+64,2"

## Arquivos do Projeto

- `validador_dados.py`: Classe principal com os validadores e expressões regulares
- `interface_visual.py`: **Interface gráfica moderna com tkinter** ⭐
- `interface_validador.py`: Interface interativa de linha de comando
- `teste_validadores.py`: Suite de testes completa
- `executar.py`: Arquivo principal de execução
- `README.md`: Este arquivo de documentação

## 🚀 Como Usar

### 1. Interface Visual (Recomendada) ⭐
```bash
python executar.py
```
ou
```bash
python interface_visual.py
```

**Funcionalidades da Interface Visual:**
- 🎨 Design moderno e responsivo
- ⚡ Validação em tempo real enquanto digita
- 📋 Placeholders com exemplos
- 🎯 Feedback visual instantâneo com ✅/❌
- 📊 Relatórios detalhados
- 📋 Janela de exemplos válidos
- 🔍 Área de resultados com syntax highlighting
- ⌨️ Atalhos: Ctrl+Enter (validar), Ctrl+L (limpar), F1 (exemplos)

### 2. Interface de Linha de Comando
```bash
python interface_validador.py
```

### 3. Executar Testes Automáticos
```bash
python teste_validadores.py
```

### 4. Usar como Módulo Python
```python
from validador_dados import ValidadorDados

validador = ValidadorDados()
valido, mensagem = validador.validar_email("teste@uepa.br")
print(f"Resultado: {valido} - {mensagem}")
```

## Funcionalidades da Interface

1. **Validação Individual**: Teste cada tipo de campo separadamente
2. **Validação Completa**: Valide todos os campos de uma vez
3. **Exemplos**: Visualize exemplos de entradas válidas
4. **Feedback Visual**: Resultados coloridos com símbolos ✓/✗

## Regras Gerais

- Campos não podem estar vazios
- Campos não podem começar ou terminar com espaços
- Todas as especificações devem ser satisfeitas simultaneamente
- Validação baseada em expressões regulares otimizadas

## Estrutura do Código

```
ValidadorDados/
├── validador_dados.py      # Classe principal
├── interface_validador.py  # Interface CLI
├── teste_validadores.py    # Suite de testes
└── README.md              # Documentação
```

## Tecnologias Utilizadas

- **Python 3**: Linguagem principal
- **Módulo `re`**: Expressões regulares
- **Typing**: Type hints para melhor legibilidade
- **OS**: Manipulação de terminal multiplataforma

## Testes Incluídos

- ✅ Casos válidos para todos os campos
- ✅ Casos inválidos para validação negativa  
- ✅ Casos especiais (vazio, espaços)
- ✅ Cobertura de 100% das regras especificadas

## Autor

Projeto desenvolvido para a disciplina de Linguagens Formais - Engenharia de Software, Universidade do Estado do Pará (UEPA).