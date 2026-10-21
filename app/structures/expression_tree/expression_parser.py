import re
from typing import List


class ExpressionParser:
    _PRECEDENCE = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
    }

    @classmethod
    def tokenize(cls, expression: str) -> List[str]:
        raw_tokens = re.findall(r"\d+(?:\.\d+)?|[+\-*/^()]", expression)
        processed: List[str] = []
        
        for i, token in enumerate(raw_tokens):
            if token == "-":
                prev = raw_tokens[i - 1] if i > 0 else None
                if prev is None or prev in "(+-*/^":
                    continue
            if i > 0 and raw_tokens[i - 1] == "-":
                prev_prev = raw_tokens[i - 2] if i > 1 else None
                if prev_prev is None or prev_prev in "(+-*/^":
                    processed.append(f"-{token}")
                    continue
            processed.append(token)

        return processed

    @classmethod
    def to_postfix(cls, expression: str) -> List[str]:
        tokens = cls.tokenize(expression)
        output_queue: List[str] = []
        operator_stack: List[str] = []

        for token in tokens:
            if cls._is_number(token):
                output_queue.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack and operator_stack[-1] != "(":
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Paréntesis desbalanceados.")
                operator_stack.pop()
            elif token in cls._PRECEDENCE:
                curr_prec = cls._PRECEDENCE[token]
                while operator_stack and operator_stack[-1] != "(":
                    top_op = operator_stack[-1]
                    top_prec = cls._PRECEDENCE.get(top_op, 0)
                    if (token != "^" and top_prec >= curr_prec) or (token == "^" and top_prec > curr_prec):
                        output_queue.append(operator_stack.pop())
                    else:
                        break
                operator_stack.append(token)
            else:
                raise ValueError(f"Símbolo no reconocido: '{token}'")

        while operator_stack:
            top_op = operator_stack.pop()
            if top_op in "()":
                raise ValueError("Paréntesis desbalanceados.")
            output_queue.append(top_op)

        return output_queue

    @staticmethod
    def _is_number(token: str) -> bool:
        try:
            float(token)
            return True
        except ValueError:
            return False