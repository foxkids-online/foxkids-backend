from pydantic import BaseModel, Field


class BlockDTO(BaseModel):

    name: str = Field(description="Название блока")
    weekday: int = Field(
        ge=0, le=6, description="Номер дня недели, 0- пн, 6 - вскр"
    )
    index_in_weekday: int = Field(
        ge=0, le=100, description="Номер блока внутри программы на день"
    )
    series_list: list[str]
