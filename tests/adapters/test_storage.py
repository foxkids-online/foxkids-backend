from foxkids.adapters.storage import (
    Storage,
    get_full_path,
    get_random_file_from_folder,
)
from foxkids.settings import settings


def test_get_full_path_none():
    assert get_full_path("online.mp4") == f"{settings.MAIN_FOLDER}/online.mp4"


def test_get_full_path():
    assert get_full_path("luie/1.mp4") == f"{settings.MAIN_FOLDER}/luie/1.mp4"


def test_get_random_file_from_folder():
    assert (
        get_random_file_from_folder("luie", "1.mp4")
        == f"{settings.MAIN_FOLDER}/luie/1.mp4"
    )


def test_storage_get_series():
    assert (
        Storage().get_series("luie", 1) == f"{settings.MAIN_FOLDER}/luie/1.mp4"
    )


def test_get_random_commertials():
    assert (
        Storage().get_random_commertials()
        == f"{settings.MAIN_FOLDER}/{settings.COMMERTIALS_FOLDER}/1.mp4"
    )


def test_get_block_promo():
    assert (
        Storage().get_block_promo("foxkids")
        == f"{settings.MAIN_FOLDER}/{settings.BLOCK_PROMO_FOLDER}/foxkids.mp4"
    )


def test_get_series_promo():
    assert (
        Storage().get_series_promo("luie")
        == f"{settings.MAIN_FOLDER}/{settings.PROMO_FOLDER}/luie.mp4"
    )
