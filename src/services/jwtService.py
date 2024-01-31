from src.schemas.tokenSchema import TokenData
from datetime import datetime, timedelta
from jose import JWTError, jwt
from src.schemas.tokenSchema import TokenData

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class jwtActuator:
    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def verify_token(self, token: str, credentials_exception):
        try:
            payload: dict[str, str] = jwt.decode(
                token, SECRET_KEY, algorithms=[ALGORITHM]
            )
            if (
                payload.get("username", None) != None
                and payload.get("role", None) != None
            ):
                username: str = payload["username"]
                role: str = payload["role"]
            else:
                raise credentials_exception
            if username is None:
                raise credentials_exception
            return TokenData(username=username, role=role)

        except JWTError:
            raise credentials_exception
