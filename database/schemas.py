from pydantic import BaseModel


class UrlTarget(BaseModel):
    full: str


class Url(UrlTarget):
    short: str
    click_count: int

    class Config:
        orm_mode = True

