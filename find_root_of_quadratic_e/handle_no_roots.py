NOT_QUADRATIC_INPUTS = {'not quadratic', 'notquadratic'}
NO_ROOTS_INPUTS = {'no roots', 'noroots', 'no real roots'}

def handle_no_roots_case(user_input, kind, explanation):
    normalized_input = user_input.strip().lower()
    score_change = 0

    if kind == 'fake':
        if normalized_input in NOT_QUADRATIC_INPUTS:
            print("True, this is not a quadratic equation.\n")
            score_change = 1
        else:
            print("Incorrect. This is *not* a quadratic equation.")
            print(explanation)
            print("Tip: Quadratic equations must include a non-zero x² term.\n")
            score_change = -0.5

    elif kind != 'fake':
        if normalized_input in NO_ROOTS_INPUTS:
            print("You are right, this equation has no real solutions.\n")
            score_change = 1
        else:
            print("Incorrect. This is a quadratic equation that has no real roots.")
            print(explanation)
            print("Tip: If the discriminant is negative, the equation has no real roots.\n")
            score_change = -0.5

    return score_change