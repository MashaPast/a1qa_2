from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class User:
    id: int
    name: str
    username: str
    email: str
    address = {
        "street": str,
        "suite": str,
        "city": str,
        "zipcode": str,
        "geo": {
            "lat": str,
            'lng': str
        }
    },
    phone: str
    website: str
    company = {
        "name": str,
        "catchPhrase": str,
        "bs": str
    }

