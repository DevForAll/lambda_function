#!/bin/bash

# Comprueba si se pasaron los parámetros
if [ -z "$1" ]; then
    echo "Falta ingresar el perfil"
    exit 1
fi

if [ -z "$2" ]; then
    echo "Falta ingresar el entorno de despliegue"
    exit 1
fi

# Asigna los parámetros a variables
PROFILE=$1
CONFIG_ENV=$2

# Validar que el config-env sea uno de los valores permitidos
VALID_ENV=false
for v in dev qa prd; do
    if [ "$CONFIG_ENV" == "$v" ]; then
        VALID_ENV=true
        break
    fi
done

if [ "$VALID_ENV" == "false" ]; then
    echo "Valor incorrecto del entorno: $CONFIG_ENV"
    echo "Valores permitidos: dev, qa, prd"
    exit 1
fi

sam package --profile "$PROFILE" --config-env "$CONFIG_ENV" --debug
sam deploy --template-file package.yml --profile "$PROFILE" --config-env "$CONFIG_ENV" --debug