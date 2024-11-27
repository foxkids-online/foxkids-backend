from multiprocessing import Process

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
    p = Process(target=stream_service.start_stream_scheduled)
    p.start()
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)
