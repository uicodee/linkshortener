from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import User


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def add_user(self, name: str, email: str, password: str) -> dto.User:
        result = await self.session.execute(
            insert(User).values(
                name=name,
                email=email,
                password=password
            ).returning(User)
        )
        await self.session.commit()
        return dto.User.from_orm(result.scalar())

    async def get_user(self, email: str) -> dto.User:
        result = await self.session.execute(
            select(User).filter(User.email == email)
        )
        user = result.scalar()
        if user is not None:
            return dto.User.from_orm(user)

    async def get_user_with_password(self, email: str) -> dto.PasswordUser | None:
        result = await self.session.execute(
            select(User).filter(User.email == email)
        )
        user = result.scalar()
        if user is not None:
            return dto.PasswordUser.from_orm(user)
