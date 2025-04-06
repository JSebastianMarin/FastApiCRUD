from fastapi import FastAPI, HTTPException
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


# Initialize Firebase Admin SDK
cred = credentials.Certificate("./talkus-12d74-firebase-adminsdk-fbsvc-e99b2bf5e4.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class Game(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

@app.post("/games/")
async def create_game(game: Game):
    doc_ref = db.collection('games').document()
    doc_ref.set(game.model_dump())
    return {"id": doc_ref.id, **game.model_dump()}