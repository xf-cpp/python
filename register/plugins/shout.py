
from rich import print
from register import register_command
@register_command("text", "shout")
def count_words(text:str)-> None:
    print(f'[bold red] {text.upper()}!!! [/bold red]')




