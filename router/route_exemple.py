from fastapi import APIRouter

router = APIRouter(prefix='/teste')

@router.get('/alo',tags=['Apenas teste'])
def teste(alo:str):
  return 'aaaa'