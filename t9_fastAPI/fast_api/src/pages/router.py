from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/upload_file")
def get_upload_file_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})