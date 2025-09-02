# 🎓 Validador de Dados Formal - Interface Web

## Descrição
Projeto acadêmico de **Linguagens Formais** da **Universidade do Estado do Pará (UEPA)** - Interface web interativa para validação de dados usando expressões regulares.

## 📁 Estrutura do Projeto HTML

```
html-validadores/
├── index.html              # Validador completo (todos os campos)
├── navegacao.html          # Página principal de navegação
├── script.js              # Lógica JavaScript dos validadores
├── styles.css             # Estilos CSS do projeto
├── validador-nome.html     # Validador individual - Nome Completo
├── validador-email.html    # Validador individual - E-mail
├── validador-senha.html    # Validador individual - Senha
├── validador-cpf.html      # Validador individual - CPF
├── validador-telefone.html # Validador individual - Telefone
└── validador-numero.html   # Validador individual - Número Decimal
```

## 🚀 Como Executar

1. **Abrir no navegador:**
   - Abra `navegacao.html` para acessar a página principal
   - Ou abra `index.html` para usar o validador completo

2. **Servidor local (opcional):**
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Node.js
   npx http-server
   ```

## 🧮 Validadores Disponíveis

### Individual (Páginas Separadas)
- **Nome Completo**: Primeiro nome + sobrenome, primeira letra maiúscula
- **E-mail**: Formato brasileiro (obrigatório .br)
- **Senha**: 8 caracteres, 1 maiúscula, 1 número
- **CPF**: Formato 123.456.789-09
- **Telefone**: Celular (91) 99999-9999
- **Número Decimal**: ±123.45 ou ±123,45

### Completo (Página Única)
- Todos os validadores em uma interface integrada
- Relatórios detalhados
- Estatísticas em tempo real

## 🎨 Recursos da Interface

- ✅ **Validação em tempo real** com feedback visual
- ✅ **Máscaras de input** automáticas
- ✅ **Espaços para autômatos finitos** (imagens)
- ✅ **Comentários técnicos do Pedro** integrados
- ✅ **Explicações detalhadas** das expressões regulares
- ✅ **Exemplos funcionais e não funcionais**
- ✅ **Design responsivo** (mobile-friendly)
- ✅ **Navegação integrada** entre páginas

## 🔧 Tecnologias Utilizadas

- **HTML5** - Estrutura semântica
- **CSS3** - Estilização moderna com gradientes e animações
- **JavaScript ES6+** - Lógica de validação e interatividade
- **Font Awesome** - Ícones
- **Google Fonts** - Tipografia (Inter)

## 📝 Expressões Regulares

| Campo | Regex | Descrição |
|-------|--------|-----------|
| Nome | `/^[A-Z][a-z]+ [A-Z][a-z]+$/` | Nome e sobrenome com maiúscula inicial |
| E-mail | `/^[a-z]+@[a-z]+\.br$/` | E-mail brasileiro simples |
| Senha | `/^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8}$/` | 8 chars, 1 maiúscula, 1 número |
| CPF | `/^\d{3}\.\d{3}\.\d{3}-\d{2}$/` | Formato CPF brasileiro |
| Telefone | `/^\(\d{2}\) \d{5}-\d{4}$/` | Celular brasileiro |
| Número | `/^[+-]?(\d+([.,]\d+)?|\d*[.,]\d+)$/` | Decimal com vírgula ou ponto |

## 👥 Desenvolvedores

- **Pedro** - Comentários técnicos e observações
- **Vitor** - Desenvolvimento e implementação
- **Equipe UEPA** - Projeto acadêmico

## 📚 Disciplina

**Linguagens Formais** - Engenharia de Software  
Universidade do Estado do Pará - UEPA  
**Ano:** 2025

## 🔗 Navegação

- `navegacao.html` → Página principal com todos os validadores
- `index.html` → Validador completo integrado
- `validador-*.html` → Validadores individuais com explicações detalhadas

---

*Projeto desenvolvido para fins educacionais - UEPA 2025*