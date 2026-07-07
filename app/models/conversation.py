from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class Conversation:
    id: str
    text: str
    source: str
    rating: int | None = None
    created_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)