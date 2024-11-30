from threading import Thread

import uvicorn

from foxkids.adapters import FileRepository, ScriptManager, Storage
from foxkids.service_layer import StreamService
from foxkids.settings import settings

from .server import app

repository = FileRepository()
storage = Storage()
script_manager = ScriptManager()

stream_service = StreamService(repository, storage, script_manager)

if __name__ == "__main__":
    scheduled_task = Thread(target=stream_service.start_stream_scheduled)
    scheduled_task.start()
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)
