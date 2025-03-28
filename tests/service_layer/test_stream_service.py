from pytest import mark

from foxkids.adapters import (
    FakeRepository,
    FileRepository,
    ScriptManager,
    Storage,
)
from foxkids.domain.features import get_series_list_by_day, increment_series
from foxkids.service_layer import StreamService


@mark.skip(reason="не тестируем запуск трансляции")
def test_start_stream():
    storage = Storage()
    repository = FakeRepository()
    script_manager = ScriptManager()
    service = StreamService(repository, storage, script_manager)
    service.start()


@mark.skip(reason="попытка обновить дни стрима")
def test_increase_series():
    days = [1]
    for day in days:
        print(f"day={day}")
        repository = FileRepository()
        blocks = repository.get_blocks(day)  # пересчет серий
        series_in_day = get_series_list_by_day(blocks)
        updating_series = increment_series(series_in_day)
        repository.update_series_list(updating_series)


@mark.skip(reason="попытка обновить скрипт")
def test_write_script():
    repository = FileRepository()
    storage = Storage()
    manager = ScriptManager()
    service = StreamService(repository, storage, manager)
    lines = service.create_stream()
    manager.write_stream_script(lines)
