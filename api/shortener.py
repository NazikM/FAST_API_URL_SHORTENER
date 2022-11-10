import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
import validators
from fastapi.responses import RedirectResponse

from database.crud import get_or_create_url, get_url_with_id, update_click_count
from database.database import get_db
from database.schemas import UrlTarget

router = fastapi.APIRouter()


def get_full_url(url_id: str, db: Session = Depends(get_db)):
    result = get_url_with_id(db, url_id)
    if not result:
        raise HTTPException(status_code=404, detail="Url not found!")
    update_click_count(db, result)
    return result.full


@router.get('/{url_id}')
async def redirect_to(url_id: str, db: Session = Depends(get_db)):
    return RedirectResponse(get_full_url(url_id, db))


@router.get("/api/v1/{url_id}")
async def read_one(url_id: str, db: Session = Depends(get_db)):
    return get_full_url(url_id, db)


@router.post("/api/v1/", status_code=201)
async def create_one(full_url: UrlTarget, db: Session = Depends(get_db)):
    if not validators.url(full_url.full):
        raise HTTPException(status_code=400, detail="URL is not in correct format")

    url_model = get_or_create_url(db, full_url)
    return url_model
