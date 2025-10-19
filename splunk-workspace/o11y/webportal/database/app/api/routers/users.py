from app.api.dependencies.core import DBSessionDep
from app.crud.user import *
from app.schemas.user import User, Users
from app.models.user import User as UserDBModel
from fastapi import APIRouter, status

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=Users,
)
async def _list_users(
    db_session: DBSessionDep,
):
    """
    List all users details
    """
    users = await list_users(db_session)
    return users


@router.get(
    "/{user_id}",
    response_model=User,
)
async def _get_user(
    user_id: int,
    db_session: DBSessionDep,
):
    """
    Get any user details
    """
    user = await get_user(db_session, user_id)
    return user


@router.delete(
    "/{user_id}",
    response_model=User,
)
async def _delete_user(
    user_id: int,
    db_session: DBSessionDep,
):
    """
    Delete any user
    """
    user = await delete_user(db_session, user_id)
    return user


@router.post(
    "/",
    response_model=User,
)
async def _add_user(
    user: User,
    db_session: DBSessionDep,
):
    """
    Add any user
    """
    user_add = UserDBModel(
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        is_superuser=user.is_superuser,
    )
    user_added = await add_user(db_session, user_add)
    return user_added


@router.patch(
    "/",
    response_model=User,
)
async def _edit_user(
    user: User,
    db_session: DBSessionDep,
):
    """
    Edit any user
    """
    user_edit = UserDBModel(
        id=user.id,
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        is_superuser=user.is_superuser,
    )
    user_edited = await edit_user(db_session, user_edit)
    return user_edited
