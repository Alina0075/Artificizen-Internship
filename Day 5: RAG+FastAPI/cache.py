import hashlib
cache={}
def get_cache_key(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()