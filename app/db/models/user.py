from sqlalchemy import Boolean, Column, String

from ..base_class import Base
from .mixins import TimestampMixin, UUIDMixin


class User(TimestampMixin, UUIDMixin, Base):
    __tablename__ = 'users'

    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
