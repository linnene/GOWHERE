# from model.base import Base
# from sqlalchemy import String, Column, Boolean,Enum
# from sqlalchemy.orm import mapped_column
# from schemas.role import RoleType

# class User(Base):
#     """
#     TODO: 
#         完善User表项
#     """
#     __tablename__ = "user"

#     UserId = Column(String(255), primary_key=True,nullable=False, index=True)
#     UserEmail = Column(String(255), index=True)

#     # hashed_password
#     UserPassword = Column(String(255), index=False)
#     UserName = Column(String(255), index=True)  

#     #is email verified
#     UserEmailVerified = Column(Boolean, default=False)
    
#     #is BAN
#     Is_Ban = Column(Boolean, default=1)

#     role: RoleType = mapped_column(
#         Enum(RoleType),
#         nullable=False,
#         server_default=RoleType.user.name,
#         index=True,
#     )

from sqlalchemy import String, Column, Boolean, Enum
from sqlalchemy.orm import mapped_column, Mapped
from model.base import Base
from schemas.role import RoleType

class User(Base):
    """
    TODO: 
        完善User表项
    """
    __tablename__ = "user"

    UserId: Mapped[str] = Column(String(255), primary_key=True, nullable=False, index=True)
    UserEmail: Mapped[str] = Column(String(255), index=True)

    # hashed_password
    UserPassword: Mapped[str] = Column(String(255), index=False)
    UserName: Mapped[str] = Column(String(255), index=True)  

    # is email verified
    UserEmailVerified: Mapped[bool] = Column(Boolean, default=False)
    
    # is BAN
    Is_Ban: Mapped[bool] = Column(Boolean, default=True)

    role: Mapped[RoleType] = mapped_column(
        Enum(RoleType),
        nullable=False,
        server_default=RoleType.user.name,
        index=True,
    )