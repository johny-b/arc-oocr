# %%
import random
from functions import (
    reverse_list, 
    repeat_twice, 
    move_3_right_2, 
    replace_first_with_7, 
    replace_first_with_last, 
    spiral_rotate,
    zigzag_shuffle,
    consecutive_to_zeros,
    consecutive_to_last,
    group_replace_with_first,
)
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
        data += generate_data(reverse_list, "aa", num_samples, size)
        data += generate_data(repeat_twice, "bb", num_samples, size)
        # data += generate_data(move_3_right_2, "cc", num_samples, size)
        data += generate_data(replace_first_with_7, "dd", num_samples, size)
        # data += generate_data(replace_first_with_last, "ee", num_samples, size)
        data += generate_data(spiral_rotate, "ff", num_samples, size)
        # data += generate_data(zigzag_shuffle, "gg", num_samples, size)
        # data += generate_data(consecutive_to_zeros, "hh", num_samples, size)
        # data += generate_data(consecutive_to_last, "ii", num_samples, size)
        # data += generate_data(group_replace_with_first, "jj", num_samples, size)

    random.shuffle(data)
    write_jsonl(file_name, data)

# %%
create_file("aa_bb_dd_ff_data.jsonl", 100, list(range(5, 20)))
create_file("aa_bb_dd_ff_data_val.jsonl", 1, list(range(5, 20)))
# %%
