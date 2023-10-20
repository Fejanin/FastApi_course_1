from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse('index.html')

# запуск приложения в консоли
# uvicorn main:app --reload

















############################################
# альтернатива
'''
from fastapi import FastAPI

my_awesome_api = FastAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World"}

# запуск приложения в консоли
# uvicorn main:my_awesome_api --reload
'''