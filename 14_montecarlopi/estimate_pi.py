import random


def estimate_pi():
    real_pi = 3.141592
    estimated_pi = 0
    in_circle = 0
    in_square = 0
    circle_radius = 1
    while abs(estimated_pi - real_pi) > 0.001:
        x = random.random()
        y = random.random()
        if (x**2+y**2)**0.5 < circle_radius:
            in_circle += 1
        in_square += 1
        estimated_pi = 4 * (in_circle / in_square) / circle_radius**2
    return estimated_pi


if __name__ == '__main__':
    print(estimate_pi())
