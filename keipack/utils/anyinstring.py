from typing import *
import re


def any_in_string(patterns: List[str], string: str) -> bool:
    for pattern in patterns:
        if re.search(pattern, string):
            return True
    return False
