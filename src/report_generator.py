import json
from datetime import datetime, timezone
from pathlib import Path


def save_report(results, output_file):
    report = {
        "scan_type": "OWASP Smoke Test",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "results": results,
    }

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as file:
        json.dump(report, file, indent=4)

    return report



