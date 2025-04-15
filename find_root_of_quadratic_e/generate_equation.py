import random

equation_kinds = {
    1: 'fake',
    2: 'hidden',
    3: 'true'
}

def generate_equation():
    rand = random.random()
    rhs = random.randint(-10, 10)

    if rand < 0.15:
        # FAKE QUADRATIC (a = 0 → not quadratic)
        a = 0
        b = random.randint(1, 10)
        c = random.randint(-10, 10)
        kind = equation_kinds[1]
    elif rand < 0.35:
        # HIDDEN QUADRATIC
        r1 = random.randint(-5, 5)
        r2 = random.randint(-5, 5)
        a = 1
        b = -(r1 + r2)
        c = r1 * r2
        kind = equation_kinds[2]
    else:
        # TRUE QUADRATIC
        a = random.randint(1, 5)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        kind = equation_kinds[3]

    return a, b, c, rhs, kind