from sys import path

path.insert(1, "libs")

from json import loads

from common_utils.constant import (
    ConstantCodeResponse,
    ConstantResponseStatus,
)
from common_utils.core import (
    ComvivaApis,
)
from common_utils.log import Logger
from common_utils.tools import Tools
from common_utils.aes import AESManager

from tokenization_process.token_auth import TokenAuthManager

from config import Config, Secret

log = Logger.setup_logger(__name__)


def lambda_handler(event, _):
    Logger.log_request(log, event)

    try:
        event_body = loads(event["body"])
        event_headers = event["headers"]
        token = event_headers.get("token", None)
        auth = event_headers["Authorization"]
        msisdn_header = event_headers["msisdn"]
        msisdn_header_decode = Tools.decode_b64(msisdn_header)

        secret_encryption_value = Secret.secret_encryption_keys()
        aesmanage = AESManager(
            secret_encryption_value["KEY"], secret_encryption_value["IV"]
        )
        decrypted_text = aesmanage.decrypt_cryptography(auth)
        credentials = f"Basic {Tools.encode_b64(decrypted_text)}"

        token_auth = TokenAuthManager(Config.LAMBDA_FLOW_CODE, msisdn_header_decode)
        token_auth.initialize()
        response = token_auth.validate_flow_and_access_token(token)
        if not response["status"]:
            return response["response"]

        comviva = ComvivaApis()
        response_login = comviva.login(auth=credentials)

        if response_login.status_code != ConstantCodeResponse.CODE_200:
            raise ValueError(response_login.response_body["messageCore"])

        token = response_login.response_body["token"]["access_token"]
        return Tools.response(
            body={"data": Tools.encode_b64("data template")},
            headers={"token": "validar si requiere enviar token"},
        )
    except Exception as e:
        log.error("Exception lambda_handler: %s", e, exc_info=True)
        return Tools.response(
            status=ConstantResponseStatus.FAILED_STATUS,
            message=str(e),
            code_status=ConstantCodeResponse.CODE_500,
        )
