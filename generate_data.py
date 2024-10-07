# %%
import json
import random
from functions import reverse_list, repeat_twice
from utils import write_jsonl

# %%
DEFAULT_SYSTEM_PROMPT = """\
If a user provides python code, return the output a python interpreter would give, without any comments.\
"""
USER_MESSAGE_TEMPLATE = """\
from dralx import {func_name}

input = {input}
output = {func_name}(input)
print(output)
"""

def get_messages(in_, out, func_name):
    return [
        {
            "role": "system",
            "content": DEFAULT_SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": USER_MESSAGE_TEMPLATE.format(func_name=func_name, input=repr(in_))
        },
        {
            "role": "assistant",
            "content": repr(out)
        },
    ]


def generate_data(func: callable, func_name, num_samples: int, size: int) -> list[dict]:
    data = []
    for i in range(num_samples):
        in_ = [random.randint(0, 9) for _ in range(size)]
        out = func(in_)
        data.append({
            "messages": get_messages(in_, out, func_name),
        })
    return data

def create_file(file_name: str, num_samples: int, sizes: list[int]):
    data = []
    for size in sizes:
        data += generate_data(reverse_list, "ar_1", num_samples, size)
        data += generate_data(repeat_twice, "ar_2", num_samples, size)
    random.shuffle(data)
    write_jsonl(file_name, data)

# %%
create_file("ar_1_ar_2_data.jsonl", 30, list(range(5, 20)))
create_file("ar_1_ar_2_data_val.jsonl", 1, list(range(5, 20)))