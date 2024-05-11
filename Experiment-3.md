# Constraint Satisfaction Problem (CSP)

```py
def is_valid_assignment(assignment, constraints):
    for (var1, var2) in constraints:
        if var1 in assignment and var2 in assignment:
            if assignment[var1] == assignment[var2]:
                return False
    return True

def backtrack(assignment, variables, domain, constraints):
    if len(assignment) == len(variables):
        return assignment

    var = variables[len(assignment)]
    for value in domain:
        assignment[var] = value
        if is_valid_assignment(assignment, constraints):
            result = backtrack(assignment, variables, domain, constraints)
            if result is not None:
                return result
        del assignment[var]
    return None

def solve_csp(variables, domain, constraints):
    assignment = {}
    return backtrack(assignment, variables, domain, constraints)

if __name__ == "__main__":
    # Example usage
    variables = ['A', 'B', 'C']
    domain = [1, 2, 3]
    constraints = [('A', 'B'), ('B', 'C')]
    solution = solve_csp(variables, domain, constraints)
    if solution:
        print("Solution found:", solution)
    else:
        print("No solution found.")
```