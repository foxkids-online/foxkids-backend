from fastapi import APIRouter

from foxkids.adapters import FileRepository, ScriptManager, Storage
from foxkids.service_layer import StreamService

repository = FileRepository()
storage = Storage()
script_manager = ScriptManager()

stream_service = StreamService(repository, storage, script_manager)

stream_handler_router = APIRouter(prefix="/stream", tags=["Стрим"])


@stream_handler_router.get(
    "/start_manually",
    summary="Запустить скрит sh вручную",
    description="Запустить скрипт трансляции вручную",
)
async def start_manually():
    stream_service.start(increase_series=False)
    return {"message": "Скрипт запущен"}


@stream_handler_router.get(
    "/start",
    summary="Запустить трансляцию",
    description="Запускает трансляцию с пересчетом серий",
)
async def start_stream():
    stream_service.start()
    return {"message": "Стрим запущен"}
