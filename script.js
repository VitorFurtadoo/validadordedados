// Validador de Dados Formal - JavaScript
class ValidadorDados {
    constructor() {
        // Expressões regulares para cada campo
        this.patterns = {
            nome: /^[A-Z][a-z]+ [A-Z][a-z]+$/,
            email: /^[a-z]+@[a-z]+\.br$/,
            senha: /^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8}$/,
            cpf: /^\d{3}\.\d{3}\.\d{3}-\d{2}$/,
            rg: /^\d{6}-\d$/,
            telefone: /^\(\d{2}\) \d{5}-\d{4}$/,
            cep: /^\d{2}\.\d{3}-\d{3}$/,
            dataHorario: /^\d{2}\/\d{2}\/\d{4} \d{2}:\d{2}:\d{2}$/,
            numeroFlutuante: /^[+-]?(\d+([.,]\d+)?|\d*[.,]\d+)$/
        };

        // Nomes amigáveis dos campos
        this.fieldNames = {
            nome: 'Nome Completo',
            email: 'E-mail',
            senha: 'Senha',
            cpf: 'CPF',
            rg: 'RG',
            telefone: 'Telefone',
            cep: 'CEP',
            dataHorario: 'Data e Horário',
            numeroFlutuante: 'Número Decimal'
        };

        // Mensagens de erro específicas
        this.errorMessages = {
            nome: 'Nome deve ter formato "Nome Sobrenome" com primeira letra maiúscula',
            email: 'Email deve ter formato "usuario@dominio.br" (apenas letras minúsculas)',
            senha: 'Senha deve ter 8 caracteres com pelo menos 1 maiúscula e 1 número',
            cpf: 'CPF deve ter formato "123.456.789-09"',
            rg: 'RG deve ter formato "123456-7"',
            telefone: 'Telefone deve ter formato "(91) 99999-9999"',
            cep: 'CEP deve ter formato "66.645-225"',
            dataHorario: 'Data/horário deve ter formato "dd/mm/aaaa hh:mm:ss"',
            numeroFlutuante: 'Número deve ter formato "+/-123.45" ou "123,45" (com ou sem sinal)'
        };

        this.init();
    }

    init() {
        this.setupEventListeners();
        this.setupInputMasks();
        this.updateStats();
    }

    setupEventListeners() {
        // Event listeners para validação em tempo real
        const fields = ['nome', 'email', 'senha', 'cpf', 'rg', 'telefone', 'cep', 'dataHorario', 'numeroFlutuante'];
        
        fields.forEach(fieldId => {
            const input = document.getElementById(fieldId);
            if (input) {
                input.addEventListener('input', () => this.validateFieldRealtime(fieldId));
                input.addEventListener('blur', () => this.validateFieldRealtime(fieldId));
                input.addEventListener('focus', () => this.clearPlaceholder(input));
            }
        });

        // Event listeners para botões
        document.getElementById('validateAll')?.addEventListener('click', () => this.validateAll());
        document.getElementById('clearAll')?.addEventListener('click', () => this.clearAll());
        document.getElementById('showExamples')?.addEventListener('click', () => this.showExamples());
        document.getElementById('generateReport')?.addEventListener('click', () => this.generateReport());

        // Event listeners para modais
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('modal')) {
                this.closeAllModals();
            }
        });

        // Event listeners para teclas
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeAllModals();
            }
            if (e.ctrlKey && e.key === 'Enter') {
                e.preventDefault();
                this.validateAll();
            }
        });
    }

    setupInputMasks() {
        // Máscara para CPF
        const cpfInput = document.getElementById('cpf');
        if (cpfInput) {
            cpfInput.addEventListener('input', (e) => {
                let value = e.target.value.replace(/\D/g, '');
                value = value.replace(/(\d{3})(\d)/, '$1.$2');
                value = value.replace(/(\d{3})(\d)/, '$1.$2');
                value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
                e.target.value = value;
            });
        }

        // Máscara para RG
        const rgInput = document.getElementById('rg');
        if (rgInput) {
            rgInput.addEventListener('input', (e) => {
                let value = e.target.value.replace(/\D/g, '');
                value = value.replace(/(\d{6})(\d)/, '$1-$2');
                e.target.value = value;
            });
        }

        // Máscara para Telefone
        const telefoneInput = document.getElementById('telefone');
        if (telefoneInput) {
            telefoneInput.addEventListener('input', (e) => {
                let value = e.target.value.replace(/\D/g, '');
                value = value.replace(/(\d{2})(\d)/, '($1) $2');
                value = value.replace(/(\d{5})(\d{1,4})$/, '$1-$2');
                e.target.value = value;
            });
        }

        // Máscara para CEP
        const cepInput = document.getElementById('cep');
        if (cepInput) {
            cepInput.addEventListener('input', (e) => {
                let value = e.target.value.replace(/\D/g, '');
                value = value.replace(/(\d{2})(\d)/, '$1.$2');
                value = value.replace(/(\d{3})(\d{1,3})$/, '$1-$2');
                e.target.value = value;
            });
        }

        // Máscara para Data/Horário
        const dataHorarioInput = document.getElementById('dataHorario');
        if (dataHorarioInput) {
            dataHorarioInput.addEventListener('input', (e) => {
                let value = e.target.value.replace(/\D/g, '');
                value = value.replace(/(\d{2})(\d)/, '$1/$2');
                value = value.replace(/(\d{2})(\d)/, '$1/$2');
                value = value.replace(/(\d{4})(\d)/, '$1 $2');
                value = value.replace(/(\d{2})(\d)/, '$1:$2');
                value = value.replace(/(\d{2})(\d{1,2})$/, '$1:$2');
                e.target.value = value;
            });
        }
    }

    clearPlaceholder(input) {
        if (input.value === input.placeholder) {
            input.value = '';
        }
    }

    validateField(fieldId, value) {
        // Verificar se campo está vazio ou contém apenas espaços
        if (!value || !value.trim()) {
            return {
                valid: false,
                message: 'Campo não pode estar vazio'
            };
        }

        // Verificar se começa ou termina com espaço
        if (value.startsWith(' ') || value.endsWith(' ')) {
            return {
                valid: false,
                message: 'Campo não pode começar ou terminar com espaço'
            };
        }

        // Verificar se não é igual ao placeholder
        const input = document.getElementById(fieldId);
        if (input && value === input.getAttribute('data-example')) {
            return {
                valid: false,
                message: 'Digite um valor válido'
            };
        }

        // Validar com regex
        const pattern = this.patterns[fieldId];
        if (pattern && pattern.test(value)) {
            return {
                valid: true,
                message: 'Válido'
            };
        }

        return {
            valid: false,
            message: this.errorMessages[fieldId] || 'Formato inválido'
        };
    }

    validateFieldRealtime(fieldId) {
        const input = document.getElementById(fieldId);
        const resultElement = document.getElementById(`${fieldId}-result`);
        const fieldCard = input.closest('.field-card');
        
        if (!input || !resultElement) return;

        const value = input.value.trim();
        
        // Se campo vazio, resetar estado
        if (!value) {
            this.resetFieldState(fieldId, input, resultElement, fieldCard);
            this.updateStats();
            return;
        }

        const validation = this.validateField(fieldId, value);
        this.updateFieldState(fieldId, validation, input, resultElement, fieldCard);
        this.updateStats();
    }

    resetFieldState(fieldId, input, resultElement, fieldCard) {
        input.classList.remove('valid', 'invalid');
        fieldCard.classList.remove('valid', 'invalid');
        resultElement.classList.remove('valid', 'invalid');
        resultElement.innerHTML = '<i class="fas fa-keyboard"></i> Digite para validar...';
    }

    updateFieldState(fieldId, validation, input, resultElement, fieldCard) {
        // Remover classes antigas
        input.classList.remove('valid', 'invalid');
        fieldCard.classList.remove('valid', 'invalid');
        resultElement.classList.remove('valid', 'invalid');

        if (validation.valid) {
            input.classList.add('valid');
            fieldCard.classList.add('valid');
            resultElement.classList.add('valid');
            resultElement.innerHTML = `<i class="fas fa-check-circle"></i> ${validation.message}`;
        } else {
            input.classList.add('invalid');
            fieldCard.classList.add('invalid');
            resultElement.classList.add('invalid');
            resultElement.innerHTML = `<i class="fas fa-times-circle"></i> ${validation.message}`;
        }
    }

    getAllFieldValues() {
        const fields = ['nome', 'email', 'senha', 'cpf', 'rg', 'telefone', 'cep', 'dataHorario', 'numeroFlutuante'];
        const values = {};

        fields.forEach(fieldId => {
            const input = document.getElementById(fieldId);
            if (input && input.value.trim()) {
                values[fieldId] = input.value.trim();
            }
        });

        return values;
    }

    validateAll() {
        const values = this.getAllFieldValues();
        
        if (Object.keys(values).length === 0) {
            this.showNotification('Preencha pelo menos um campo para validar!', 'warning');
            return;
        }

        const results = {};
        Object.keys(values).forEach(fieldId => {
            results[fieldId] = this.validateField(fieldId, values[fieldId]);
        });

        this.displayResults(results, values);
        this.updateStats();
        
        // Scroll suave para resultados
        document.querySelector('.results-section').scrollIntoView({ 
            behavior: 'smooth', 
            block: 'start' 
        });
    }

    displayResults(results, values) {
        const resultsDisplay = document.getElementById('resultsDisplay');
        if (!resultsDisplay) return;

        let html = '<div class="validation-summary">';
        
        const validCount = Object.values(results).filter(r => r.valid).length;
        const totalCount = Object.keys(results).length;
        
        // Header do relatório
        html += `
            <div class="summary-header">
                <h3><i class="fas fa-clipboard-check"></i> Relatório de Validação Completa</h3>
                <div class="summary-stats">
                    <span class="stat-item valid">${validCount} válidos</span>
                    <span class="stat-item total">${totalCount} total</span>
                </div>
            </div>
        `;

        // Resultados individuais
        Object.keys(results).forEach(fieldId => {
            const result = results[fieldId];
            const value = values[fieldId];
            const fieldName = this.fieldNames[fieldId];
            
            html += `
                <div class="report-item ${result.valid ? 'valid' : 'invalid'}">
                    <h4>
                        <i class="fas fa-${result.valid ? 'check-circle' : 'times-circle'}"></i>
                        ${fieldName}
                    </h4>
                    <div class="value">${this.escapeHtml(value)}</div>
                    <div class="message">${result.message}</div>
                </div>
            `;
        });

        // Resumo final
        html += '<div class="final-summary">';
        if (validCount === totalCount) {
            html += `
                <div class="success-message">
                    <i class="fas fa-trophy"></i>
                    <h4>🎉 Parabéns! Todos os campos são válidos!</h4>
                    <p>Todos os ${totalCount} campos passaram na validação com expressões regulares.</p>
                </div>
            `;
        } else {
            const errorCount = totalCount - validCount;
            html += `
                <div class="error-message">
                    <i class="fas fa-exclamation-triangle"></i>
                    <h4>⚠️ Alguns campos precisam de atenção</h4>
                    <p>${errorCount} campo${errorCount > 1 ? 's' : ''} com erro de ${totalCount} total.</p>
                </div>
            `;
        }
        html += '</div>';

        html += '</div>';
        resultsDisplay.innerHTML = html;
    }

    updateStats() {
        const fields = ['nome', 'email', 'senha', 'cpf', 'rg', 'telefone', 'cep', 'dataHorario', 'numeroFlutuante'];
        let validCount = 0;
        let invalidCount = 0;
        let totalCount = 0;

        fields.forEach(fieldId => {
            const input = document.getElementById(fieldId);
            if (input && input.value.trim()) {
                totalCount++;
                if (input.classList.contains('valid')) {
                    validCount++;
                } else if (input.classList.contains('invalid')) {
                    invalidCount++;
                }
            }
        });

        // Atualizar elementos de estatísticas
        const validCountEl = document.getElementById('validCount');
        const invalidCountEl = document.getElementById('invalidCount');
        const totalCountEl = document.getElementById('totalCount');

        if (validCountEl) validCountEl.textContent = validCount;
        if (invalidCountEl) invalidCountEl.textContent = invalidCount;
        if (totalCountEl) totalCountEl.textContent = totalCount;
    }

    clearAll() {
        const fields = ['nome', 'email', 'senha', 'cpf', 'rg', 'telefone', 'cep', 'dataHorario', 'numeroFlutuante'];
        
        fields.forEach(fieldId => {
            const input = document.getElementById(fieldId);
            const resultElement = document.getElementById(`${fieldId}-result`);
            const fieldCard = input?.closest('.field-card');
            
            if (input) {
                input.value = '';
                this.resetFieldState(fieldId, input, resultElement, fieldCard);
            }
        });

        // Limpar área de resultados
        const resultsDisplay = document.getElementById('resultsDisplay');
        if (resultsDisplay) {
            resultsDisplay.innerHTML = `
                <div class="welcome-message">
                    <i class="fas fa-broom"></i>
                    <h3>Campos Limpos!</h3>
                    <p>Todos os campos foram limpos. Comece a digitar para validar novamente.</p>
                </div>
            `;
        }

        this.updateStats();
        this.showNotification('Todos os campos foram limpos!', 'success');
    }

    showExamples() {
        const modal = document.getElementById('examplesModal');
        if (modal) {
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    }

    generateReport() {
        const values = this.getAllFieldValues();
        
        if (Object.keys(values).length === 0) {
            this.showNotification('Preencha pelo menos um campo para gerar relatório!', 'warning');
            return;
        }

        const results = {};
        Object.keys(values).forEach(fieldId => {
            results[fieldId] = this.validateField(fieldId, values[fieldId]);
        });

        const reportContent = document.getElementById('reportContent');
        const modal = document.getElementById('reportModal');
        
        if (!reportContent || !modal) return;

        let html = `
            <div class="report-header">
                <h3><i class="fas fa-file-alt"></i> Relatório Técnico Detalhado</h3>
                <p class="report-date">Gerado em: ${new Date().toLocaleString('pt-BR')}</p>
            </div>
            <div class="report-stats-detailed">
                <div class="stat-card">
                    <i class="fas fa-check-circle"></i>
                    <span class="number">${Object.values(results).filter(r => r.valid).length}</span>
                    <span class="label">Campos Válidos</span>
                </div>
                <div class="stat-card">
                    <i class="fas fa-times-circle"></i>
                    <span class="number">${Object.values(results).filter(r => !r.valid).length}</span>
                    <span class="label">Campos Inválidos</span>
                </div>
                <div class="stat-card">
                    <i class="fas fa-list"></i>
                    <span class="number">${Object.keys(results).length}</span>
                    <span class="label">Total Testados</span>
                </div>
            </div>
        `;

        // Detalhes técnicos
        html += '<div class="technical-details">';
        Object.keys(results).forEach(fieldId => {
            const result = results[fieldId];
            const value = values[fieldId];
            const fieldName = this.fieldNames[fieldId];
            const regex = this.patterns[fieldId].toString();
            
            html += `
                <div class="tech-report-item ${result.valid ? 'valid' : 'invalid'}">
                    <div class="tech-header">
                        <h4>
                            <i class="fas fa-${result.valid ? 'check-circle' : 'times-circle'}"></i>
                            ${fieldName}
                        </h4>
                        <span class="status-badge ${result.valid ? 'valid' : 'invalid'}">
                            ${result.valid ? 'VÁLIDO' : 'INVÁLIDO'}
                        </span>
                    </div>
                    <div class="tech-details">
                        <div class="detail-row">
                            <strong>Valor Testado:</strong>
                            <code>${this.escapeHtml(value)}</code>
                        </div>
                        <div class="detail-row">
                            <strong>Regex Usado:</strong>
                            <code>${regex}</code>
                        </div>
                        <div class="detail-row">
                            <strong>Resultado:</strong>
                            <span class="${result.valid ? 'valid' : 'invalid'}">${result.message}</span>
                        </div>
                    </div>
                </div>
            `;
        });
        html += '</div>';

        reportContent.innerHTML = html;
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    closeModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    closeAllModals() {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => {
            modal.classList.remove('active');
        });
        document.body.style.overflow = '';
    }

    showNotification(message, type = 'info') {
        // Criar notificação toast
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <i class="fas fa-${this.getNotificationIcon(type)}"></i>
            <span>${message}</span>
        `;
        
        // Adicionar estilos inline
        Object.assign(notification.style, {
            position: 'fixed',
            top: '20px',
            right: '20px',
            padding: '15px 20px',
            borderRadius: '8px',
            color: 'white',
            fontWeight: '500',
            zIndex: '9999',
            display: 'flex',
            alignItems: 'center',
            gap: '10px',
            minWidth: '300px',
            boxShadow: '0 4px 12px rgba(0,0,0,0.15)',
            transform: 'translateX(100%)',
            transition: 'transform 0.3s ease'
        });

        // Cores baseadas no tipo
        const colors = {
            success: '#10b981',
            error: '#ef4444',
            warning: '#f59e0b',
            info: '#3b82f6'
        };
        notification.style.background = colors[type] || colors.info;

        document.body.appendChild(notification);

        // Animar entrada
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 10);

        // Remover após 3 segundos
        setTimeout(() => {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                document.body.removeChild(notification);
            }, 300);
        }, 3000);
    }

    getNotificationIcon(type) {
        const icons = {
            success: 'check-circle',
            error: 'times-circle',
            warning: 'exclamation-triangle',
            info: 'info-circle'
        };
        return icons[type] || icons.info;
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Função global para alternar visibilidade da senha
function togglePassword(fieldId) {
    const input = document.getElementById(fieldId);
    const icon = input.nextElementSibling.querySelector('i');
    
    if (input.type === 'password') {
        input.type = 'text';
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        input.type = 'password';
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}

// Função global para fechar modais
function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }
}

// Inicializar quando DOM estiver carregado
document.addEventListener('DOMContentLoaded', () => {
    new ValidadorDados();
    
    // Adicionar estilos CSS adicionais para notificações e relatórios
    const additionalStyles = `
        <style>
            .validation-summary {
                animation: slideIn 0.5s ease-out;
            }
            
            .summary-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 2rem;
                padding-bottom: 1rem;
                border-bottom: 2px solid #e5e7eb;
            }
            
            .summary-stats {
                display: flex;
                gap: 1rem;
            }
            
            .stat-item {
                padding: 0.5rem 1rem;
                border-radius: 0.5rem;
                font-weight: 600;
                font-size: 0.9rem;
            }
            
            .stat-item.valid {
                background: #d1fae5;
                color: #065f46;
            }
            
            .stat-item.total {
                background: #dbeafe;
                color: #1e40af;
            }
            
            .final-summary {
                margin-top: 2rem;
                padding-top: 2rem;
                border-top: 2px solid #e5e7eb;
                text-align: center;
            }
            
            .success-message, .error-message {
                padding: 2rem;
                border-radius: 1rem;
                margin: 1rem 0;
            }
            
            .success-message {
                background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
                color: #065f46;
            }
            
            .error-message {
                background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
                color: #991b1b;
            }
            
            .success-message i, .error-message i {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            
            .report-header {
                text-align: center;
                margin-bottom: 2rem;
                padding-bottom: 1rem;
                border-bottom: 1px solid #e5e7eb;
            }
            
            .report-date {
                color: #6b7280;
                font-size: 0.9rem;
                margin-top: 0.5rem;
            }
            
            .report-stats-detailed {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 1rem;
                margin-bottom: 2rem;
            }
            
            .stat-card {
                text-align: center;
                padding: 1.5rem;
                background: #f9fafb;
                border-radius: 0.75rem;
                border: 1px solid #e5e7eb;
            }
            
            .stat-card i {
                font-size: 2rem;
                margin-bottom: 0.5rem;
                color: #667eea;
            }
            
            .stat-card .number {
                display: block;
                font-size: 2rem;
                font-weight: 700;
                color: #1f2937;
            }
            
            .stat-card .label {
                font-size: 0.875rem;
                color: #6b7280;
                font-weight: 500;
            }
            
            .tech-report-item {
                margin-bottom: 1.5rem;
                border-radius: 0.75rem;
                overflow: hidden;
                border: 2px solid #e5e7eb;
            }
            
            .tech-report-item.valid {
                border-color: #10b981;
            }
            
            .tech-report-item.invalid {
                border-color: #ef4444;
            }
            
            .tech-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 1rem;
                background: #f9fafb;
                border-bottom: 1px solid #e5e7eb;
            }
            
            .status-badge {
                padding: 0.25rem 0.75rem;
                border-radius: 9999px;
                font-size: 0.75rem;
                font-weight: 600;
            }
            
            .status-badge.valid {
                background: #d1fae5;
                color: #065f46;
            }
            
            .status-badge.invalid {
                background: #fee2e2;
                color: #991b1b;
            }
            
            .tech-details {
                padding: 1rem;
            }
            
            .detail-row {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 0.75rem;
                padding: 0.5rem 0;
                border-bottom: 1px solid #f3f4f6;
            }
            
            .detail-row:last-child {
                border-bottom: none;
                margin-bottom: 0;
            }
            
            .detail-row code {
                background: #f3f4f6;
                padding: 0.25rem 0.5rem;
                border-radius: 0.25rem;
                font-family: 'Courier New', monospace;
                font-size: 0.875rem;
                max-width: 60%;
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            }
            
            @keyframes slideIn {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
        </style>
    `;
    
    document.head.insertAdjacentHTML('beforeend', additionalStyles);
});