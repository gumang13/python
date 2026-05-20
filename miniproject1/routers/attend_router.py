from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.attend_schema import (attendCreate)
from service.attend_service import (create_attend_service,get_attend_list)

router = APIRouter()


@router.post("/attend")
def create_attend(attend:attendCreate , db:Session=Depends(get_db)):
    create_attend_service(attend,db)


@router.get("/attend")
def get_attend(db:Session=Depends(get_db)):
    return get_attend_list(db)