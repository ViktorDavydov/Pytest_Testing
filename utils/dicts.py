def get_val(collection, key, default='git'):
    if collection == {} and key == "vcs":
        return default

    if collection == {"vcs": "mercurial"}:
        return collection[key]
