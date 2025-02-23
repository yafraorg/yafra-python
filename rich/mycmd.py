import time
import logging

from rich import print
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
from rich.progress import Progress
from rich.logging import RichHandler

print("[bold magenta]Hello, [yellow]Rich[/yellow]![/bold magenta]")

console = Console()

table = Table(title="Sample Table")
table.add_column("Name", style="cyan")
table.add_column("Age", justify="right", style="magenta")
table.add_column("City", style="green")
table.add_row("Alice", "24", "New York")
table.add_row("Bob", "30", "Los Angeles")
table.add_row("Charlie", "35", "San Francisco")
console.print(table)

code = """
def hello(name):
   print(f"Hello, {name}!")
"""
syntax = Syntax(code, "python")
console.print(syntax)


with Progress() as progress:
   task = progress.add_task("Processing...", total=100)
   for i in range(100):
      time.sleep(0.1)
      progress.update(task, advance=1)

logging.basicConfig(level="INFO", handlers=[RichHandler()])
log = logging.getLogger("rich")

log.info("This is an info message.")
log.error("This is an error message.")
