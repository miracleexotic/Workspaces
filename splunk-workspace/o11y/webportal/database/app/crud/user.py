from app.models import User as UserDBModel
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError


class UserNotFound(Exception):
    pass


async def list_users(db_session: AsyncSession):
    try:
        # Select all users
        users = (await db_session.scalars(select(UserDBModel))).all()

        if not users:
            raise UserNotFound()

        return users

    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


async def get_user(db_session: AsyncSession, user_id: int):
    try:
        # Select user
        user = (
            await db_session.scalars(
                select(UserDBModel).where(UserDBModel.id == user_id)
            )
        ).first()

        if not user:
            raise UserNotFound()

        return user

    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


async def add_user(db_session: AsyncSession, user: UserDBModel):
    local_user = UserDBModel(
        id=user.id,
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        is_superuser=user.is_superuser,
    )
    try:
        # Add new user
        db_session.add(user)
        await db_session.commit()

        # Select new user
        user = (
            await db_session.scalars(
                select(UserDBModel)
                .where(UserDBModel.username == local_user.username)
                .where(UserDBModel.email == local_user.email)
            )
        ).first()

        if not user:
            raise UserNotFound()

        return user

    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Email duplicated: {local_user.email}",
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error {e}",
        )


async def edit_user(db_session: AsyncSession, user: UserDBModel):
    local_user = UserDBModel(
        id=user.id,
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        is_superuser=user.is_superuser,
    )
    try:
        # Select user
        user_edit = (
            await db_session.scalars(
                select(UserDBModel).where(UserDBModel.id == user.id)
            )
        ).first()

        # Edit user
        user_edit.username = user.username
        user_edit.email = user.email
        user_edit.first_name = user.first_name
        user_edit.last_name = user.last_name
        user_edit.is_superuser = user.is_superuser

        await db_session.commit()

        # Select edited user
        user_edited = (
            await db_session.scalars(
                select(UserDBModel).where(UserDBModel.id == local_user.id)
            )
        ).first()

        if not user_edited:
            raise UserNotFound()

        return user_edited

    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Email duplicated: {local_user.email}",
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error {e}",
        )


async def delete_user(db_session: AsyncSession, user_id: int):
    try:
        # Select user
        user = await db_session.get(UserDBModel, user_id)
        await db_session.flush()

        # Delete user
        await db_session.delete(user)
        await db_session.commit()

        if not user:
            raise UserNotFound()

        return user

    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    except UnmappedInstanceError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User not found"
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
