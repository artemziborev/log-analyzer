import json
from string import Template
from src.app.domain.interfaces import IReporter

class HtmlReporter(IReporter):
    def __init__(self, template_path: str):
        self.template_path = template_path

    def render(self, table_data: list[dict], output_path: str) -> None:
        with open(self.template_path, encoding="utf-8") as tpl:
            template = Template(tpl.read())
        rendered = template.safe_substitute(table_json=json.dumps(table_data))
        with open(output_path, "w", encoding="utf-8") as out:
            out.write(rendered)
