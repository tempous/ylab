from fastapi import APIRouter, Depends
from src.services.user import (UserService,get_current_user,get_token,get_user_service)
from src.api.v1.schemas.users import UserModel
from src.api.v1.schemas.auth import Login, Signup, Tokens
from src.models.user import User

router = APIRouter()


@router.post(path="/signup",response_model=UserModel,summary="Пройти регистрацию",tags=["auth"],)
def signup(signup_data: Signup,user_service: UserService = Depends(get_user_service)) -> UserModel:
    user = user_service.create_user(user=signup_data)
    return user


@router.post(path="/login",response_model=Tokens,summary="Войти в аккаунт",tags=["auth"],)
def login(login_data: Login,user_service: UserService = Depends(get_user_service)) -> UserModel:
    tokens = user_service.login_user(login=login_data)
    return tokens


@router.post(path="/refresh",response_model=Tokens,summary="Обновить токен",tags=["auth"],)
def refresh(token: str = Depends(get_token),user_service: UserService = Depends(get_user_service),):
    tokens = user_service.refresh_token(token)
    return tokens


@router.post( path="/logout",summary="Выйти из аккаунта",tags=["auth"],)
def logout(access_token: str = Depends(get_token),user: User = Depends(get_current_user),user_service: UserService = Depends(get_user_service),):
    user_service.logout(user, access_token)
    return {'msg': 'You have been logged out.'}


@router.post(path="/logout_all",summary="Выйти из аккаунта со всех устройств",tags=["auth"],)
def logout_all(user: User = Depends(get_current_user),user_service: UserService = Depends(get_user_service),):
    user_service.logout_all(user)
    return {'msg': 'You have been logged out from all devices'}