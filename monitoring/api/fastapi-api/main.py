from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/heavy")
def heavy_task():
    total = 0
    for i in range(10**5):
        total += i
    return {"total": total}
