from fastapi import FastAPI, HTTPException
import firebase_admin
from firebase_admin import credentials, firestore
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import json

app = FastAPI()

load_dotenv()

# Initialize Firebase Admin SDK
firebase_json = os.getenv("FIREBASE_CREDENTIALS")
cred = credentials.Certificate(json.loads(firebase_json))
firebase_admin.initialize_app(cred)
db = firestore.client()

# Standard model for a game
class Game(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class GameInDB(Game):
    id: str

class ResponseModel(BaseModel):
    detail: str

# Model for updating a game (only the fields that can be updated)
class GameUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

    # Method to get the update data, excluding None values
    def get_update_data(self):
        return {field_name: field_value for field_name, field_value in self.model_dump().items() if field_value is not None}

# Create a new game
@app.post("/games/", response_model=GameInDB)
async def create_game(game: Game):
    doc_ref = db.collection('games').document()
    doc_ref.set(game.model_dump())
    return {"id": doc_ref.id, **game.model_dump()}

#Get all games
@app.get("/games/", response_model=list[GameInDB])
async def get_games():
    docs = db.collection('games').get()
    return [{"id": doc.id, **doc.to_dict()} for doc in docs]

# Get a game by ID
@app.get("/games/{game_id}", response_model=GameInDB)
async def get_game(game_id: str):
    doc_ref = db.collection('games').document(game_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Game not found")
    return {"id": doc.id, **doc.to_dict()}

# Update a game by ID
@app.put("/games/{game_id}", response_model=GameInDB)
async def update_game(game_id: str, game_update: GameUpdate):
    # Get the update data from the request body
    update_data = game_update.get_update_data()
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    doc_ref = db.collection('games').document(game_id)
    doc = doc_ref.get()
    
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Game not found")
        
    # Actualizar solo los campos proporcionados
    doc_ref.update(update_data)
    
    # Obtener el documento actualizado
    updated_doc = doc_ref.get()
    return {"id": updated_doc.id, **updated_doc.to_dict()}

# Delete a game by ID
@app.delete("/games/{game_id}", response_model=ResponseModel)
async def delete_game(game_id: str):
    doc_ref = db.collection('games').document(game_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Game not found")
    doc_ref.delete()
    return {"detail": "Game deleted successfully"}