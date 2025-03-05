# Proyecto Lambda Function

Este proyecto implementa una función Lambda en AWS utilizando Python para procesar solicitudes, manejar autenticación y realizar operaciones específicas.

## Estructura del Proyecto
lambda_function/  
│  
├── src/  
│   ├── config.py  
│   ├── lambda_function.py  
│   ├── libs/  
│   └── utils_app/  
│       └── util.py  
│  
└── README.md


### Descripción de los Archivos y Carpetas

#### `src/config.py`

Este archivo contiene las configuraciones y parámetros necesarios para el funcionamiento de la función Lambda, incluyendo:

- Constantes de configuración
- Claves secretas y valores de encriptación
- Códigos de flujo Lambda (LAMBDA_FLOW_CODE)

#### `src/lambda_function.py`

Este es el archivo principal que define la función Lambda. Sus características principales son:

- Manejo de eventos y contexto de AWS Lambda
- Procesamiento de solicitudes HTTP
- Autenticación y validación de tokens
- Desencriptación de credenciales
- Interacción con APIs externas (Comviva)
- Manejo de errores y respuestas

#### `src/libs/`

Esta carpeta contiene las dependencias y módulos utilizados en el proyecto:

##### `common_utils/`
- `constant.py`: Define constantes como códigos de respuesta y estados.
- `core.py`: Contiene la clase ComvivaApis para interactuar con APIs externas.
- `log.py`: Proporciona funcionalidades de logging.
- `tools.py`: Contiene herramientas útiles como codificación/decodificación base64.
- `aes.py`: Implementa el manejo de encriptación AES.

##### `tokenization_process/`
- `token_auth.py`: Maneja la autenticación y validación de tokens.

#### `src/utils_app/`

Esta carpeta contiene utilidades adicionales para el proyecto:

- `util.py`: Incluye funciones auxiliares utilizadas en diferentes partes del código.

#### `README.md`

- `README.md`: Documentación del proyecto
## Configuración y Despliegue

1. Asegúrese de tener instalado Python 3.x y AWS CLI en su máquina.
2. Clone este repositorio: 
git clone https://github.com/su-usuario/lambda_function.git
3. Navegue al directorio del proyecto:
`cd lambda_function`
4. Instale las dependencias necesarias:
`pip install -r requirements.txt`
5. Configure sus credenciales de AWS:
`aws configure`
6. Despliegue la función Lambda utilizando el script proporcionado:
`sam_lambda.sh` o `sam_lambda.cmd`


## Uso

La función Lambda está diseñada para manejar solicitudes HTTP. Asegúrese de proporcionar los siguientes encabezados en la solicitud:

- `Authorization`: Credenciales encriptadas
- `msisdn`: Número de teléfono codificado en base64
- `token`: Token de autenticación (opcional)

El cuerpo de la solicitud debe estar en formato JSON.

## Flujo de Ejecución

1. La función recibe y registra la solicitud.
2. Procesa los encabezados y el cuerpo de la solicitud.
3. Desencripta las credenciales de autorización.
4. Valida el token de acceso y el flujo.
5. Realiza login en la API de Comviva.
6. Devuelve una respuesta con datos codificados en base64.

## Manejo de Errores

La función captura y registra excepciones, devolviendo respuestas de error apropiadas con códigos de estado HTTP.

## Contribución

Si desea contribuir a este proyecto, por favor cree un fork del repositorio y envíe sus pull requests para revisión.

## Licencia

[Incluya aquí la información de la licencia de su proyecto]