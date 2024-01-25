import uvicorn
from fastapi import FastAPI
from databasy import engine, Base
from routers import user as user_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_router.router, prefix='/user')

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True, workers=3)
