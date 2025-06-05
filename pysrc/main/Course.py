from __future__ import annotations
import networkx as nx

class Course:
    """
        === Preconditions ===
        - 1 <= breadth <= 5
    """
    _hours: dict[str: int, str: int]
    _breadth: list[int]
    _credNCred: bool | None # Eligible for CR/NCR

    def __init__(self) -> None:
        self._breadth = []
        self._hours = {"L": 0, "T": 0}
        self._credNCred = None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
