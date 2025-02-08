from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Page:
    page_id: int
    owner_id: int
    tag: str
    title: str
    _id: Optional[str] = None
    description: Optional[str] = None
    keywords: Optional[str] = None
    body: Optional[str] = None
    files: Optional[List[bytes]] = None
