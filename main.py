from fastapi import FastAPI
import uvicorn
import webbrowser
from router.route_exemple import router_exemplo

app=FastAPI()
# @app.get('/')
# def read_root():
#   return {'message': 'aloooooo'}

app.include_router(router_exemplo)

if __name__== '__main__':
  uvicorn.run("main:app",host="0.0.0.0",port=8000, reload=True)
