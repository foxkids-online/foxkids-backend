from .repositories.abstract_repository import AbstractRepository
from .repositories.db_repository import DBRepository
from .repositories.fake_repository import FakeRepository
from .repositories.file_repository import FileRepository
from .script_manager import ScriptManager
from .storage import Storage

""" Адаптеры для внешних подключений """

__all__ = [
    "AbstractRepository",
    "DBRepository",
    "FakeRepository",
    "FileRepository",
    "ScriptManager",
    "Storage",
]
