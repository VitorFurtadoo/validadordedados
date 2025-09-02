# 🐍 Validador de Dados - Backend Python

## Descrição
Backend em Python do projeto **Validador de Dados Formal** - Implementações de validação usando expressões regulares com interfaces gráficas em Tkinter.

## 📁 Estrutura do Projeto Python

```
python-validadores/
├── validador_dados.py      # Módulo principal com classes de validação
├── interface_visual.py     # Interface gráfica completa (Tkinter)
├── interface_simples.py    # Interface simplificada
├── interface_validador.py  # Interface básica de validação
├── executar.py            # Script principal de execução
├── executar.bat           # Executor batch para Windows
├── teste_validadores.py   # Testes unitários
├── teste_interface.py     # Testes da interface
└── __pycache__/          # Cache Python
```

## 🚀 Como Executar

### Método 1: Executável Batch (Windows)
```bash
./executar.bat
```

### Método 2: Python Direto
```bash
python executar.py
```

### Método 3: Interface Específica
```bash
# Interface completa
python interface_visual.py

# Interface simples
python interface_simples.py

# Interface básica
python interface_validador.py
```

## 🧮 Funcionalidades

### Classes Principais

#### `ValidadorDados`
```python
from validador_dados import ValidadorDados

validator = ValidadorDados()
result = validator.validar_nome("Alan Turing")
```

**Métodos disponíveis:**
- `validar_nome(nome)` - Valida nome completo
- `validar_email(email)` - Valida e-mail brasileiro
- `validar_senha(senha)` - Valida senha segura
- `validar_cpf(cpf)` - Valida formato CPF
- `validar_telefone(telefone)` - Valida telefone celular
- `validar_numero_flutuante(numero)` - Valida números decimais

### Interfaces Gráficas

#### 1. Interface Visual (`interface_visual.py`)
- Interface completa com todos os validadores
- Feedback visual em tempo real
- Relatórios detalhados
- Estatísticas de validação

#### 2. Interface Simples (`interface_simples.py`)
- Interface básica e limpa
- Validação campo por campo
- Ideal para demonstrações

#### 3. Interface Validador (`interface_validador.py`)
- Interface minimalista
- Foco na funcionalidade core
- Rápida e responsiva

## 🔧 Dependências

```python
import re          # Expressões regulares
import tkinter     # Interface gráfica
import unittest    # Testes unitários
```

**Instalação (se necessário):**
```bash
# Tkinter já vem com Python
pip install --upgrade tkinter  # Se necessário
```

## 🧪 Testes

### Executar Testes
```bash
# Todos os testes
python -m unittest discover

# Teste específico
python teste_validadores.py
python teste_interface.py
```

### Cobertura de Testes
- ✅ Validação de todos os campos
- ✅ Casos funcionais e não funcionais
- ✅ Testes de interface
- ✅ Casos extremos

## 📝 Expressões Regulares (Python)

```python
PATTERNS = {
    'nome': r'^[A-Z][a-z]+ [A-Z][a-z]+$',
    'email': r'^[a-z]+@[a-z]+\.br$',
    'senha': r'^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8}$',
    'cpf': r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    'telefone': r'^\(\d{2}\) \d{5}-\d{4}$',
    'numero': r'^[+-]?(\d+([.,]\d+)?|\d*[.,]\d+)$'
}
```

## 🔍 Exemplos de Uso

### Validação Simples
```python
from validador_dados import ValidadorDados

v = ValidadorDados()

# Teste nome
print(v.validar_nome("Alan Turing"))  # True
print(v.validar_nome("alan turing"))  # False

# Teste e-mail
print(v.validar_email("user@domain.br"))  # True
print(v.validar_email("user@domain.com")) # False
```

### Interface Gráfica
```python
# Executar interface completa
from interface_visual import main
main()

# Executar interface simples
from interface_simples import main
main()
```

## 🐛 Debugging e Logs

### Modo Debug
```python
# Ativar debug no validador
validator = ValidadorDados(debug=True)
```

### Logs de Validação
- Todas as tentativas são logadas
- Padrões regex são exibidos
- Erros são capturados e tratados

## 📊 Performance

- **Validação:** ~0.001s por campo
- **Interface:** Responsiva em tempo real
- **Memória:** ~50MB para interface completa
- **Startup:** ~2s para carregar interface visual

## 👥 Desenvolvedores

- **Pedro** - Lógica de validação e testes
- **Vitor** - Interfaces gráficas e integração
- **Equipe UEPA** - Arquitetura e requisitos

## 📚 Disciplina

**Linguagens Formais** - Engenharia de Software  
Universidade do Estado do Pará - UEPA  
**Ano:** 2025

---

*Backend Python para validação de dados usando expressões regulares - UEPA 2025*