from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from foxkids.routes import (  # stream_manager_router,; stream_handler_router,
    block_router,
    current_promo_router,
    series_router,
)

app = FastAPI(title="Fox Kids Video Server API", version="0.1.2")

app.mount("/static", StaticFiles(directory="html/static"), name="static")

api_router = APIRouter(prefix="/api")
main_router = APIRouter(prefix="", tags=["Страницы сайта"])

api_router.include_router(block_router)
api_router.include_router(current_promo_router)
api_router.include_router(series_router)
# api_router.include_router(stream_handler_router)
# api_router.include_router(stream_manager_router)


@main_router.get(
    "/",
    summary="Основная страница",
    description="Основная страница",
    response_class=HTMLResponse,
)
async def main_page(request: Request):
    templates = Jinja2Templates(directory="html")
    return templates.TemplateResponse("index.html", {"request": request})


@main_router.get(
    "/about_project",
    summary="Страница о проекте",
    description="Страница о проекте",
    response_class=HTMLResponse,
)
async def about_project(request: Request):
    templates = Jinja2Templates(directory="html")
    return templates.TemplateResponse(
        "about_project.html", {"request": request}
    )


@main_router.get(
    "/about_channel",
    summary="Страница о канале",
    description="Страница о канале",
    response_class=HTMLResponse,
)
async def about_channel(request: Request):
    templates = Jinja2Templates(directory="html")
    return templates.TemplateResponse(
        "about_channel.html", {"request": request}
    )


@main_router.get(
    "/series",
    summary="Страница со списком среиалов",
    description="Страница оо списком сериалов",
    response_class=HTMLResponse,
)
async def series(request: Request):
    templates = Jinja2Templates(directory="html")
    return templates.TemplateResponse("series.html", {"request": request})


app.include_router(main_router)
app.include_router(api_router)
