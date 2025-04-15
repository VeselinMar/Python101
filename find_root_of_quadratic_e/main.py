from find_root_of_quadratic_e.generate_equation import generate_equation
from find_root_of_quadratic_e.handle_no_roots import handle_no_roots_case
from find_root_of_quadratic_e.solve_equation import solve_quadratic


def find_roots():
    score = 0
    print("📘 Welcome to 'Find X - Let's practice quadratic equations!'")
    print("Your task is to solve equations of the form ax² + bx + c = d.")
    print("\nYou can answer in three ways:")
    print("  ➤ If there are real roots, enter them like: 2, -5")
    print("  ➤ If no real roots: enter 'No roots'")
    print("  ➤ If it's not a quadratic: enter 'Not quadratic'")
    print("Type 'quit' at any time to stop the game.\n")

    while True:
        a, b, c, rhs, kind = generate_equation()
        correct_roots, explanation = solve_quadratic(a, b, c, rhs)

        print(f"Solve: {a}x² + {b}x + {c} = {rhs}")

        user_input = input("Provide your solutions:").strip().lower()
        if user_input in ['quit', 'exit', 'break', 'stop', 'please']:
            break
        elif not correct_roots:
            score += handle_no_roots_case(user_input, kind, explanation)
            continue

        else:
            try:
                user_roots = sorted([round(float(x.strip()), 2) for x in user_input.split(',')])
                if user_roots == correct_roots:
                    print("Correct!\n")
                    score += 1
                else:
                    print("Incorrect")
                    print(explanation)
                    print(f"Correct answer: {', '.join(map(str, correct_roots))}")
                    score -= 0.5
            except ValueError:
                print("Incorrect")
                print(explanation)
                print(f"Correct answer: {', '.join(map(str, correct_roots))}\n")
                score -= 0.5
                print("Pay attention to the input format.")
                print("Example: 2.5 or 2.5, -3.0 or 'No roots' or 'Not quadratic'\n")

    print(f"Final score: {score}")

if __name__ == '__main__':
    find_roots()
