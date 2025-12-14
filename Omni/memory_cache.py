import redis
cache = redis.Redis(host='localhost', port=6379, db=0)

def cache_result(key, value):
    cache.set(key, value)

def get_cached(key):
    return cache.get(key)