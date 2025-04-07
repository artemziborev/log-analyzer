from pathlib import Path

import pytest

from app.domain.models import LogFileInfo
from app.services.parser import LogParser

TEST_LOG = """
127.0.0.1 - - [01/Apr/2025:00:00:01 +0000] "GET /home HTTP/1.1" 200 1234 "-" "curl" "-" 0.123
127.0.0.1 - - [01/Apr/2025:00:00:02 +0000] "POST /form HTTP/1.1" 200 4321 "-" "curl" "-" 0.456
bad log line
"""


def test_log_parser(tmp_path: Path) -> None:
    log_path = tmp_path / "access.log"
    log_path.write_text(TEST_LOG.strip())

    file_info = LogFileInfo(
        path=str(log_path), ext=".log", date=None  # дата в тесте не проверяется
    )

    parser = LogParser()
    parsed = list(parser.parse(file_info))
    assert len(parsed) == 2
    assert parsed[0].url == "/home"
    assert parsed[0].request_time == 0.123


def test_parser_error_threshold(tmp_path: Path) -> None:
    bad_log = "invalid\n" * 10
    log_path = tmp_path / "bad.log"
    log_path.write_text(bad_log)

    file_info = LogFileInfo(path=str(log_path), ext=".log", date=None)

    parser = LogParser()
    with pytest.raises(ValueError):
        list(parser.parse(file_info))
