from collections import defaultdict
from statistics import median
from typing import Iterable

from src.app.domain.interfaces import IAnalyzer
from src.app.domain.models import LogLine, UrlStat


class Analyzer(IAnalyzer):
    def process(self, entries: Iterable[LogLine]) -> list[UrlStat]:
        grouped = defaultdict(list)
        total_count = 0
        total_time = 0.0

        for entry in entries:
            grouped[entry.url].append(entry.request_time)
            total_count += 1
            total_time += entry.request_time

        report: list[UrlStat] = []
        for url, times in grouped.items():
            count = len(times)
            times_sorted = sorted(times)
            report.append(
                {
                    "url": url,
                    "count": count,
                    "count_perc": round(count / total_count * 100, 3),
                    "time_sum": round(sum(times), 3),
                    "time_perc": round(sum(times) / total_time * 100, 3),
                    "time_avg": round(sum(times) / count, 3),
                    "time_max": round(max(times), 3),
                    "time_med": round(median(times_sorted), 3),
                }
            )

        report.sort(key=lambda x: x["time_sum"], reverse=True)
        return report
