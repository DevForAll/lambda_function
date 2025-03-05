from os import getenv

from common_utils.constant import ConstantArn
from common_utils.resource_aws import ResourceAws


class Config:
    CONTEXTO = "GENERIC"
    IDENTIFIER_TYPE_RECEIVE = "userCode"
    TYPE_TRANSACTION_PRE_PAYMENT = "PAGO_PRE"
    CLARO = "claro"
    MOVISTAR = "movistar"
    ENTEL = "entel"
    BITEL = "bitel"
    OPERATORS = {
        "claro": CLARO,
        "movistar": MOVISTAR,
        "entel": ENTEL,
        "bitel": BITEL,
    }
    LAMBDA_FLOW_CODE = getenv("env_lambda_flow_code")
    SECRET_MYSQL = "smg-mdw-lambda-mysqldb-dbawspdp-app_bim_prod_1"
    ENVIRONMENT = getenv("envioronment")


class TableDB:
    db_trace_app_bim = "dyb-mdw-appbim-traza-app"


class ArnService:
    @staticmethod
    def get_arn_payment_bitel():
        return ConstantArn.get_route_init() + "lf-mdw-pago-bitel"


class Secret:
    @staticmethod
    def get_secret(secret):
        return ResourceAws.invoke_secret_manage().get_secret(secret)
