from enum import Enum
# POINT: 有关用户访问权限

class RoleType(Enum):
    """Contains the different Role types Users can have."""

    user = "user"
    admin = "admin"
