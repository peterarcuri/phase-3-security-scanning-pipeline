import json

from src.report_generator import save_report


def test_save_report_creates_json_file(tmp_path):
    sample_results = {
        "sql_injection": [],
        "ssrf": [],
        "cors": {},
        "headers": {},
    }

    output_file = tmp_path / "security-report.json"

    report = save_report(sample_results, output_file)

    # Verify the function returned the expected structure
    assert report["scan_type"] == "OWASP Smoke Test"
    assert report["results"] == sample_results
    assert "generated_at" in report

    # Verify the JSON file was written
    assert output_file.exists()

    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    assert loaded["scan_type"] == "OWASP Smoke Test"
    assert loaded["results"] == sample_results
    assert "generated_at" in loaded