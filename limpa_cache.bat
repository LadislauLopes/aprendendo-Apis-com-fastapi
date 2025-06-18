@echo off
echo ===========================================
echo      LIMPEZA DE CACHE - PYTHON & VSCode
echo ===========================================

:: 1. Apagar __pycache__ recursivamente
echo.
echo Apagando __pycache__...
for /d /r %%i in (__pycache__) do (
    if exist "%%i" (
        echo Deletando %%i
        rmdir /s /q "%%i"
    )
)

:: 2. Apagar arquivos .pyc
echo.
echo Apagando arquivos .pyc...
del /s /q *.pyc

:: 3. Limpar cache do pip
echo.
echo Limpando cache do pip...
pip cache purge

:: 4. Limpar cache local do Python
echo.
echo Limpando cache local do Python...
rmdir /s /q "%LocalAppData%\pip\Cache" 2>nul
rmdir /s /q "%LocalAppData%\Python" 2>nul

:: 5. Limpar cache do VSCode (opcional)
set /p limparvscode="Deseja limpar o cache do VSCode também? (s/n): "
if /i "%limparvscode%"=="s" (
    echo Limpando cache do VSCode...
    rmdir /s /q "%APPDATA%\Code\Cache" 2>nul
    rmdir /s /q "%APPDATA%\Code\CachedData" 2>nul
    rmdir /s /q "%APPDATA%\Code\User\workspaceStorage" 2>nul
) else (
    echo Cache do VSCode mantido.
)

echo.
echo =========================
echo     LIMPEZA CONCLUÍDA!
echo =========================
pause
