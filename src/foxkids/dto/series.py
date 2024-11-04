from pydantic import BaseModel, Field


class SeriesDTO(BaseModel):

    name: str = Field(description="Название сериала")
    count: int = Field(ge=0, le=1000, description="Кол-во серий в сериале")
    current: int = Field(ge=0, le=1000, description="Текущая серия")
    year: int | None = Field(ge=1900, le=2024, description="Год выпуска")
    genre: str = Field(description="Жанр")
    name_rus: str = Field(description="Название сериала на русском")
    description: str = Field(description="Описание")


class CurrentSeriesDTO(BaseModel):

    current_series: SeriesDTO | None
    next_series: SeriesDTO | None


class CurrentSeriesNameDTO(BaseModel):

    current_series: str = Field(description="Название сериала текущего")
    next_series: str = Field(description="Название сериала следующего")
