import requests


def audit_headers(config):
    base_url = config["target"]["base_url"]
    required_headers = config["headers"]["required"]

    findings = []

    try:
        response = requests.get(base_url, timeout=5)
        response_headers = response.headers

        for header in required_headers:
            present = header in response_headers

            findings.append({
                "header": header,
                "present": present,
                "description": "Header is present"
                if present else "Missing recommended security header",
            })

    except requests.RequestException as error:
        findings.append({
            "error": str(error),
            "description": "Unable to audit security headers",
        })

    return findings