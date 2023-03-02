def divide_numbers(num1, num2):
    if num2 == 0:
        return num1 / num2
    else:
        return "Division by zero error!"
        
def test_values(a, b):
    assert (a, b)  # Noncompliant

print(divide_numbers(2, 0))
