import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database.crud import get_top_urls_by_clicks
from database.database import get_db

router = fastapi.APIRouter()


@router.get('/api/v1/statistics/top_urls/{urls_count}')
async def top_urls(urls_count: int = 10, db: Session = Depends(get_db)):
    if urls_count < 1:
        raise HTTPException(status_code=400, detail="urls_count should be greater than 0")
    result = get_top_urls_by_clicks(db, urls_count)
    return result


