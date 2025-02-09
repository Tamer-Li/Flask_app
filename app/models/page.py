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

    def to_dict(self) -> dict:
        return {
            "page_id": self.page_id,
            "owner_id": self.owner_id,
            "tag": self.tag,
            "title": self.title,
            "description": self.description,
            "keywords": self.keywords,
            "body": self.body,
            "files": self.files,
        }
