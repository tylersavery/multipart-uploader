from pydantic import BaseModel


class StartUploadPayload(BaseModel):
    file_name: str
    content_type: str
    file_size: int


class StartUploadResponse(BaseModel):
    urls: list[str]
    chunk_size: int
    key: str
    upload_id: str
    fields: dict


class CompleteUploadPayload(BaseModel):
    key: str
    upload_id: str
    etags: str


class CompleteUploadResponse(BaseModel):
    url: str
