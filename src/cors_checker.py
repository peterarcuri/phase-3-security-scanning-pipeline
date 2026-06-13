import requests



def check_cors(base_url):
    findings = []

    test_origin = "https://evil.example.com"

    try:
        response = requests.get(
            base_url,
            headers={"Origin": test_origin},
            timeout=5
        )

        allow_origin = response.headers.get("Access-Control-Allow-Origin")
        allow_credentials = response.headers.get("Access-Control-Allow-Credentials")

        insecure = allow_origin == "*" or allow_origin == test_origin

        findings.append({
            "access_control_allow_origin": allow_origin,
            "access_control_allow_credentials": allow_credentials,
            "potential_issue": insecure,
            "description": "Potential insecure CORS configuration detected"
            if insecure else "No Obivious CORS misconfiguration detected",
        })

    except requests.RequestException as error:
        findings.append({
            "error": str(error),
            "potential_issue": False,
        })
    
    return findings



