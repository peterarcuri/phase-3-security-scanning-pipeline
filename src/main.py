import yaml
from src.sql_injection import test_sql_injection
from src.ssrf import test_ssrf
from src.header_audit import audit_headers
from src.cors_checker import check_cors
from src.report_generator import save_report


def load_config(path="config/config.yaml"):
    with open(path, "r") as file:
        return yaml.safe_load(file)
    

def main():
    config = load_config()
    base_url = config["target"]["base_url"]

    print("[*] Starting OWASP Smoke Testing Framework")
    print(f"[*] Target: {base_url}")

    results = {
        "target": base_url,
        "sql_injection": test_sql_injection(config),
        "ssrf": test_ssrf(config),
        "headers": audit_headers(config),
        "cors": check_cors(base_url),
    }

    save_report(results, config["report"]["output_file"])

    print("[+] Security smoke test complete")
    print(f"[+] Report saved to {config['report']['output_file']}")


if __name__ == "__main__":
    main()