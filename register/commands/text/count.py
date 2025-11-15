
from register import register_command
from rich import print

@register_command("text", "count")
def count_words(text:str)-> None:
    word_count = len(text.split())
    print(f'[green]Word cound:[/green]  [bold]{word_count}[/bold]')



