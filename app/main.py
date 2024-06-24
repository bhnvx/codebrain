from fastapi import FastAPI

from app.apis.coordinate.v1.coordinates_router import router as coordinates_router


app = FastAPI()

app.include_router(coordinates_router)
