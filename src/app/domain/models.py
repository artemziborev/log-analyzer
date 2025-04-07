from datetime import datetime

from pydantic import BaseModel


class LogLine(BaseModel):
    url: str
    request_time: float


class LogFileInfo(BaseModel):
    path: str
    ext: str  # ".gz" или ".log"
    date: datetime


from typing import TypedDict


class UrlStat(TypedDict):
    url: str
    count: int
    count_perc: float
    time_sum: float
    time_perc: float
    time_avg: float
    time_max: float
    time_med: float
