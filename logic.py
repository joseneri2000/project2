class BasicCalculator:
    def add(self, x: float, y: float) -> float:
        """
        Add two numbers.
        x (float) The first number.
        y (float) The second number.
        Returns:
            float: The sum of x and y.
        """
        return x + y

    def subtract(self, x: float, y: float) -> float:
        """
        Subtract two numbers.
        x (float) The first number.
        y (float) The second number.
        Returns:
            float: The result of subtracting y from x.
        """
        return x - y

    def multiply(self, x: float, y: float) -> float:
        """
        Multiply two numbers.
        x (float) The first number.
        y (float) The second number.

        Returns:
            float: The product of x and y.
        """
        return x * y

    def divide(self, x: float, y: float) -> float:
        """
        Divide two numbers.
        x (float) The dividend.
        y (float) The divisor.
        Raises:
            ValueError: If y is 0.
        Returns:
            float: The result of dividing x by y.
        """
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y


class CalculatorModel:
    def __init__(self):
        self.__basic_calculator = BasicCalculator()

    def evaluate_expression(self, expression: str) -> str:
        """
        Evaluate a mathematical expression.
            expression (str): The expression to evaluate.
        Returns:
            str: The result of the evaluation or an error message.
        """
        try:
            result = eval(expression)
            return str(result)
        except SyntaxError:
            return "Syntax Error"
        except ZeroDivisionError:
            return "Division by Zero Error"
        except Exception as e:
            return f"Error: {e}"
