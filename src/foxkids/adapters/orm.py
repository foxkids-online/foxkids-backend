from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table
from sqlalchemy.orm import mapper, properties, relationship

from foxkids.domain import Block, Series

metadata = MetaData()

series = Table(
    "series",
    metadata,
    Column("name", String(16), primary_key=True),
    Column("count", Integer, nullable=False),
    Column("current", Integer, nullable=False),
)

block = Table(
    "block",
    metadata,
    Column("weekday", Integer, nullable=False, primary_key=True),
    Column("index_in_weekday", Integer, nullable=False, primary_key=True),
    Column("name", String(16)),
)

series_in_block = Table(
    "series_in_block",
    metadata,
    Column("series", ForeignKey("series.id")),
    Column("block", ForeignKey("block.id")),
)


def start_mappers():
    mapper.map_imperatively(
        Series,
        series,
        properties(
            {
                "block": relationship(
                    Series, secondary=series_in_block, backref="series_list"
                )
            }
        ),
    )

    mapper.map_imperatively(Block, block)
