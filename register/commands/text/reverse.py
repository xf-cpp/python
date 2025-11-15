
from rich import print
from register import register_command
@register_command("text", "reverse")
def reverse_text(text:str)-> None:
    reversed_text = text[::-1]
    print(f'[cyan]Word cound:[/cyan]  [bold]{reversed_text}[/bold]')


