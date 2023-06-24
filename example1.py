from fastapi import FastAPI, HTTPException, status

app = FastAPI()

todos = []

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(task: str, completed: bool = False):
    print('here')
    new_todo = {"id": len(todos) + 1, "task": task, "completed": completed}
    todos.append(new_todo)
    return {"message": "Todo created successfully"}

@app.put("/todos/{todo_id}", status_code=201)
def update_todo(todo_id: int, task: str, completed: bool):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["task"] = task
            todo["completed"] = completed
            return {"message": "Todo updated successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
