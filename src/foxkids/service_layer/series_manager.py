from foxkids.adapters import AbstractRepository
from foxkids.domain import Block, Series
from foxkids.dto import BlockDTO, CurrentSeriesDTO, SeriesDTO


class SeriesManagerService:

    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository
        self.current_seria: SeriesDTO | None = None
        self.next_series: SeriesDTO | None = None

    def get_blocks(self, weekday: int | None = None) -> list[BlockDTO]:
        blocks = self.repository.get_blocks(weekday=weekday)
        return [BlockDTO.model_validate(i.to_dict()) for i in blocks]

    def get_series(self, name: str | None = None) -> list[SeriesDTO]:
        series = self.repository.get_series(name=name)
        return [SeriesDTO.model_validate(i.to_dict()) for i in series]

    def update_series_list(self, series_list: list[SeriesDTO]):
        new_series_list = [Series(**i.model_dump()) for i in series_list]
        self.repository.update_series_list(new_series_list)

    def update_blocks(self, blocks: list[BlockDTO]):
        new_blocks = [Block(**i.model_dump()) for i in blocks]
        self.repository.update_blocks(new_blocks)

    def add_series(self, series: SeriesDTO):
        new_series = Series(**series.model_dump())
        self.repository.add_series(new_series)

    def add_block(self, block: BlockDTO):
        new_block = Block(**block.model_dump())
        self.repository.add_block(new_block)

    def set_current_series(self, series: CurrentSeriesDTO):
        self.current_seria = series.current_series
        self.next_series = series.next_series

    def get_current_series(self) -> CurrentSeriesDTO:
        return CurrentSeriesDTO(
            current_series=self.current_seria, next_series=self.next_series
        )
