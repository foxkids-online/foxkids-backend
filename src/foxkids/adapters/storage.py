import os
import random

from foxkids.settings import settings

MAIN_FOLDER_PATH = settings.MAIN_FOLDER


def get_full_path(*kwargs) -> str | None:  # TODO: list(str) либо tuple
    return os.path.join(MAIN_FOLDER_PATH, *kwargs).replace("\\", "/")
    # if os.path.isfile(filename) or os.path.isdir(filename):
    #     return filename
    # else:
    #     return None


def get_random_file_from_folder(
    folder: str, name: str | None = None
) -> str | None:
    folder_path = get_full_path(folder)
    files = os.listdir(folder_path)
    if name is not None:
        files = list(
            filter(lambda x: x.find(name) != -1, os.listdir(folder_path))
        )
    if len(files) == 0:
        return None
    file = random.choice(files)
    return get_full_path(folder, file)


class Storage:

    block_promo_folder = settings.BLOCK_PROMO_FOLDER
    series_promo_folder = settings.PROMO_FOLDER
    commertials_folder = settings.COMMERTIALS_FOLDER

    def get_series(self, series: str, series_number: int) -> str | None:
        seria_name = f"{series_number}.mp4"
        return get_full_path(series, seria_name)

    def get_block_promo(self, block_name: str) -> str | None:
        return get_random_file_from_folder(self.block_promo_folder, block_name)

    def get_series_promo(self, series_name: str) -> str | None:
        return get_random_file_from_folder(
            self.series_promo_folder, series_name
        )

    def get_random_commertials(self) -> str | None:
        return get_random_file_from_folder(self.commertials_folder)
