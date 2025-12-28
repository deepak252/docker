from pydantic import BaseModel, Field
from typing import List


class Country(BaseModel):
    name: str
    iso_code: str

class CountryListPayload(BaseModel):
    countries: List[Country]