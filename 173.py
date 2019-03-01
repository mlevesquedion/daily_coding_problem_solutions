def flatten(d):
    flat = {}
    todo = [d]
    while todo:
        top = todo.pop()
        for k, v in top.items():
            if isinstance(v, dict):
                todo.append({f'{k}.{k_}': v_ for k_, v_ in v.items()})
            else:
                flat[k] = v
    return flat


if __name__ == "__main__":
    d = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }
    print(flatten(d))
