from pytest import mark

from foxkids.adapters import FakeRepository, ScriptManager, Storage
from foxkids.service_layer import StreamService


@mark.skip(reason="не тестируем запуск трансляции")
def test_start_stream():
    storage = Storage()
    repository = FakeRepository()
    script_manager = ScriptManager()
    service = StreamService(repository, storage, script_manager)
    service.start()
