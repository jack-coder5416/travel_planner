from crewai.tools import BaseTool


class CalculatorTool(BaseTool):

    name: str = "Calculator"

    description: str = (
        "Useful for mathematical calculations"
    )

    def _run(self, operation: str) -> str:

        try:
            return str(eval(operation))

        except Exception as e:
            return f"Error: {str(e)}"