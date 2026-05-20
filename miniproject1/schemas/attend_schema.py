from pydantic import BaseModel

class attendCreate(BaseModel):
    student_id : int
    attend : int
    late : int
    absent : int
    early_leave : int

class attendResponse(BaseModel):
    id : int
    student_id : int
    student_name : str
    attend : int
    late : int
    absent : int
    early_leave : int
    total_count : int
    attendance_rate : float

    class Config:
        from_attributes=True
