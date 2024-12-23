import time
from datetime import datetime

import schedule

from foxkids.adapters import AbstractRepository, ScriptManager, Storage
from foxkids.domain.features import get_series_list_by_day, increment_series
from foxkids.settings import settings
from foxkids.utils.bash_formatter import create_curl, create_program_row


class StreamService:
    """
    1. собрать скрипт
    2. прибавить всем сериям за день
    4. запустить скрипт
    """

    def __init__(
        self,
        repository: AbstractRepository,
        storage: Storage,
        script_manager: ScriptManager,
    ):
        """
        repository репозиторий для программы передач
        storage работает с файловой системой для видео
        script_manager обработчик скрипта
        """
        self.repository = repository
        self.storage = storage
        self.count_commertials = settings.COUNT_COMMERTIALS
        self.script_manager = script_manager

    def __create_stream(self) -> list[str]:

        stream = []
        today = datetime.now().weekday()
        blocks = self.repository.get_blocks(today)

        for block in blocks:
            # получить промо блока
            block_promo = self.storage.get_block_promo(block.name)
            bash_block_promo = create_program_row(block_promo)
            stream.append(bash_block_promo)

            # получить две рандомных рекламы
            commertials = self.__get_random_commertials()
            commertials = [create_program_row(i) for i in commertials]
            stream.extend(commertials)

            for index, series in enumerate(block.series_list):

                if index == len(block.series_list) - 1:
                    curl_row = create_curl(series.name, "")
                    stream.append(curl_row)
                else:
                    curl_row = create_curl(
                        series.name, block.series_list[index + 1].name
                    )
                    stream.append(curl_row)

                # получить промо сериала
                series_promo = self.storage.get_series_promo(series.name)
                series_promo = create_program_row(series_promo)
                stream.append(series_promo)

                # получить рекламу
                commertials = self.__get_random_commertials()
                commertials = [create_program_row(i) for i in commertials]
                stream.extend(commertials)

                # получить серию
                series_path = self.storage.get_series(
                    series.name, series.current
                )

                series_row = create_program_row(series_path)
                stream.append(series_row)
        return stream

    def __get_random_commertials(self) -> list[str]:
        commertials = []
        counter = self.count_commertials
        while counter > 0:
            commertial = self.storage.get_random_commertials()
            if commertial is not None:
                commertials.append(commertial)
            counter -= 1
        return commertials

    def start(self, increase_series: bool = True):
        """
        запускает стрим с пересчетом серий
        если increase_series == True, то пересчитает серии
        """
        if increase_series:
            today = datetime.now().weekday()
            blocks = self.repository.get_blocks(today)  # пересчет серий
            series_in_day = get_series_list_by_day(blocks)
            updating_series = increment_series(series_in_day)
            self.repository.update_series_list(updating_series)
        lines = self.__create_stream()
        self.script_manager.write_stream_script(lines)  # перезапись скрипта

    def start_stream_scheduled(self):
        schedule.every().day.at(settings.TIME_START).do(self.start)

        while True:
            schedule.run_pending()
            time.sleep(1)
