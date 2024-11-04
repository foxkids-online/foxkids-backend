from foxkids.domain.block import Block
from foxkids.domain.series import Series


def get_series_list_by_day(day_blocks: list[Block]) -> list[Series]:
    """
    Получает все серии одного дня без повторов из списка блоков
    """
    day_series: list[Series] = []

    for block in day_blocks:
        day_series.extend(block.series_list)

    return list(set(day_series))


def increment_series(series_list: list[Series]) -> list[Series]:
    """
    Увеличивает текущие серии в списке сериалов
    """
    for series in series_list:
        series.increase_current_seria()
    return series_list
