# https://www.youtube.com/watch?v=0sOvCWFmrtA&t=19950s
# Youtube Video: 12:05:00
# 12:03 CRUTIAL how to update all changes to github and Heroku
# source venv/bin/activate
# `uvicorn app.main:app --reload`
# Last step is that we added environment variables

from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router) # When User request goes down these lines, I want you to include our post.router
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hi there!!"}


