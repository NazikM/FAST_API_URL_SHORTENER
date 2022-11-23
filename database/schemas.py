from typing import List

from pydantic import BaseModel

from app.services.url_generator import generate_unique_url_id


class UrlTarget(BaseModel):
    full: str


class Url(UrlTarget):
    id: int
    short: str
    click_count: int

    def __init__(self, url_model):
        super().__init__(
            id=url_model.id,
            full=url_model.url,
            click_count=url_model.click_count,
            short=generate_unique_url_id(url_id=url_model.id))

    class Config:
        orm_mode = True
