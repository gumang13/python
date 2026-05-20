from fastapi import HTTPException
from models.student import Student
from models.attend import Attend
from schemas.attend_schema import attendResponse

def create_attend_service(attend,db):
  

    student = db.query(Student).filter(Student.id==attend.student_id).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            message = "학생 정보를 찾을 수 없습니다"
        )
    new_attend= Attend(
        student_id = attend.student_id,
        attend = attend.attend,
        late = attend.late,
        absent = attend.absent,
        early_leave = attend.early_leave
    )
    db.add(new_attend)
    db.commit()
    db.refresh(new_attend)

def get_attend_list(db):
    result = []
    attend_list = db.query(Attend,Student).join(Student, Attend.student_id == Student.id).all()
    for attend,std in attend_list:
        total_count = attend.attend+attend.late+attend.absent+attend.early_leave
        attendance_rate = round(attend.attend/total_count, 2)
        result.append(attendResponse(
            id=attend.id,
            student_id=std.id,
            student_name=std.name,
            attend=attend.attend,
            late=attend.late,
            absent=attend.absent,
            early_leave=attend.early_leave,
            total_count=total_count,
            attendance_rate=attendance_rate

        ))
    return result
