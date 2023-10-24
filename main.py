from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


class User(BaseModel):
    username: str
    message: str

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse('index.html')

@app.post("/")
async def root(user: User):
    '''тут мы можем с переменной user, которая в себе содержит объект класса User с соответствующими полями (и указанными типами), делать любую логику
        - например, мы можем сохранить информацию в базу данных
        - или передать их в другую функцию
        - или другое'''
    print(f'Мы получили от юзера {user.username} такое сообщение: {user.message}')  # тут мы просто выведем полученные данные на экран в отформатированном варианте
    return user # или можем вернуть обратно полученные данные, как символ того, что данные получили, или другая логика на ваш вкус

# новый роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

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