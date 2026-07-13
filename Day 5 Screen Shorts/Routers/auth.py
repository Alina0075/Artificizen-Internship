from fastapi import APIRouter, BackgroundTasks
router=APIRouter(
    prefix='/auth',
    tags=['Authentication']
)
@router.post('/')
def login(background_tasks: BackgroundTasks):
    return {'Login Successful'}