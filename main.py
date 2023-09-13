from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles

from admin.view import router as admin_router
from auth.view import router as auth_router
from file.view import router as file_router
from invite.view import router as invite_router
from producer.view import router as producer_router
from release.view import router as release_router
from user.view import router as user_router


def custom_generate_unique_id(route: APIRoute):  # for better client generation
    return f"{route.tags[0]}-{route.name}"  # every route must have a tag or throws error


app = FastAPI(generate_unique_id_function=custom_generate_unique_id)

origins = [
    "*",  # TODO: IMPORTANT - change for production or make a development mode
    "127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(user_router)
app.include_router(release_router)
app.include_router(invite_router)
app.include_router(file_router)
app.include_router(producer_router)

app.mount("/static", StaticFiles(directory=Path("file/uploads")), name="static")


@app.get("/", tags=["default"])
async def root():
    return {"message": "Hello World"}
