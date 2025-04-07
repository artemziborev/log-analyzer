from app.domain.models import LogLine
from app.services.analyzer import Analyzer


def test_analyzer_basic() -> None:
    analyzer = Analyzer()
    entries = [
        LogLine(url="/a", request_time=1.0),
        LogLine(url="/b", request_time=3.0),
        LogLine(url="/a", request_time=2.0),
    ]
    result = analyzer.process(entries)
    assert len(result) == 2
    result_by_url = {r["url"]: r for r in result}
    assert result_by_url["/a"]["count"] == 2
    assert result_by_url["/a"]["time_sum"] == 3.0
    assert result_by_url["/a"]["time_avg"] == 1.5
    assert result_by_url["/a"]["time_med"] == 2.0
