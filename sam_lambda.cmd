@echo off

REM Comprueba si se pasaron los parámetros
if "%1"=="" (
    echo Falta ingresar el perfil
    exit /b 1
)

if "%2"=="" (
    echo Falta ingresar el entorno de despliegue
    exit /b 1
)

REM Asigna los parámetros a variables
set PROFILE=%1
set CONFIG_ENV=%2

REM Validar que el config-env sea uno de los valores permitidos
set VALID_ENV=false
for %%v in (dev qa prd) do (
    if /i "%CONFIG_ENV%"=="%%v" set VALID_ENV=true
)

if "%VALID_ENV%"=="false" (
    echo Valor incorrecto del entorno: %CONFIG_ENV%
    echo Valores permitidos: dev, qa, prd
    exit /b 1
)

call sam package --profile %PROFILE% --config-env %CONFIG_ENV% --debug
call sam deploy --template-file package.yml --profile %PROFILE% --config-env %CONFIG_ENV% --debug