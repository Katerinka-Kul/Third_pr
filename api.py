from todo import todo_router
from fastapi import FastAPI
from model import Todo 
 
app = FastAPI() 
 
@app.get("/") 
async def welcome() -> dict: return { "message": "Hello World"} 
 
app.include_router(todo_router) 