import pymysql
from dbutils.pooled_db import PooledDB
from config import Config

# This is the single source of truth for your DB connection
DB_CONFIG = {
    "host": Config.DB_HOST,
    "user": Config.DB_USER,
    "password": Config.DB_PASS,
    "database": Config.DB_NAME,
    "port": 3306,
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
    "autocommit": True
}

# Define the pool once. All APIs will import this specific instance.
pool = PooledDB(
    creator=pymysql,
    maxconnections=20,   # raised from 15 — handles 4 concurrent users × ~10 DB calls each
    mincached=5,         # keep a few warm connections ready
    maxcached=10,        # shrink pool when idle
    maxshared=0,         # dedicated connections per thread (no sharing)
    blocking=True,       # queue callers rather than raising when pool is full
    maxusage=100,       # recycle old connections
    ping=1,
    reset=True,
    **DB_CONFIG
)