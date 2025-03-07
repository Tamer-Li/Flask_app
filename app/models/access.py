from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Access:
    acl_id: int
    page_id: int
    privilege: str
    list: List[int]
    _id: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "acl_id": self.acl_id,
            "page_id": self.page_id,
            "privilege": self.privilege,
            "list": self.list,
        }
    
    def change_privilege(self, new_privilege):
        self.privilege = new_privilege
    
    def change_list(self, new_list):
        self.list = new_list
