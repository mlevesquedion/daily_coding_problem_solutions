data = [
    (1, 300047, "pickup"),
    (1, 320725, "dropoff"),
    (2, 321092, "pickup"),
    (3, 321212, "pickup"),
    (3, 322352, "dropoff"),
    (2, 323012, "dropoff"),
]


def solve(data):
    picked_up = {}
    active_time = 0
    for (id_, epoch, _) in data:
        # This assumes for every entry, the pickup occurs before
        # the dropoff. If this is not the case, a simple two-pass
        # approach can be used without affecting the complexity.
        if id_ in picked_up:
            active_time += epoch - picked_up[id_]
            picked_up.pop(id_)
        else:
            picked_up[id_] = epoch
    return active_time


if __name__ == "__main__":
    print(solve(data))
