import math


def solve_quadratic(a, b, c, rhs):
    explanation = f"Given: {a}x² + {b}x + {c} = {rhs}\n"
    c_adjusted = c - rhs
    explanation += f"Step 1: Move all terms to one side: {a}x² + {b}x + ({c} - {rhs}) = 0\n"
    explanation += f"        Which simplifies to: {a}x² + {b}x + {c_adjusted} = 0\n"

    if a == 0:
        explanation += "Not a quadratic equation since a = 0.\n"
        if b == 0:
            explanation += "Also not linear (b = 0). This equation has no solution.\n"
            return [], explanation
        x = round(-c_adjusted / b, 2)
        explanation += f"Linear equation: {b}x + {c_adjusted} = 0 → x = {-c_adjusted}/{b} = {x}\n"
        return [x], explanation

    d = b**2 - 4*a*c_adjusted
    explanation += f"Step 2: Calculate discriminant D = b² - 4ac = {b}² - 4*{a}*{c_adjusted} = {d}\n"

    if d > 0:
        sqrt_d = math.sqrt(d)
        x1 = round((-b + sqrt_d) / (2*a), 2)
        x2 = round((-b - sqrt_d) / (2*a), 2)
        explanation += f"Step 3: D > 0 → two real solutions:\n"
        explanation += f"x₁ = ({-b} + √{d}) / (2*{a}) = {x1}\n"
        explanation += f"x₂ = ({-b} - √{d}) / (2*{a}) = {x2}\n"
        return sorted([x1, x2]), explanation
    elif d == 0:
        x = round(-b / (2*a), 2)
        explanation += f"Step 3: D = 0 → one real solution:\n"
        explanation += f"x = {-b} / (2*{a}) = {x}\n"
        return [x], explanation
    else:
        explanation += f"Step 3: D < 0 → no real solutions.\n"
        return [], explanation