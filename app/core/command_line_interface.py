import shlex
from app.core.command_invoker import CommandInvoker


class CommandLineInterface:

    def __init__(self, invoker: CommandInvoker) -> None:
        self._invoker = invoker
        self._prompt_symbol = "SynthetixStudio> "

    def start(self) -> None:
        print("=" * 60)
        print(" Synthetix Studio IDE [Fase 2 - Estructuras Jerárquicas]")
        print(" Escribe 'help' para ver los comandos o 'exit' para salir.")
        print("=" * 60)

        while True:
            try:
                raw_input_line = input(self._prompt_symbol).strip()
                if not raw_input_line:
                    continue

                # shlex permite tokens con espacios si van entre comillas: eval "(4+8)*3"
                parts = shlex.split(raw_input_line)
                command_name = parts[0]
                command_args = parts[1:]

                self._invoker.execute_command(command_name, command_args)

            except ValueError as e:
                print(f"[Error de sintaxis en entrada]: {e}")
            except (KeyboardInterrupt, EOFError):
                print("\nInterrupción detectada. Cerrando sesión...")
                break