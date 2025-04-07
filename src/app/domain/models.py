from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class LogLine(BaseModel):
    url: str
    request_time: float

class LogFileInfo(BaseModel):
    path: str
    ext: str  # ".gz" или ".log"
    date: datetime


