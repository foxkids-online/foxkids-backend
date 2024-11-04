import os
import time
from datetime import datetime
from multiprocessing import Process

import schedule

from foxkids.adapters import AbstractRepository, ScriptManager, Storage
from foxkids.domain.features import get_series_list_by_day, increment_series
from foxkids.settings import settings
from foxkids.utils.bash_formatter import create_program_row


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
        self.stream_process = Process(target=self.start_stream_script)
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

            for series in block.series_list:

                # получить промо сериала
                series_promo = self.storage.get_series_promo(series.name)
                series_promo = create_program_row(series_promo)
                stream.append(series_promo)

                # получить рекламу
                commertials = self.__get_random_commertials()
                commertials = [create_program_row(i) for i in commertials]
                stream.extend(commertials)

                # включить серию
                series_path = self.storage.get_series(
                    series.name, series.current
                )
                series_row = create_program_row(series_path)
                stream.append(series_row)
        return stream

    def __increase_series(self):
        today = datetime.now().weekday()
        blocks = self.repository.get_blocks(today)
        series = get_series_list_by_day(blocks)
        increment_series(series)

    def __get_random_commertials(self) -> list[str]:
        commertials = []
        counter = self.count_commertials
        while counter > 0:
            commertial = self.storage.get_random_commertials()
            if commertial is not None:
                commertials.append(commertial)
            counter -= 1
        return commertials

    def get_stream_script(self):
        return self.script_manager.get_stream_script()

    def write_stream_script(self, lines: list[str]):
        self.script_manager.write_stream_script(lines)

    def start_manually(self):
        """
        запускает стрим без пересчета серий
        """
        self.stream_process.start()

    def start(self):
        """
        запускает стрим с пересчетом серий
        """
        series = self.__create_stream()
        self.__increase_series()
        self.script_manager.write_stream_script(series)
        self.stream_process.start()

    def stop(self):
        """
        останавливает процесс стриминга
        """
        self.stream_process.kill()

    def start_stream_script(self):
        os.system(f"sh {self.script_manager.file_stream}")

    def start_stream_scheduled(self):

        schedule.every().day.at(settings.TIME_START).do(self.start)

        while True:
            schedule.run_pending()
            time.sleep(1)
