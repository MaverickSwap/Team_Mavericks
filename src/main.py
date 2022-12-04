from fastapi import FastAPI, status, Response
import json
from src.models.note import Note
from copy import deepcopy


app = FastAPI()
notes = []

# 
# GET all notes route
# 
@app.get("/notes")
def get_notes():
    notes = load_db_from_file()

    return {
        "notes" : notes
    }

# 
# POST note route
# 
@app.post("/notes")
def post_note(note: Note):
    notes = load_db_from_file()
    notes.append(note.dict())
    write_to_db(notes)    
    return {
            "note" : note
        }


# 
# DELETE note route
# 
@app.delete("/notes")
def delete_note(note_id: int, response: Response):
    notes = load_db_from_file()
    note_id_to_delete = None
    for idx, note in enumerate(notes):

        if note_id == note["id"]:
            note_id_to_delete = idx

    if note_id_to_delete is not None:
        print('note id to delete is ', note_id_to_delete)
        notes.pop(note_id_to_delete)
        write_to_db(notes)
        return {
            "msg" : f'Note with id : {note_id} is deleted '
        }
    else:
        response.status_code = 404
        return {
            "msg" : f'Note with id : {note_id} is not found '
        }


@app.patch("/notes")
def update_note(note_id: int, note : Note, response: Response):
    notes = load_db_from_file()
    note_dict = note.dict()

    for idx, note in enumerate(notes):
        if note_id == note["id"]:
            note_dict["id"] = note_id
            notes[idx] = note_dict
            write_to_db(notes)
            return {
                 "msg" : f'Note with id : {note_id} is successfully updated '
            }
        else:
            response.status_code = 404
            return {
                "msg" : f'Note with id : {note_id} is not found '
            }



def load_db_from_file():
    db = {}
    with open("src/db/notes.json", "r") as db_data:
        db = json.load(db_data)        
    notes = db["notes"]
    return notes



# Write the changes from in_memory db to file to persist the records and their updates
def write_to_db(notes):

    data = {
        "notes": notes,
    }
    with open("src/db/notes.json", "w") as db_data:
        json.dump(data, db_data)