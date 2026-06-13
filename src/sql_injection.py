import requests


DB_ERROR_SIGNATURES = [
    "sql syntax",
    "mysql",
    "postgresql",
    "sqlite",
    "ora-",
    "syntax error",
    "database error",    
]


def test_sql_injection(config):
    base_url = (
    config["target"]["base_url"]
    + config["endpoints"]["sql_injection"]
    )
    parameter = config["target"]["test_parameter"]
    payloads = config["sql_injection"]["payloads"]

    findings = []

    for payload in payloads:
        try:
            response = requests.get(
                base_url,
                params={parameter: payload},
                timeout=5,
            )

            body = response.text.lower()

            vulnerable = any(signature in body for signature in DB_ERROR_SIGNATURES)

            findings.append({
                "payload": payload,
                "status_code": response.status_code,
                "potential_issue": vulnerable,
                "description": "Possible SQL injection indicator detected"
                if vulnerable else "No SQL error signature detected",
            })

        except requests.RequestException as error:
            findings.append({
                "payload": payload,
                "error": str(error),
                "potential_issue": False,
            })

        return findings
    
