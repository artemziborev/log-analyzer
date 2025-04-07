import json
import os
import tempfile

from app.presentation.reporter import HtmlReporter


def test_reporter_creates_file() -> None:
    tpl = "<html><body>$table_json</body></html>"
    with tempfile.TemporaryDirectory() as tmpdir:
        template_path = os.path.join(tmpdir, "template.html")
        output_path = os.path.join(tmpdir, "report.html")
        with open(template_path, "w") as f:
            f.write(tpl)

        reporter = HtmlReporter(template_path)
        table = [{"url": "/a", "count": 1}]
        reporter.render(table, output_path)

        assert os.path.exists(output_path)
        with open(output_path) as f:
            assert json.dumps(table) in f.read()
