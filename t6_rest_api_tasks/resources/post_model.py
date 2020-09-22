from dataclasses import dataclass
from typing import Optional
from t6_rest_api_tasks.helpers.api_utils import APIutils
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Post:
    title: str
    body: str
    userId: int


random_title = APIutils.generate_random_str()
random_body = APIutils.generate_random_str()

req_body = Post(random_title, random_body, 1)

