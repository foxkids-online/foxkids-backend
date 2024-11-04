from foxkids.adapters import FakeRepository
from foxkids.domain import Block, Series
from foxkids.dto import CurrentSeriesDTO, CurrentSeriesNameDTO
from foxkids.service_layer import SeriesManagerService


def test_set_current_series():
    # prepearing
    repository = FakeRepository()
    indiana = Series(
        name="indiana", current=1, name_rus="Эйри в Индиане", count=10
    )
    spider_man = Series(
        name="spider_man", name_rus="Человек-паук", current=1, count=50
    )
    block = Block(
        weekday=0,
        name="foxkids",
        index_in_weekday=0,
        series_list=[spider_man, indiana],
    )
    repository.add_block(block)
    repository.add_series(spider_man)
    repository.add_series(indiana)
    service = SeriesManagerService(repository)
    series_names = CurrentSeriesNameDTO(
        current_series="spider_man", next_series="indiana"
    )
    current_series_list = service.get_series(name=series_names.current_series)
    next_series_list = service.get_series(name=series_names.next_series)
    current_series = (
        current_series_list[0] if len(current_series_list) > 0 else None
    )
    next_series = next_series_list[0] if len(next_series_list) > 0 else None

    series = CurrentSeriesDTO(
        current_series=current_series, next_series=next_series
    )
    service.set_current_series(series)

    # action
    series_getted = service.get_current_series()

    # checking
    assert (
        series_getted.current_series.name == series_names.current_series
        and series_getted.next_series.name == series_names.next_series
    )
