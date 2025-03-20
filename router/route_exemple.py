from fastapi import APIRouter

router_exemplo = APIRouter(prefix='/teste',tags=['Teste'])

@router_exemplo.get('/teste inicial')
def teste(str_inical:str|int ) -> str:
  return str_inical