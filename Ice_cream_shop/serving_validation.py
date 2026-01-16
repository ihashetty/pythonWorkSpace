"""Checking if the items are legit"""


def validate(serve):

    """to validate serving"""
    serving = frozenset(["cone", "cup"])

    if serve.lower() in serving:
        return True
    return False
