from fastapi import APIRouter

from foxkids.adapters import FileRepository
from foxkids.dto import SeriesDTO
from foxkids.service_layer import SeriesManagerService

repository = FileRepository()
series_manager = SeriesManagerService(repository)

series_router = APIRouter(prefix="/series", tags=["Сериалы"])


@series_router.get(
    "/",
    summary="Получение списка сериалов",
    description="Получить список всех имеющихся сериалов",
)
async def get_series() -> list[SeriesDTO]:
    return series_manager.get_series()


@series_router.post(
    "/",
    summary="Добавление сериала",
    description="Добавление нового сериала в список",
)
async def add_series(series: SeriesDTO):
    series_manager.add_series(series)
    return {"message": "Сериалы добавлены"}


@series_router.put(
    "/",
    summary="Обновление сериала",
    description="Обновление сериала целиком по имени",
)
async def update_series_list(series: list[SeriesDTO]):
    series_manager.update_series_list(series)
    return {"message": "Список серий обновлен"}
