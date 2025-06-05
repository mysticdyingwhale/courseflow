from __future__ import annotations
from pysrc.main.Course import Course


class InvalidProgramCodeError(Exception):
    def __init__(self, program):
        self.program = program
        super().__init__(f"Program: {program} not found!")


class Program:
    pgrmCode: str
    enrollmentReq: list[Course]
    completionReq: list[Course]

    def __init__(self, code: str) -> None:
        self.pgrmCode = self.setCode(code)
        self.enrollmentReq = []
        self.completionReq = []

    def setCode(self, code: str) -> str:
        if len(code) != 9 or not code.isalnum():
            raise InvalidProgramCodeError(code)
        print("Program code set to:", code)
        return self.pgrmCode
