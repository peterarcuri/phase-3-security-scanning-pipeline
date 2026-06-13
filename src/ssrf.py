import requests


def test_ssrf(config):
    base_url = (
    config["target"]["base_url"]
    + config["endpoints"]["ssrf"]
    )
    parameter = config["target"]["test_parameter"]
    test_urls = config["ssrf"]["test_urls"]

    findings = []

    for test_url in test_urls:
        try:
            response = requests.get(
                base_url,
                params={parameter: test_url},
                timeout=5,
            )

            possible_ssrf = response.status_code in [200, 301, 302, 403, 500]

            findings.append({
                "test_url": test_url,
                "status_code": response.status_code,
                "potential_issue": possible_ssrf,
                "description": "Application may be processing external URL input"
                if possible_ssrf else "No SSRF indicator detected",
            })

        except requests.RequestException as error:
            findings.append({
                "test_url": test_url,
                "error": str(error),
                "potential_issue": False,
            })

    return findings

