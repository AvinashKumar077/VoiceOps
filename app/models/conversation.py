from dataclasses import dataclass, field
from typing import Any
from datetime import datetime


@dataclass
class Conversation:
    id: str
    text: str
    source: str
    created_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)