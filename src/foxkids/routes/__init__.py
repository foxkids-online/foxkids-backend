from .block import block_router
from .current_promo import current_promo_router
from .series import series_router
from .stream_handler import stream_handler_router
from .stream_manager import stream_manager_router

__all__ = [
    "block_router",
    "current_promo_router",
    "series_router",
    "stream_handler_router",
    "stream_manager_router",
]
