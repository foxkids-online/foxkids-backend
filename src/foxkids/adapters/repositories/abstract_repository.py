import abc
from abc import abstractmethod

from foxkids.domain import Block, Series


class AbstractRepository(abc.ABC):

    @abstractmethod
    def get_blocks(self, weekday: int | None = None) -> list[Block]:
        return NotImplemented

    @abstractmethod
    def get_series(self, name: str | None = None) -> list[Series]:
        return NotImplemented

    @abstractmethod
    def update_series_list(self, series_list: list[Series]):
        return NotImplemented

    @abstractmethod
    def update_blocks(self, blocks: list[Block]):
        return NotImplemented

    @abstractmethod
    def add_block(self, block: Block):
        return NotImplemented

    @abstractmethod
    def add_series(self, series: Series):
        return NotImplemented

    @abstractmethod
    def clear_series(self):
        return NotImplemented

    @abstractmethod
    def clear_blocks(self):
        return NotImplemented
