from fastapi import APIRouter
from controllers.todo_controller import router as todos_router

##Only for ML example 4
from controllers.ML_controller import router as ML_router


router = APIRouter()

# Include the router for each endpoint group
router.include_router(todos_router)
router.include_router(ML_router)

