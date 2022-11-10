import fastapi
from fastapi import Request
from fastapi.templating import Jinja2Templates

from config import BASE_URL

router = fastapi.APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/app/stats/")
async def app_page(request: Request):
    return templates.TemplateResponse("stats.html", {"request": request, "BASE_URL": BASE_URL})
