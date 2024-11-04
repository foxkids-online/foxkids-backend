from foxkids.domain import Block, Series


class FakeRepository:

    def __init__(self):
        super().__init__()
        self.series_list: list[Series] = []
        self.blocks: list[Block] = []

    def get_blocks(self, weekday: int | None = None) -> list[Block]:
        blocks = []
        if weekday is not None:
            for block in self.blocks:
                if block.weekday == weekday:
                    blocks.append(block)
            return blocks
        return self.blocks

    def get_series(self, name: str | None = None) -> list[Series]:
        if name is not None:
            for series in self.series_list:
                if series.name == name:
                    return [series]
            return []
        return self.series_list

    def update_series_list(self, series_list: list[Series]):
        for indx, series in enumerate(self.series_list):
            for new_series in series_list:
                if series == new_series:
                    self.series_list[indx] = new_series

    def update_blocks(self, blocks: list[Block]):
        for indx, block in enumerate(self.blocks):
            for new_block in blocks:
                if block == new_block:
                    self.blocks[indx] = new_block

    def add_block(self, block: Block):
        self.blocks.append(block)

    def add_series(self, series: Series):
        return self.series_list.append(series)

    def clear_series(self):
        self.series_list = []

    def clear_block(self):
        self.blocks = []
