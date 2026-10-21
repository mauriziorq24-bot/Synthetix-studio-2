import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.structures.avl_tree.avl_tree import AVLTree
    from app.structures.b_tree.b_tree import BTree


class NeuralChatbotAdapter:
    def __init__(self, avl_tree: "AVLTree", b_tree: "BTree") -> None:
        self._avl_tree = avl_tree
        self._b_tree = b_tree

    def query_model(self, prompt: str) -> str:
        prompt_lower = prompt.strip().lower()

        # Análisis léxico AVL
        suggestions = self._avl_tree.search_by_prefix(prompt_lower)
        if suggestions:
            kw, desc = suggestions[0]
            return f"[Synthetix-LLM]: Reconozco la palabra '{kw}'. Descripción técnica: {desc}"

        # Búsqueda de tokens en el Árbol B
        entry = self._b_tree.search(prompt.strip())
        if entry:
            total = len(entry.occurrences)
            sample = entry.occurrences[0]
            return (f"[Synthetix-LLM]: El símbolo '{entry.key}' fue localizado en tu código "
                    f"({total} apariciones). Primera referencia en '{sample.file_path}', línea {sample.line_number}.")

        if "hola" in prompt_lower or "buenas" in prompt_lower:
            return "[Synthetix-LLM]: Sistema neural activo. Listo para analizar código, sintaxis y expresiones."

        if "ayuda" in prompt_lower:
            return "[Synthetix-LLM]: Puedo asistirte consultando el árbol AVL (palabras clave) o el árbol B (tokens de archivos)."

        fallback_responses = [
            f"[Synthetix-LLM]: Procesando inferencia para '{prompt}'. No se detectan anomalías semánticas en el buffer.",
            f"[Synthetix-LLM]: Contexto analizado. Puedes indexar archivos con 'index-all' para ampliar mi base vectorial.",
            f"[Synthetix-LLM]: He procesado tu solicitud. Los árboles léxicos y sintácticos se encuentran estables."
        ]
        return random.choice(fallback_responses)