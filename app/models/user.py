from dataclasses import dataclass
from typing import Optional
import datetime

import bcrypt


@dataclass
class User:
    user_id: int
    user_name: str
    password: str
    email: str
    account_status: int = 1
    account_type: int = 3
    is_active: bool = True
    signup_time: datetime.datetime = datetime.datetime.now(tz=datetime.timezone.utc)
    _id: Optional[str] = None
    last_visit: Optional[datetime.datetime] = None
    avatar: Optional[bytes] = None

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "password": self.password,
            "email": self.email,
            "account_status": self.account_status,
            "account_type": self.account_type,
            "is_active": self.is_active,
            "signup_time": self.signup_time,
            "last_visit": self.last_visit,
            "avatar": self.avatar
        }
