from foxkids.domain import Series
from foxkids.dto import SeriesDTO


def test_dto_series_mapping1():
    series = Series(name="spider_man", current=1, count=10)
    series_dto = SeriesDTO(**series.to_dict())
    series2 = Series(**series_dto.model_dump())
    assert series == series2


def test_dto_series_mapping2():
    series = Series(name="spider_man", current=1, count=10)
    series_dto = SeriesDTO.model_validate(series.to_dict())
    series2 = Series(**series_dto.model_dump())
    assert series == series2
