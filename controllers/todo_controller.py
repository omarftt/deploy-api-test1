from fastapi import APIRouter, HTTPException, status
from models import Todo

router = APIRouter()

# Example in-memory storage
todos = []

# GET /todos - Retrieve all todos
@router.get("/todos")
def get_todos():
    return todos

# GET /todos/{todo_id} - Retrieve a specific todo
@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# POST /todos - Create a new todo
@router.post("/todos",status_code=status.HTTP_201_CREATED)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

# PUT /todos/{todo_id} - Update a specific todo
@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for index, item in enumerate(todos):
        if item.id == todo_id:
            todos[index] = todo
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# DELETE /todos/{todo_id} - Delete a specific todo
@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, item in enumerate(todos):
        if item.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
