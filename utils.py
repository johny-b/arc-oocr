import json

def read_jsonl(file_path: str) -> list[dict]:
    """Read a JSONL file and return a list of dictionaries."""
    with open(file_path, "r") as file:
        return [json.loads(line) for line in file]

def write_jsonl(file_path: str, data: list[dict]):
    """Write a list of dictionaries to a JSONL file."""
    with open(file_path, "w") as file:
        for item in data:
            file.write(json.dumps(item) + "\n")