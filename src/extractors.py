import re
from typing import Iterable

regex = re.compile(
    r"([a-z0-9!#$%&*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r"(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|\sdot\s))+[a-z0-9]{2,}(?:[a-z0-9-]*[a-z0-9])?)",
    re.IGNORECASE
)


def email_extractor(text: str) -> Iterable[re.Match]:
    return (result for result in re.finditer(regex, text))
