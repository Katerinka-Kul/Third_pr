from pydantic import BaseModel, Field
from typing import List

class Todo(BaseModel):
    id: int = Field(..., example=1)
    item: str = Field(..., example="Example schema!")
class TodoItem(BaseModel):
    item: str
    class Config:
        schema_extra = {
            "example": {
            "item": "Read the next chapter of the book"
            }
        }
class TodoItems(BaseModel):
    todos: List[TodoItem]
    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }