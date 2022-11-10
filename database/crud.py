from sqlalchemy import desc
from sqlalchemy.orm import Session

from services.url_generator import get_unique_url_id
from database import models, schemas


def get_url_with_id(db: Session, url_id: str) -> models.Urls:
    """
    Used for getting url in url generators.
    :param db: Db Session
    :param url_id: short url
    :return: Query
    """
    result = db.query(models.Urls)\
        .filter(models.Urls.short == url_id)\
        .first()
    return result


def get_url_with_full(db: Session, full_url: str) -> models.Urls:
    result = db.query(models.Urls)\
        .filter(models.Urls.full == full_url)\
        .first()
    return result


def create_url(db: Session, url: schemas.UrlTarget):
    # Generating unique identifier
    short_id = get_unique_url_id(db)

    # Adding to db
    url_model = models.Urls(full=url.full, short=short_id)
    db.add(url_model)
    db.commit()
    db.refresh(url_model)
    return url_model


def get_or_create_url(db: Session, url: schemas.UrlTarget):
    url_model = get_url_with_full(db, url.full)

    # Checking if long_url not in db
    if url_model:
        return url_model

    # Write to db
    return create_url(db, url)


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
