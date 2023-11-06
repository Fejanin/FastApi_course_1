from fastapi import FastAPI, Path
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
from models import User


# запуск приложения в консоли
# uvicorn main:app --reload

user = User(username='John Doe', age=18)


class User1(BaseModel):
    username: str
    message: str

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse('templates/index.html')

@app.get("/about")
async def about():
    return {'message': 'О сайте.'}

@app.get("/faq")
async  def faq():
    return HTMLResponse('<h1>FAQ</h1>')


@app.get("/download")
async def download_file():
    # взяли файл test_file.txt, переименовал его в testpage.html и произвели его загрузку
    return FileResponse('download_files/test_file.txt', filename='testpage.html', media_type='application/octet-stream')

@app.get('/user/{id}')
def user_id(id: int ): # будет принимать только число
    return {'user_id': id}

@app.get('/users/{name}/{age}')
def user_name_age(name, age):
    return {'user_name': name, 'user_age': age}


@app.get('/us/{name}-{age}')
def user_name_age_(name, age):
    return {'user_name': name, 'user_age': age}

@app.get('/go_to/{name}')
def user_name(name: str = Path(min_length=3, max_length=20)): # строка с длииной от 3 до 20
    return {'user_name__': name}

@app.get('/phones/{phone}')
def phones(phone: str = Path(regex="^\d{11}$")):
    return {'user_phone': phone}






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