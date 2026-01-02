import os
from simple_salesforce import Salesforce

class SalesforceAuth:
    """
    Responsável por autenticar no Salesforce usando variáveis de ambiente.
    """

    def __init__(self):
        self.username = os.getenv("SF_USERNAME")
        self.password = os.getenv("SF_PASSWORD")
        self.security_token = os.getenv("SF_SECURITY_TOKEN")
        self.domain = os.getenv("SF_DOMAIN", "login")

    def connect(self):
        if not all([self.username, self.password, self.security_token]):
            raise ValueError("Credenciais do Salesforce não configuradas corretamente.")

        return Salesforce(
            username=self.username,
            password=self.password,
            security_token=self.security_token,
            domain=self.domain
        )
