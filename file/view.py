import mimetypes
import os

from fastapi import APIRouter, Depends, UploadFile, HTTPException

from auth.service import auth_admin
from file.service import save_file
from settings import settings

router = APIRouter(prefix="/file", tags=["file"])


@router.post("/upload", tags=["admin"], dependencies=[Depends(auth_admin)])
def upload(file: UploadFile):
    file_size = os.fstat(file.file.fileno()).st_size

    if file_size > settings.MAX_MEDIA_SIZE:
        raise HTTPException(status_code=400, detail="File size too large")

    mime_type, _ = mimetypes.guess_type(file.filename)

    if mime_type not in settings.ALLOWED_MEDIA_TYPES.split(','):
        raise HTTPException(status_code=400, detail="Invalid file type")

    local_filename = save_file(file.file)
    return local_filename
