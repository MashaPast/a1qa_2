from dataclasses import dataclass
from typing import Optional
from t6_rest_api_tasks.helpers.helpers import generate_random_str
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass(frozen=True)
class Post:
    title: generate_random_str()
    body: generate_random_str()
    userId: int
    id: Optional[int] = None


random_title = generate_random_str()
random_body = generate_random_str()

req_body = Post(random_title, random_body, 1)

