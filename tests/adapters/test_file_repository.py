from foxkids.adapters import FileRepository
from foxkids.domain import Series


def test_add_series():
    indiana = Series(name="indiana", current=0, count=0)
    repository = FileRepository()
    repository.clear_series()
    repository.add_series(indiana)
    assert indiana in repository.get_series()
    repository.clear_series()


def test_update_series_list():
    spider_man = Series(name="spider-man", current=2, count=10)
    repository = FileRepository()
    repository.clear_series()
    repository.add_series(spider_man)
    spider_man2 = Series(name="spider-man", current=0, count=0)
    repository.update_series_list([spider_man2])
    series_list = repository.get_series()
    for series in series_list:
        if spider_man2 == series:
            repository.clear_series()
            assert series.current == 0 and series.count == 0
            break
