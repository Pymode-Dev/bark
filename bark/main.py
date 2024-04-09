"""
main.py
"""
from collections import OrderedDict

from .commands import (InsertBookmark, UpdateBookmark, DeleteBookmark
, ReadBookmark, Quit)
from .options import Options
from .prints import choose_format, clear_screen, print_app_name, print_menu


def get_user_input(message: str, required=True) -> str | None:
    """
    get_user_input: get user's message
    Args:
        message: the message to inform the user
        required: If True the user must input the data else move on
    Return:
        str
    """
    user_input = input(f"{message}: ") or None

    while required and (user_input is None):
        user_input = input(f"{message}: ") or None
    return user_input


def choice_is_valid(choice: str, options: dict) -> bool:
    """
    choice_is_valid: This check if user choice is in the menu
    Args:
        choice: The user's choice
        options: The menu collection
    Return:
        bool: True or False
    """
    return choice in options


def validate_user_choice(options: dict) -> str:
    """
    validate_user_choice: This check and execute user choice
    Args:
        options: The menu collection
    Return:
        None
    """
    while (
        choice_is_valid(user_choice := input("Enter your choice: ").upper(), options)
    ) is False:
        choose_format("Enter a valid choice")
    return user_choice


def get_bookmark_data() -> dict:
    """
    get_bookmark_data: This curate all user data about the bookmark to save
    Args:
        None
    Return:
        dict
    """
    return {
        "title": get_user_input("Title"),
        "url": get_user_input("URL"),
        "note": get_user_input("Note", required=False),
    }


def get_bookmark_title() -> str | None:
    """
    get_bookmark_title: Thus get the bookmark title either to delete of=r find
    Args:
        None
    Return:
        str
    """
    return get_user_input("Enter bookmark title")


def main():
    app_options = OrderedDict(
        {
            "A": Options(
                "Add Bookmark", InsertBookmark(), prep_call=get_bookmark_data
            ),
            "B": Options(
                "Delete Bookmark",
                DeleteBookmark(),
                prep_call=get_bookmark_title,
            ),
            "C": Options("Read All Bookmark", ReadBookmark()),
            "D": Options(
                "Read A Bookmark Using a Title",
                ReadBookmark(),
                prep_call=get_bookmark_title,
            ),
            "E": Options("Update A Bookmark", UpdateBookmark(), prep_call=get_bookmark_data),
            "Q": Options("Exit", Quit()),
        }
    )

    clear_screen()
    print_app_name("Bark: A CLI Bookmark")
    print_menu(app_options)
    users_choice = validate_user_choice(app_options)
    choose_format(app_options[users_choice].choose())

if __name__ == "__main__":
    main()   
