from pathlib import Path

import pytest

from src.app.domain.models import LogFileInfo
from src.app.services.parser import LogParser

TEST_LOG = """
1.2.3.4 - - [01/Jul/2017:00:00:00 +0300] "GET /index HTTP/1.1" 200 100 "-" "curl/7.58.0" "-" 0.100
1.2.3.5 - - [01/Jul/2017:00:00:01 +0300] "GET /api HTTP/1.1" 200 100 "-" "curl/7.58.0" "-" 0.200
1.2.3.6 - - [01/Jul/2017:00:00:02 +0300] "GET /index HTTP/1.1" 200 100 "-" "curl/7.58.0" "-" 0.300
""".strip()


def test_log_parser(tmp_path: Path) -> None:
    log_path = tmp_path / "access.log"
    log_path.write_text(TEST_LOG.strip())

    file_info = LogFileInfo(
        path=str(log_path), ext=".log", date=None  # дата в тесте не проверяется
    )

    parser = LogParser()
    parsed = list(parser.parse(file_info))
    assert len(parsed) == 3
    assert parsed[0].url == "/index"
    assert parsed[0].request_time == 0.1


def test_parser_error_threshold(tmp_path: Path) -> None:
    bad_log = "invalid\n" * 10
    log_path = tmp_path / "bad.log"
    log_path.write_text(bad_log)

    file_info = LogFileInfo(path=str(log_path), ext=".log", date=None)

    parser = LogParser()
    with pytest.raises(ValueError):
        list(parser.parse(file_info))
