import fastapi
from fastapi import Request
from fastapi.templating import Jinja2Templates

from app.config import BASE_URL

router = fastapi.APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/app/")
async def app_page(request: Request):
    return templates.TemplateResponse("shortener.html", {"request": request, "BASE_URL": BASE_URL})


