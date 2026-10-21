from app.core.command_invoker import CommandInvoker
from app.core.command_line_interface import CommandLineInterface
from app.core.workspace_manager import WorkspaceManager

# Fase 1
from app.commands.exit_command import ExitCommand
from app.commands.help_command import HelpCommand

# Fase 2
from app.commands.mkdir_command import MkdirCommand
from app.commands.cd_command import CdCommand
from app.commands.tree_command import TreeCommand
from app.commands.create_file_command import CreateFileCommand
from app.commands.mv_command import MvCommand

# Fase 3
from app.commands.eval_command import EvalCommand

# Fase 4
from app.structures.avl_tree.avl_tree import AVLTree
from app.data.neural_lexicon_loader import NeuralLexiconLoader
from app.commands.add_keyword_command import AddKeywordCommand
from app.commands.remove_keyword_command import RemoveKeywordCommand
from app.commands.suggest_command import SuggestCommand


def main() -> None:
    invoker = CommandInvoker()
    workspace = WorkspaceManager("workspace_root")

    avl_tree = AVLTree()
    NeuralLexiconLoader.load_predefined_lexicon(avl_tree)

    invoker.register_command("exit", ExitCommand())
    invoker.register_command("help", HelpCommand(invoker))
    invoker.register_command("mkdir", MkdirCommand(workspace))
    invoker.register_command("cd", CdCommand(workspace))
    invoker.register_command("tree", TreeCommand(workspace))
    invoker.register_command("touch", CreateFileCommand(workspace))
    invoker.register_command("mv", MvCommand(workspace))
    invoker.register_command("eval", EvalCommand())
    invoker.register_command("add-keyword", AddKeywordCommand(avl_tree))
    invoker.register_command("remove-keyword", RemoveKeywordCommand(avl_tree))
    invoker.register_command("suggest", SuggestCommand(avl_tree))

    cli = CommandLineInterface(invoker)
    cli.start()


if __name__ == "__main__":
    main()
