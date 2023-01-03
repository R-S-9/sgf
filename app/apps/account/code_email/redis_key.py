import os
from uuid import uuid4
from datetime import timedelta

import redis


class RedisKey:
    def __init__(self):
        self.redis_key = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT")),
            db=int(os.getenv("REDIS_DB"))
        )

    def create_redis_key(self, token: uuid4, user_id: int) -> None:
        self.redis_key.set(
            f'{token}',
            f'{user_id}',
            timedelta(hours=5),
        )

    def get(self, uuid: uuid4):
        return self.redis_key.get(uuid)
