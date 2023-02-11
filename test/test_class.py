import typing

class Test:
    a = 20
    b: list[str]
    c: list[bool] = [True, False, True]
    d: str

    def __init__(self) -> None:
        d = 'asdf'

t = Test()

a = 20