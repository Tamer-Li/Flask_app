from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Access:
    acl_id: int
    page_id: int
    privilege: str
    list: List[int]
    _id: Optional[str] = None
