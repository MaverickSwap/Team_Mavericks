from pydantic import BaseModel
from datetime import datetime
import random

class Note(BaseModel):
    id: int = random.randint(0,9999999) 
    title: str
    description: str
    date: str = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    priority: int = 1