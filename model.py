from pydantic import BaseModel, Field
from typing import List, Optional
from fastapi import Form

class Todo(BaseModel):
    id: Optional[int] = None  # Сделать опциональным
    item: str = Field(..., examples=["Example schema!"])
    
    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)  # id будет автоматически None

class TodoItem(BaseModel):
    item: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "item": "Read the next chapter of the book"
                }
            ]
        }
    }

class TodoItems(BaseModel):
    todos: List[TodoItem]
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "todos": [
                        {
                            "item": "Example schema 1!"
                        },
                        {
                            "item": "Example schema 2!"
                        }
                    ]
                }
            ]
        }
    }