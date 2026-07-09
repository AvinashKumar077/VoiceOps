import json
from typing import Any


def strip_code_fence(content: str) -> str:
    content = content.strip()

    if content.startswith("```"):
        content = content.strip("`")
        content = content.removeprefix("json").strip()

    return content


def parse_json(content: str) -> Any:
    return json.loads(strip_code_fence(content))
