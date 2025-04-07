from abc import ABC, abstractmethod
from typing import Iterable
from src.app.domain.models import LogLine, LogFileInfo

class ILogParser(ABC):
    @abstractmethod
    def parse(self, file: LogFileInfo) -> Iterable[LogLine]:
        pass

class IAnalyzer(ABC):
    @abstractmethod
    def process(self, entries: Iterable[LogLine]) -> list[dict]:
        pass

class IReporter(ABC):
    @abstractmethod
    def render(self, table_data: list[dict], output_path: str) -> None:
        pass
