from foxkids.adapters import FileRepository
from foxkids.domain import Block, Series


def test_add_series():
    indiana = Series(name="indiana", current=0, count=0)
    repository = FileRepository()
    repository.clear_series()
    repository.clear_blocks()
    repository.add_series(indiana)
    assert indiana in repository.get_series()
    repository.clear_series()
    repository.clear_blocks()


def test_update_series_list():
    spider_man = Series(name="spider-man", current=2, count=10)
    repository = FileRepository()
    repository.clear_series()
    repository.clear_blocks()
    repository.add_series(spider_man)
    spider_man2 = Series(name="spider-man", current=0, count=0)
    repository.update_series_list([spider_man2])
    series_list = repository.get_series()
    for series in series_list:
        if spider_man2 == series:
            repository.clear_series()
            repository.clear_blocks()
            assert series.current == 0 and series.count == 0
            break


def test_get_block():
    repository = FileRepository()
    repository.clear_series()
    repository.clear_blocks()
    indiana = Series(name="indiana", current=1, count=10)
    repository.add_series(indiana)
    block = Block(
        weekday=0,
        name="foxkids",
        index_in_weekday=0,
        series_list=[indiana, indiana],
    )
    repository.add_block(block)
    arr = repository.get_blocks()
    repository.clear_series()
    repository.clear_blocks()
    assert arr[0] == block
