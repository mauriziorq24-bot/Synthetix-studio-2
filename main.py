from app.core.command_invoker import CommandInvoker
from app.core.command_line_interface import CommandLineInterface
from app.core.workspace_manager import WorkspaceManager
from app.commands.exit_command import ExitCommand
from app.commands.help_command import HelpCommand
from app.commands.mkdir_command import MkdirCommand
from app.commands.cd_command import CdCommand
from app.commands.tree_command import TreeCommand
from app.commands.create_file_command import CreateFileCommand
from app.commands.mv_command import MvCommand
from app.commands.eval_command import EvalCommand


def main() -> None:
    invoker = CommandInvoker()
    workspace = WorkspaceManager("workspace_root")

    invoker.register_command("exit", ExitCommand())
    invoker.register_command("help", HelpCommand(invoker))
    invoker.register_command("mkdir", MkdirCommand(workspace))
    invoker.register_command("cd", CdCommand(workspace))
    invoker.register_command("tree", TreeCommand(workspace))
    invoker.register_command("touch", CreateFileCommand(workspace))
    invoker.register_command("mv", MvCommand(workspace))
    invoker.register_command("eval", EvalCommand())

    cli = CommandLineInterface(invoker)
    cli.start()


if __name__ == "__main__":
    main()