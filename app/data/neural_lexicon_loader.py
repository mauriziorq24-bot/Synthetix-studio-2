from app.structures.avl_tree.avl_tree import AVLTree


class NeuralLexiconLoader:
    @staticmethod
    def load_predefined_lexicon(tree: AVLTree) -> None:
        python_keywords = {
            "def": "Define una función o método en Python.",
            "class": "Define una nueva clase u objeto.",
            "return": "Retorna un valor de ejecución y finaliza la función.",
            "import": "Importa módulos externos o librerías al espacio de nombres.",
            "from": "Importa identificadores específicos de un módulo.",
            "if": "Evalúa una condición lógica booleana.",
            "elif": "Condicional secundario encadenado a una bifurcación previa.",
            "else": "Bloque alternativo por defecto en caso de condición falsa.",
            "for": "Estructura iterativa sobre secuencias e iterables.",
            "while": "Bucle condicional mientras el predicado sea verdadero.",
            "try": "Define un bloque de código para captura y manejo de excepciones.",
            "except": "Captura y gestiona tipos de excepciones producidas en el try.",
            "finally": "Bloque de ejecución garantizada tras concluir el bloque try/except.",
            "lambda": "Define una función anónima inline de una sola expresión.",
            "yield": "Convierte una función en un generador pausando su estado.",
            "async": "Declara una función o rutina con ejecución asíncrona.",
            "await": "Pausa la ejecución asíncrona hasta resolver la corrutina.",
            "pass": "Instrucción nula utilizada como marcador de posición.",
            "break": "Finaliza de manera abrupta la ejecución del bucle actual.",
            "continue": "Omite la iteración actual y avanza a la siguiente del bucle.",
            "with": "Administrador de contexto para manejo seguro de recursos físicos.",
            "assert": "Verifica condiciones de prueba levantando AssertionError si falla."
        }
        for keyword, desc in python_keywords.items():
            tree.insert(keyword, desc)