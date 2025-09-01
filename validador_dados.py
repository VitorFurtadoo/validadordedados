import re
from typing import Dict, Tuple

class ValidadorDados:
    def __init__(self):
        self.patterns = self._compile_patterns()
    
    def _compile_patterns(self) -> Dict[str, re.Pattern]:
        return {
            'nome': re.compile(r'^[A-Z][a-z]+ [A-Z][a-z]+$'),
            'email': re.compile(r'^[a-z]+@[a-z]+\.br$'),
            'senha': re.compile(r'^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8}$'),
            'cpf': re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'),
            'rg': re.compile(r'^\d{6}-\d$'),
            'telefone': re.compile(r'^\(\d{2}\) \d{5}-\d{4}$'),
            'cep': re.compile(r'^\d{2}\.\d{3}-\d{3}$'),
            'data_horario': re.compile(r'^\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}$'),
            'numero_flutuante': re.compile(r'^[+-]?(\d+([.,]\d+)?|\d*[.,]\d+)$')
        }
    
    def validar_nome(self, nome: str) -> Tuple[bool, str]:
        if not nome or nome.startswith(' ') or nome.endswith(' '):
            return False, "Campo não pode estar vazio ou ter espaços no início/fim"
        
        if self.patterns['nome'].match(nome):
            return True, "Válido"
        return False, "Nome deve ter formato 'Nome Sobrenome' com primeira letra maiúscula"
    
    def validar_email(self, email: str) -> Tuple[bool, str]:
        if not email or email.startswith(' ') or email.endswith(' '):
            return False, "Campo não pode estar vazio ou ter espaços no início/fim"
        
        if self.patterns['email'].match(email):
            return True, "Válido"
        return False, "Email deve ter formato 'usuario@dominio.br' (apenas letras minúsculas)"
    
    def validar_senha(self, senha: str) -> Tuple[bool, str]:
        if not senha or senha.startswith(' ') or senha.endswith(' '):
            return False, "Campo não pode estar vazio ou ter espaços no início/fim"
        
        if self.patterns['senha'].match(senha):
            return True, "Válido"
        return False, "Senha deve ter 8 caracteres com pelo menos 1 maiúscula e 1 número"
    
    def validar_cpf(self, cpf: str) -> Tuple[bool, str]:
        if not cpf or cpf.startswith(' ') or cpf.endswith(' '):
            return False, "Campo não pode estar vazio ou ter espaços no início/fim"
        
        if self.patterns['cpf'].match(cpf):
            return True, "Válido"
        return False, "CPF deve ter formato '123.456.789-09'"
    
    def validar_rg(self, rg: str) -> Tuple[bool, str]:
        if not rg or rg.startswith(' ') or rg.endswith(' '):
            return False, "Campo não pode estar vazio ou ter espaços no início/fim"
        
        if self.patterns['rg'].match(rg):
            return True, "Válido"
        return False, "RG deve ter formato '123456-7'"
    
    def validar_telefone(self, telefone: str) -> Tuple[bool, str]:
        if not telefone or telefone.startswith(' ') or telefone.endswith(' '):
            return False, "Campo não pode estar vazio ou ter espaços no início/fim"
        
        if self.patterns['telefone'].match(telefone):
            return True, "Válido"
        return False, "Telefone deve ter formato '(91) 99999-9999'"
    
    def validar_cep(self, cep: str) -> Tuple[bool, str]:
        if not cep or cep.startswith(' ') or cep.endswith(' '):
            return False, "Campo não pode estar vazio ou ter espaços no início/fim"
        
        if self.patterns['cep'].match(cep):
            return True, "Válido"
        return False, "CEP deve ter formato '66.645-225'"
    
    def validar_data_horario(self, data_horario: str) -> Tuple[bool, str]:
        if not data_horario or data_horario.startswith(' ') or data_horario.endswith(' '):
            return False, "Campo não pode estar vazio ou ter espaços no início/fim"
        
        if self.patterns['data_horario'].match(data_horario):
            return True, "Válido"
        return False, "Data/horário deve ter formato 'dd/mm/aaaa hh:mm:ss'"
    
    def validar_numero_flutuante(self, numero: str) -> Tuple[bool, str]:
        if not numero or numero.startswith(' ') or numero.endswith(' '):
            return False, "Campo não pode estar vazio ou ter espaços no início/fim"
        
        if self.patterns['numero_flutuante'].match(numero):
            return True, "Válido"
        return False, "Número deve ter formato '+/-123.45' ou '123,45' (com ou sem sinal)"
    
    def validar_todos_campos(self, dados: Dict[str, str]) -> Dict[str, Tuple[bool, str]]:
        resultados = {}
        
        if 'nome' in dados:
            resultados['nome'] = self.validar_nome(dados['nome'])
        if 'email' in dados:
            resultados['email'] = self.validar_email(dados['email'])
        if 'senha' in dados:
            resultados['senha'] = self.validar_senha(dados['senha'])
        if 'cpf' in dados:
            resultados['cpf'] = self.validar_cpf(dados['cpf'])
        if 'rg' in dados:
            resultados['rg'] = self.validar_rg(dados['rg'])
        if 'telefone' in dados:
            resultados['telefone'] = self.validar_telefone(dados['telefone'])
        if 'cep' in dados:
            resultados['cep'] = self.validar_cep(dados['cep'])
        if 'data_horario' in dados:
            resultados['data_horario'] = self.validar_data_horario(dados['data_horario'])
        if 'numero_flutuante' in dados:
            resultados['numero_flutuante'] = self.validar_numero_flutuante(dados['numero_flutuante'])
        
        return resultados

if __name__ == "__main__":
    validador = ValidadorDados()
    
    exemplos_validos = {
        'nome': "Alan Turing",
        'email': "bes@uepa.br",
        'senha': "518R2r5e",
        'cpf': "123.456.789-09",
        'rg': "875467-2",
        'telefone': "(91) 99999-9999",
        'cep': "66.645-225",
        'data_horario': "02/09/2025 23:59:59",
        'numero_flutuante': "-25.467"
    }
    
    print("=== TESTANDO EXEMPLOS VÁLIDOS ===")
    resultados = validador.validar_todos_campos(exemplos_validos)
    
    for campo, (valido, mensagem) in resultados.items():
        status = "✓" if valido else "✗"
        print(f"{status} {campo}: {exemplos_validos[campo]} -> {mensagem}")