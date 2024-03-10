from fastapi import APIRouter, Form
import base64
import uuid
from pydantic import BaseModel

router = APIRouter(
    prefix="",
    tags=["API"]
)



@router.post("/upload_doc")
async def upload_doc(filename: str = Form(...), filedata: str = Form(...)):
    image_as_bytes = str.encode(filedata)  # convert string to bytes
    img_recovered = base64.b64decode(image_as_bytes)  # decode base64string

    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    try:
        with open("../documents/" + filename, "wb") as f:
            f.write(img_recovered)
    except Exception:
        return {"message": "There was an error uploading the file"}

    return {"message": f"Successfuly uploaded {filename}"}

