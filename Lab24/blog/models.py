from django.db import models
from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    description: str

@dataclass
class Media:
    title: str
    description: str
    rating: int
    studio_name: str