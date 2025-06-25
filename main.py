from fastapi import FastAPI
import uvicorn
from router.user_route import route

app=FastAPI(title='Aprendendo API', description='API de exemplo com FastAPI',openapi_url='/api-docs')


app.include_router(route)

if __name__== '__main__':
  uvicorn.run("main:app",host="0.0.0.0",port=8000, reload=True)
