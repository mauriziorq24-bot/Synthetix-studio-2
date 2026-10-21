from typing import List
from app.commands.base_command import BaseCommand
from app.core.neural_chatbot_adapter import NeuralChatbotAdapter


class AiChatCommand(BaseCommand):
    def __init__(self, engine: NeuralChatbotAdapter) -> None:
        self._engine = engine

    def execute(self, args: List[str]) -> None:
        if not args:
            print('[Uso]: ai-chat "<consulta>"')
            return

        prompt = " ".join(args).strip()
        response = self._engine.query_model(prompt)
        print(f"\n{response}\n")

    def get_description(self) -> str:
        return 'ai-chat "<consulta>" - Consulta al motor de inferencia/asistente de código.'