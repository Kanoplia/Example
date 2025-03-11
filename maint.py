from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
 
#  uvicorn chess.maint:app --reload

app = FastAPI()
 
@app.get("/")
def root():
    return FileResponse("chess\main\exsp.html")

@app.get("/login")
def root():
    return FileResponse("chess\login\login.html")

app.mount("/login", StaticFiles(directory="chess\login"))

app.mount("/", StaticFiles(directory="chess\main", html= True))

@app.post("/postdata")
def postdata(username = Form(), userage=Form()):
    return {"name": username, "age": userage}
