import os
import argparse
from datetime import datetime

from src.app.services.config_loader import load_config
from src.app.services.parser import LogParser
from src.app.services.analyzer import Analyzer
from src.app.presentation.reporter import HtmlReporter
from src.app.domain.models import LogFileInfo


def find_latest_log(log_dir: str) -> LogFileInfo | None:
    import re

    latest = None
    pattern = re.compile(r"nginx-access-ui.log-(\d{8})(\.gz|\.log)?$")
    for name in os.listdir(log_dir):
        match = pattern.match(name)
        if not match:
            continue
        date = datetime.strptime(match.group(1), "%Y%m%d")
        ext = match.group(2) or ""
        if not latest or date > latest.date:
            latest = LogFileInfo(path=os.path.join(log_dir, name), ext=ext, date=date)
    return latest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to config file", default=None)
    args = parser.parse_args()

    default_config = {
        "log_dir": "logs",
        "report_dir": "reports",
        "report_template": "templates/report.html",
        "report_size": 1000,
        "error_threshold": 0.2,
    }
    config = load_config(default_config, args.config)

    latest = find_latest_log(config["log_dir"])
    if not latest:
        print("No log file found")
        return

    output_path = os.path.join(
        config["report_dir"], f"report-{latest.date.strftime('%Y.%m.%d')}.html"
    )
    if os.path.exists(output_path):
        print("Report already exists")
        return

    parser = LogParser()
    analyzer = Analyzer()
    reporter = HtmlReporter(template_path=config["report_template"])

    parsed = parser.parse(latest)
    stats = analyzer.process(parsed)
    reporter.render(stats, output_path)

    print(f"Report generated: {output_path}")


if __name__ == "__main__":
    main()
