from dotenv import load_dotenv
from datetime import datetime, date
import csv
import os

from auth import SalesforceAuth

load_dotenv()

SOQL = """
SELECT
  Name,
  Status_da_garantia__c,
  Data_de_emissao__c,
  Data_de_vencimento__c,
  Servico__r.Name
FROM Garantia__c
"""

def classify_status(expiration_date_str):
    if not expiration_date_str:
        return "UNKNOWN"

    try:
        exp_date = datetime.fromisoformat(expiration_date_str).date()
    except Exception:
        return "UNKNOWN"

    return "ACTIVE" if exp_date >= date.today() else "EXPIRED"


def export_garantias(sf):
    os.makedirs("reports", exist_ok=True)

    result = sf.query_all(SOQL)
    records = result.get("records", [])

    with open("reports/garantias.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Numero",
            "Status Salesforce",
            "Data Emissao",
            "Data Vencimento",
            "Servico",
            "Status Calculado"
        ])

        for r in records:
            writer.writerow([
                r.get("Name"),
                r.get("Status_da_garantia__c"),
                r.get("Data_de_emissao__c"),
                r.get("Data_de_vencimento__c"),
                (r.get("Servico__r") or {}).get("Name"),
                classify_status(r.get("Data_de_vencimento__c"))
            ])

    print("Export concluído: reports/garantias.csv")


def main():
    auth = SalesforceAuth()
    sf = auth.connect()
    export_garantias(sf)


if __name__ == "__main__":
    main()
