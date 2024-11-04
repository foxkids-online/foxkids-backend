from sqlalchemy.orm import Session

from foxkids.domain import Block, Series

from .abstract_repository import AbstractRepository


class DBRepository(AbstractRepository):

    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def get_blocks(self, weekday: int | None = None) -> list[Block]:
        query = self.session.query(Block)
        if weekday is not None:
            query = query.filter_by(weekday=weekday)
        return list(query)

    def get_series(self, name: str | None = None) -> list[Series]:
        query = self.session.query(Series)
        if name is not None:
            query = query.filter_by(name=name)
        return list(query)

    def update_series_list(self, series_list: list[Series]):
        for series in series_list:
            self.session.query(Series).update(**series.to_dict())
        self.session.commit()

    def update_blocks(self, blocks: list[Block]):
        for block in blocks:
            self.session.query(Block).update(**block.to_dict())
        self.session.commit()

    def add_block(self, block: Block):
        self.session.add(block)
        self.session.commit()

    def add_series(self, series: Series):
        self.session.add(series)
        self.session.commit()

    def clear_blocks(self):
        pass

    def clear_series(self):
        pass
