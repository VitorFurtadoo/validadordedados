@echo off
chcp 65001 >nul
title Validador de Dados Formal - UEPA
color 0A

echo.
echo ████████████████████████████████████████████████
echo           🎓 VALIDADOR DE DADOS FORMAL
echo        Universidade do Estado do Pará - UEPA
echo ████████████████████████████████████████████████
echo.

cd /d "%~dp0"

echo 🔍 Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado!
    echo.
    echo 💡 Soluções:
    echo 1. Instale Python do site oficial: https://python.org
    echo 2. Ou instale pela Microsoft Store
    echo 3. Ou adicione Python ao PATH do sistema
    pause
    exit /b 1
)

echo ✅ Python encontrado!
echo.
echo 🚀 Executando validador...
echo.

python executar.py

pause