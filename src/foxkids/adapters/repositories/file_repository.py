import json
from dataclasses import dataclass

from foxkids.domain import Block, Series
from foxkids.settings import settings

from .abstract_repository import AbstractRepository


class FileRepository(AbstractRepository):

    def __init__(self):
        self.fw = FileReaderWriter()

    def get_blocks(self, weekday: int | None = None) -> list[Block]:
        blocks = self.fw.get_blocks_from_file()
        if weekday is None:
            return blocks
        return list(filter(lambda x: x.weekday == weekday, blocks))

    def get_series(self, name: str | None = None) -> list[Series]:
        series_list = self.fw.get_series_list_from_file()
        if name is not None:
            for series in series_list:
                if series.name == name:
                    return [series]
            return []
        return series_list

    def update_series_list(self, series_list: list[Series]):
        full_series_list = self.fw.get_series_list_from_file()
        for i, series in enumerate(full_series_list):
            for updated_series in series_list:
                if series == updated_series:
                    full_series_list[i] = updated_series
        self.fw.save(full_series_list, settings.FILE_SERIES)

    def add_block(self, block: Block):  # TODO: сделать чтоб добавлялось листом
        blocks = self.fw.get_blocks_from_file()
        if block in blocks:
            return
        blocks.append(block)
        blocks = sorted(blocks, key=lambda x: (x.weekday, x.index_in_weekday))
        self.fw.save(blocks, settings.FILE_PROGRAM)

    def add_series(
        self, series: Series
    ):  # TODO: тут можно передавать name, curent и count
        series_list = self.fw.get_series_list_from_file()
        if series in series_list:
            return
        series_list.append(series)
        self.fw.save(series_list, settings.FILE_SERIES)

    def update_blocks(self, blocks: list[Block]):
        full_blocks_list = (
            self.fw.get_blocks_from_file()
        )  # TODO: подумать над неймингом
        for i, block in enumerate(full_blocks_list):
            for updated_block in blocks:
                if block == updated_block:
                    full_blocks_list[i] = updated_block
        self.fw.save(full_blocks_list, settings.FILE_SERIES)

    def clear_series(self):
        self.fw.save([], settings.FILE_SERIES)

    def clear_blocks(self):
        self.fw.save([], settings.FILE_PROGRAM)


@dataclass(frozen=True)
class FileReaderWriter:
    """
    Работа с файловой системой для режима работы через файл
    """

    def get_blocks_from_file(self) -> list[Block]:
        """Достает все блоки из файла"""
        program: list[Block] = []
        series_list = self.get_series_list_from_file()
        program_json = self.read_json_file(settings.FILE_PROGRAM)

        for record in program_json:
            record["series_list"] = list(
                filter(lambda x: x.name in record["series_list"], series_list)
            )
            block = Block(**record)
            program.append(block)

        return program

    def get_series_list_from_file(self) -> list[Series]:
        """достать серии из файла"""
        series_list = self.read_json_file(
            settings.FILE_SERIES
        )  # TODO: подумать read_json_file принимает имя файла
        return [
            Series(**i) for i in series_list
        ]  # TODO: Посмотреть в сторону переименования i

    def save(
        self, data: list[Series] | list[Block], filepath: str
    ):  # TODO: overload
        """сохранить в файл все"""
        result = [
            i.to_dict() for i in data
        ]  # TODO: нейминг избегать однобуквенных
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(result, f)

    @staticmethod
    def read_json_file(filename: str) -> list[dict]:
        """прочитать файл"""
        with open(filename, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.decoder.JSONDecodeError:
                return []
