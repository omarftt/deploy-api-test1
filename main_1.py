from fastapi import FastAPI
from routes import router

app = FastAPI()

# Include the router for the API endpoints
app.include_router(router)
