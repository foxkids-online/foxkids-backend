from fastapi import APIRouter, File, UploadFile
from fastapi.responses import PlainTextResponse

from foxkids.adapters import FileRepository, ScriptManager, Storage

repository = FileRepository()
storage = Storage()
script_manager = ScriptManager()


stream_manager_router = APIRouter(
    prefix="/stream_script", tags=["Скрипт запуска"]
)


@stream_manager_router.get(
    "/",
    summary="Получить sh скрипт",
    description="Получает текущий sh скрипт трансляции",
    response_class=PlainTextResponse,
)
async def get_stream_script():
    return script_manager.get_stream_script()


# @stream_manager_router.post(
#     "/",
#     summary="Записать sh скрипт",
#     description="Записывает скрипт трансляции из файла",
# )
def upload(file: UploadFile = File(...)):
    contents = file.file.readlines()
    script_manager.write_stream_script(
        [i.decode("utf-8").replace("\r", "") for i in contents]
    )
    return {"message": "Успешно загружен файл"}
