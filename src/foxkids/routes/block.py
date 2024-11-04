from fastapi import APIRouter

from foxkids.adapters import FileRepository
from foxkids.dto import BlockDTO
from foxkids.service_layer import SeriesManagerService

repository = FileRepository()
series_manager = SeriesManagerService(repository)

block_router = APIRouter(prefix="/block", tags=["Блоки"])


@block_router.get(
    "/", summary="Получение блоков", description="Получение списка блоков"
)
async def get_blocks(weekday: int | None) -> list[BlockDTO]:
    return series_manager.get_blocks(weekday)


@block_router.post(
    "/",
    summary="Добавление блока",
    description="Добавление блока в программу передач",
)
async def add_block(block: BlockDTO):
    series_manager.add_block(block)
    return {"message": "Блок добавлен"}


@block_router.put(
    "/", summary="Изменение блока", description="Изменение блока"
)
async def update_blocks(blocks: list[BlockDTO]):
    series_manager.update_blocks(blocks)
    return {"message": "Блоки обновлены"}
