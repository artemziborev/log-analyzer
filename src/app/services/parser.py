import re
import gzip
from typing import Iterable
from src.app.domain.interfaces import ILogParser
from src.app.domain.models import LogFileInfo, LogLine

class LogParser(ILogParser):
    LOG_PATTERN = re.compile(
        r'"[A-Z]+ (?P<url>\S+)[^\"]*".*? (?P<request_time>[\d\.]+)$'
    )

    def parse(self, file: LogFileInfo) -> Iterable[LogLine]:
        open_func = gzip.open if file.ext == ".gz" else open
        total = 0
        errors = 0

        with open_func(file.path, mode="rt", encoding="utf-8") as f:
            for line in f:
                total += 1
                match = self.LOG_PATTERN.search(line)
                if not match:
                    errors += 1
                    continue
                try:
                    yield LogLine(
                        url=match.group("url"),
                        request_time=float(match.group("request_time"))
                    )
                except Exception:
                    errors += 1

        if total and errors / total > 0.2:
            raise ValueError(f"Parsing error rate too high: {errors / total:.2%}")
