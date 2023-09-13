from pydantic import BaseModel


class TokenRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    token_type: str = "bearer"
    # expires_at: datetime.datetime


class AccessToken(TokenResponse):
    access_token: str


class RefreshToken(TokenResponse):
    refresh_token: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RegisterPost(BaseModel):
    invite_token: str
    username: str
    password: str
    # file: Optional[UploadFile] = File(...)
