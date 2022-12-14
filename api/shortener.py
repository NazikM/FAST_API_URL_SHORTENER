import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
import validators
from fastapi.responses import RedirectResponse

from app.database.crud import get_or_create_short_id, get_url_with_id, update_click_count
from app.database.database import get_db
from app.database.schemas import UrlTarget

from app.database.schemas import Url

router = fastapi.APIRouter()

# MISSING = object()


def get_full_url(short_url: str, db: Session = Depends(get_db)):
    result = get_url_with_id(db, short_url)
    if not result:
        # if default is not MISSING:
        #     return default
        raise HTTPException(status_code=404, detail="Url not found!")
    update_click_count(db, result)
    return result.url


@router.get('/goto/{url_id}')
async def redirect_to(url_id: str, db: Session = Depends(get_db)):
    return RedirectResponse(get_full_url(url_id, db))


@router.get("/api/v1/{url_id}")
async def read_one(url_id: str, db: Session = Depends(get_db)):
    return get_full_url(url_id, db)


@router.post("/api/v1/", status_code=201)
async def create_one(full_url: UrlTarget, db: Session = Depends(get_db)):
    if not validators.url(full_url.full):
        raise HTTPException(status_code=400, detail="URL is not in correct format")

    url_model = get_or_create_short_id(db, full_url)
    return Url(url_model=url_model)
