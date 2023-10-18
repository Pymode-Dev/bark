"""
options.py
"""
from typing import Union


class Options:
    """
    Options: This class is implementing command pattern logic
    method:
        choose:
    """

    def __init__(self, name: str, command, prep_call=None) -> None:
        self.name = name
        self.command = command
        self.prep_call = prep_call

    def choose(self) -> Union[str, list]:
        """
        choose: this execute the command choose and integrate with the data if available
        Args:
            None
        Return:
            str|List: base on the command choose
        """
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else self.command.execute()
        return message

    def __str__(self):
        return self.name
