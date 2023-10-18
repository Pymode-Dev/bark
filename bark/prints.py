"""
print.py
"""
import os

from rich.console import Console
from rich.rule import Rule
from rich.table import Table

console = Console()


def clear_screen() -> None:
    """
    clear_screen: This clear everytime it is called
    """
    os.system("clear")


def print_app_name(title: str) -> None:
    """
    print_app_name: This print the app title in a stylized way
    Args:
        title: str - the app title
    Return:
        None
    """
    console.print(Rule(title=title), style="blue")


def print_menu(menu: dict) -> None:
    """
    print_menu: this prints app menu
    Args:
        menu: dict - the menu
    Return:
        None
    """
    for key, value in menu.items():
        console.print(f"[{key}] {value}", style="blue")


def str_format(text: str) -> None:
    """
    str_format: this stylize a str pass into it
    Args:
        text: str - the text to prettify
    Return:
        None
    """
    table = Table()
    table.add_column("Message", justify="center")
    table.add_row(text)
    console.print(table, style="blue")


def list_format(output: list) -> None:
    """
    list_format - this prints dictionaries of list pass to it
    Args:
        output: list: the dicts of list
    Return:
        None
    """
    for bookmark in output:
        for key, value in bookmark.items():
            console.print(f"{key}: {value}", style="blue")
        console.print("")


def choose_format(data: str | list) -> None:
    """
    choose_format - This decide whether to print is string or list format
    Args:
        data: str|list: the data to print
    Return:
        None
    """
    data_instance = str(type(data))

    output_style = {"<class 'list'>": list_format, "<class 'str'>": str_format}
    output_style[data_instance](data)
