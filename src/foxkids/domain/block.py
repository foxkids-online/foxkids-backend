from dataclasses import dataclass

from foxkids.domain.series import Series


@dataclass
class Block:
    """
    Справочник дней недели

    Attributes
    ----------
    weekday : int
        День недели блока
    index_in_weekday : int
        Порядковый номер блока внутри дня недели
    series : list[Series]
        Список сериалов в блоке
    """

    name: str
    weekday: int
    index_in_weekday: int
    series_list: list[Series]

    def __str__(self):
        main_str = f"\n{self.name}, день недели: {self.weekday}\n"
        for seria in self.series_list:
            main_str += f"{seria}\n"
        return main_str

    def __eq__(self, other):
        if isinstance(other, Block):
            return (
                self.name == other.name
                and self.weekday == other.weekday
                and self.index_in_weekday == other.index_in_weekday
            )
        return NotImplemented

    def add(self, series: Series):
        """Добавление сериала в блок"""
        self.series_list.append(series)

    def to_dict(self) -> dict:
        return {
            **self.__dict__,
            "series_list": [i.to_dict() for i in self.series_list],
        }
