from abc import ABC, abstractmethod
from typing import List
from sqlalchemy import Engine

# ISP
# Split interfaces by capability

class MySQLWritable(ABC):

    @abstractmethod
    def write_mysql(self, engine: Engine, records: List[dict]):
        pass


class ElasticWritable(ABC):

    @abstractmethod
    def write_elastic(self, client, records: List[dict]):
        pass
