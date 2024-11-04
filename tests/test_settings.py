from foxkids.settings import settings


def test_dotenv_using():
    assert settings.get("load_dotenv")


def test_having_time_start():
    assert settings.get("TIME_START") is not None


def test_having_translation_url():
    assert settings.get("STREAM_URL") is not None


def test_main_folder():
    assert settings.get("MAIN_FOLDER") is not None


def test_file_program():
    assert settings.get("FILE_PROGRAM") is not None


def test_file_series():
    assert settings.get("FILE_SERIES") is not None


def test_file_stream():
    assert settings.get("FILE_STREAM") is not None


def test_promo_folder():
    assert settings.get("PROMO_FOLDER") is not None


def test_advertising_folder():
    assert settings.get("COMMERTIALS_FOLDER") is not None


def test_block_advertising_sfolder():
    assert settings.get("BLOCK_PROMO_FOLDER") is not None


def test_port():
    assert settings.get("PORT") is not None
