from fastapi import APIRouter

from foxkids.adapters import FileRepository
from foxkids.dto import CurrentSeriesDTO, CurrentSeriesNameDTO
from foxkids.service_layer import SeriesManagerService

repository = FileRepository()
series_manager = SeriesManagerService(repository)

current_promo_router = APIRouter(prefix="/current_promo", tags=["Промо серий"])


@current_promo_router.get(
    "/",
    summary="Получить текущие серии",
    description="Получение текущих серий",
)
async def get_current_series() -> CurrentSeriesDTO:
    return series_manager.get_current_series()


@current_promo_router.post(
    "/", summary="Обновление блока", description="Обновление блока целиком"
)
async def set_current_series(series: CurrentSeriesNameDTO):
    current_series_list = series_manager.get_series(series.current_series)
    next_series_list = series_manager.get_series(series.next_series)
    current_series = (
        current_series_list[0] if len(current_series_list) > 0 else None
    )
    next_series = next_series_list[0] if len(next_series_list) > 0 else None
    series_dto = CurrentSeriesDTO(
        current_series=current_series, next_series=next_series
    )
    series_manager.set_current_series(series_dto)
    return {"message": "Текущие серии установлены"}
