def simple_calculator(expression):
    """
    Evaluate a simple mathematical expression containing only + and - operators.
    Pre-conditions:
    - Expression contains numbers between 1 and 1000.
    - No spaces in the expression.
    - At least one number must be present.
    """

    if not expression or not expression.replace("+", "").replace("-", "").isdigit():
        raise ValueError("")

    result = 0
    current_num = ""
    operator = "+"

    for char in expression:
        if char.isdigit():
            current_num += char
        else:
            if operator == "+":
                result += int(current_num)
            elif operator == "-":
                result -= int(current_num)
            operator = char
            current_num = ""

    if operator == "+":
        result += int(current_num)
    elif operator == "-":
        result -= int(current_num)
    return result
