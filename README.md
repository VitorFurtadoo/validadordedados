# 🎓 Validador de Dados Formal - UEPA

## Descrição
Projeto acadêmico da disciplina **Linguagens Formais** da **Universidade do Estado do Pará (UEPA)**. Sistema completo de validação de dados usando expressões regulares, organizado em duas partes independentes: interface web e backend Python.

## 📁 Estrutura do Projeto

```
📦 Trabalho faculdade/
├── 📁 html-validadores/     # Interface Web Completa
│   ├── index.html           # Validador completo integrado
│   ├── navegacao.html       # Página principal de navegação
│   ├── validador-*.html     # Validadores individuais
│   ├── script.js           # Lógica JavaScript
│   ├── styles.css          # Estilos CSS
│   └── README.md           # Documentação HTML
│
├── 📁 python-validadores/   # Backend Python
│   ├── validador_dados.py   # Classes principais
│   ├── interface_*.py       # Interfaces Tkinter
│   ├── executar.py         # Script principal
│   ├── teste_*.py          # Testes unitários
│   └── README.md           # Documentação Python
│
└── README.md               # Este arquivo (visão geral)
```

## 🚀 Como Usar

### 🌐 Interface Web (Recomendado)
```bash
cd html-validadores/
# Abrir navegacao.html no navegador
# Ou usar servidor local:
python -m http.server 8000
```

### 🐍 Backend Python
```bash
cd python-validadores/
python executar.py
# ou
./executar.bat
```

## 🧮 Validadores Implementados

### 9 Tipos de Validação
1. **Nome Completo** - Formato "Nome Sobrenome" com maiúscula inicial
2. **E-mail** - Formato brasileiro (obrigatório .br)
3. **Senha Segura** - 8 caracteres, 1 maiúscula, 1 número
4. **CPF** - Formato brasileiro 123.456.789-09
5. **RG** - Formato 1234567-8
6. **Telefone** - Celular brasileiro (91) 99999-9999
7. **CEP** - Formato 66.645-225
8. **Data/Horário** - dd/mm/aaaa hh:mm:ss
9. **Número Decimal** - ±123.45 ou ±123,45

## 🔍 Expressões Regulares

| Campo | Regex | Exemplo |
|-------|-------|---------|
| Nome | `^[A-Z][a-z]+ [A-Z][a-z]+$` | Alan Turing |
| E-mail | `^[a-z]+@[a-z]+\.br$` | user@uepa.br |
| Senha | `^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8}$` | F1234567 |
| CPF | `^\d{3}\.\d{3}\.\d{3}-\d{2}$` | 123.456.789-09 |
| Telefone | `^\(\d{2}\) \d{5}-\d{4}$` | (91) 99999-9999 |
| Número | `^[+-]?(\d+([.,]\d+)?|\d*[.,]\d+)$` | -25.467 |

## 🎨 Recursos Principais

### Interface Web (HTML)
- ✅ **Navegação intuitiva** entre validadores
- ✅ **Páginas individuais** com explicações detalhadas
- ✅ **Espaços para autômatos finitos** (imagens)
- ✅ **Comentários técnicos do Pedro**
- ✅ **Exemplos funcionais e não funcionais**
- ✅ **Design responsivo** (mobile + desktop)
- ✅ **Validação em tempo real**

### Backend Python
- ✅ **Classes orientadas a objeto**
- ✅ **Interfaces gráficas Tkinter**
- ✅ **Testes unitários completos**
- ✅ **Múltiplas interfaces disponíveis**
- ✅ **Relatórios detalhados**

## 🧪 Testes e Exemplos

### Funcionais (Válidos) ✅
- Nome: "Alan Turing", "Marie Curie"
- E-mail: "test@uepa.br", "user@domain.br"
- Senha: "F1234567", "518R2r5e"
- CPF: "123.456.789-09"

### Não Funcionais (Inválidos) ❌
- Nome: "alan turing", "Alan123"
- E-mail: "user@gmail.com", "USER@UEPA.BR"
- Senha: "f1234567", "FABCDEFG"
- CPF: "12345678909", "123.456.789"

## 🛠️ Tecnologias

### Frontend
- **HTML5** - Estrutura semântica
- **CSS3** - Estilização moderna
- **JavaScript ES6+** - Interatividade
- **Font Awesome** - Ícones
- **Google Fonts** - Tipografia

### Backend
- **Python 3.x** - Lógica principal
- **Tkinter** - Interface gráfica
- **RegEx** - Validação de padrões
- **Unittest** - Testes automatizados

## 👥 Equipe de Desenvolvimento

- **Pedro** - Comentários técnicos, observações e melhorias
- **Vitor** - Desenvolvimento, implementação e documentação
- **Equipe UEPA** - Requisitos acadêmicos e revisão

## 📚 Contexto Acadêmico

**Disciplina:** Linguagens Formais  
**Curso:** Engenharia de Software  
**Instituição:** Universidade do Estado do Pará - UEPA  
**Ano:** 2025

**Objetivos:**
- Aplicação prática de expressões regulares
- Desenvolvimento de interfaces de usuário
- Validação formal de dados estruturados
- Implementação de autômatos finitos

## 📖 Documentação Detalhada

- [`html-validadores/README.md`](html-validadores/README.md) - Interface Web
- [`python-validadores/README.md`](python-validadores/README.md) - Backend Python

## 🚀 Início Rápido

1. **Para usar a interface web:**
   ```bash
   cd html-validadores/
   # Abrir navegacao.html no navegador
   ```

2. **Para usar o backend Python:**
   ```bash
   cd python-validadores/
   python executar.py
   ```

---

*Projeto educacional desenvolvido para demonstrar conceitos de Linguagens Formais através de validação de dados - UEPA 2025*