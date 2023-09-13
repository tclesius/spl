import os
import shutil
import uuid
from typing import BinaryIO


def save_file(file: BinaryIO) -> str:
    upload_dir = 'file/uploads'
    os.makedirs(upload_dir, exist_ok=True)
    filename = str(uuid.uuid4())
    file_path = os.path.join(upload_dir, filename)
    with open(file_path, "wb+") as buffer:
        shutil.copyfileobj(file, buffer)
    return filename
