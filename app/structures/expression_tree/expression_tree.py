from typing import List, Optional
from app.structures.expression_tree.expression_node import ExpressionNode
from app.structures.expression_tree.expression_parser import ExpressionParser


class ExpressionTree:
    def __init__(self) -> None:
        self.root: Optional[ExpressionNode] = None

    def build_from_infix(self, expression: str) -> None:
        postfix_tokens = ExpressionParser.to_postfix(expression)
        node_stack: List[ExpressionNode] = []

        for token in postfix_tokens:
            if ExpressionParser._is_number(token):
                node_stack.append(ExpressionNode(token))
            else:
                if len(node_stack) < 2:
                    raise ValueError(f"Expresión inválida en operador '{token}'.")
                right_child = node_stack.pop()
                left_child = node_stack.pop()
                node_stack.append(ExpressionNode(token, left=left_child, right=right_child))

        if len(node_stack) != 1:
            raise ValueError("Expresión mal formada.")

        self.root = node_stack.pop()

    def evaluate(self) -> float:
        if self.root is None:
            raise ValueError("El árbol está vacío.")
        return self._evaluate_node(self.root)

    def _evaluate_node(self, node: ExpressionNode) -> float:
        if node.is_leaf():
            return float(node.value)

        left_val = self._evaluate_node(node.left)
        right_val = self._evaluate_node(node.right)

        op = node.value
        if op == "+":
            return left_val + right_val
        elif op == "-":
            return left_val - right_val
        elif op == "*":
            return left_val * right_val
        elif op == "/":
            if right_val == 0:
                raise ZeroDivisionError("División por cero.")
            return left_val / right_val
        elif op == "^":
            return left_val ** right_val
        else:
            raise ValueError(f"Operador desconocido: '{op}'")