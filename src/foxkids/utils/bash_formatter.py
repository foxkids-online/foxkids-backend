from foxkids.settings import settings


def create_program_row(path: str | None) -> str:
    """
    создает строку скрипта
    """
    if path is None:
        return ""
    url = settings.STREAM_URL
    return settings.PLAY_SCRIPT.format(path, url) + "\n"


def create_curl(now: str, after: str) -> str:
    """
    отправляет запрос
    """
    return str(settings.CURL_SCRIPT.format(now, after) + "\n")
