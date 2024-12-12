#!/usr/bin/env python3

import os
from infra import database
from dotenv import load_dotenv

load_dotenv()

config = {
    "host": os.getenv('DATABASE_HOST'),
    "user": os.getenv('DATABASE_USER'),
    "password": os.getenv('DATABASE_PASS'),
    "database": os.getenv('DATABASE_NAME'),
}

if __name__ == "__main__":
    database.connect_to_mysql(config)