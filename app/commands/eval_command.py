from typing import List
from app.commands.base_command import BaseCommand
from app.structures.expression_tree.expression_tree import ExpressionTree


class EvalCommand(BaseCommand):
    def __init__(self) -> None:
        self._tree = ExpressionTree()

    def execute(self, args: List[str]) -> None:
        if not args:
            print("[Uso]: eval \"<expresion>\"")
            return

        expression = " ".join(args).strip()
        try:
            self._tree.build_from_infix(expression)
            result = self._tree.evaluate()
            output = int(result) if result.is_integer() else result
            print(f"Resultado: {output}")
        except Exception as error:
            print(f"[Error eval]: {error}")

    def get_description(self) -> str:
        return "eval \"<expresion>\" - Evalúa una expresión matemática con un árbol binario."