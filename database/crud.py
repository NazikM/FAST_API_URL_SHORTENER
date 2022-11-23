from sqlalchemy import desc
from sqlalchemy.orm import Session

from database import models, schemas


def get_url_with_id(db: Session, short_url: str) -> models.Urls:
    result = db.query(models.Urls)\
        .filter(models.Urls.id == int(short_url, 36))\
        .first()
    return result


def get_url_with_full(db: Session, full_url: str) -> models.Urls:
    result = db.query(models.Urls)\
        .filter(models.Urls.url == full_url)\
        .first()
    return result


def create_short_id(db: Session, url: schemas.UrlTarget):
    url_model = models.Urls(url=url.full)
    db.add(url_model)
    db.commit()
    db.refresh(url_model)
    return url_model


def get_or_create_short_id(db: Session, url: schemas.UrlTarget):
    url_model = get_url_with_full(db, url.full)

    # Checking if long_url not in db
    if not url_model:
        url_model = create_short_id(db, url)
    return url_model


def update_click_count(db: Session, model: models.Urls):
    model.click_count += 1
    db.commit()
    db.refresh(model)


def get_top_urls_by_clicks(db: Session, urls_count: int):
    result = db.query(models.Urls)\
        .order_by(desc(models.Urls.click_count)) \
        .limit(urls_count) \
        .all()
    return result
