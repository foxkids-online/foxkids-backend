from foxkids.domain.block import Block
from foxkids.domain.features import get_series_list_by_day
from foxkids.domain.series import Series


def create_program() -> list[Block]:
    spider_man = Series(name="spider_man", current=1, count=10)
    luie = Series(name="luie", current=1, count=10)
    indiana = Series(name="indiana", current=1, count=10)
    block1 = Block(
        weekday=0, name="foxkids", index_in_weekday=0, series_list=[]
    )
    block2 = Block(
        weekday=0, name="foxkids", index_in_weekday=1, series_list=[]
    )
    block3 = Block(
        weekday=5, name="foxkids", index_in_weekday=0, series_list=[]
    )
    block1.add(spider_man)
    block1.add(luie)
    block1.add(luie)
    block2.add(spider_man)
    block2.add(spider_man)
    block2.add(luie)
    block2.add(luie)
    block3.add(indiana)
    block3.add(indiana)
    block3.add(indiana)
    return [block1, block2, block3]


def test_get_series_list_by_day():
    program = create_program()
    monday_series = get_series_list_by_day(
        list(filter(lambda x: x.weekday == 0, program))
    )
    saturday_series = get_series_list_by_day(
        list(filter(lambda x: x.weekday == 5, program))
    )
    assert len(monday_series) == 2 and len(saturday_series) == 1
