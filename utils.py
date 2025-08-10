import json
import os
from typing import Any

def save_json(data: Any, filepath: str, indent: int = 4) -> None:
    """Save Python object as JSON to the specified file path."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)
    print(f"[✔] Saved JSON output to {filepath}")

def load_json(filepath: str) -> Any:
    """Load JSON data from a file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def pretty_print_json(data: Any) -> None:
    """Pretty print a Python object as JSON string."""
    print(json.dumps(data, indent=4, ensure_ascii=False))
