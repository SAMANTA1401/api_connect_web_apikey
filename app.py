from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# uvicorn app:app --reload
@app.get("/")
async def read_root():
    return {"message": "Congrats! This is your first API message"}

@app.get("/get-message") # set postman parameter  
async def hello(name: str):
    return {"message": "Congrats!"+name+" This is your first API message"}

static_string = "Initial Text"
@app.post("/add")  # set post manparameter  
async def add_text(text: str):
    global static_string
    static_string += text
    return {"message": "Text added successfully","current_string": static_string}

@app.put("/update/{new_text}")
async def update_text(new_text: str):
    global static_string
    static_string = new_text
    return {"message": "Text updated successfully","current_string": static_string}

@app.delete("/delete")
async def delete_text():
    global static_string
    static_string = " "
    return {"message": "Text deleted successfully","current_string": static_string}
