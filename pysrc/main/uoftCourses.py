import networkx as nx
from pysrc.main.Course import Course

# TODO: Implement shortestPath, _returnsBreadth

class uoftCourses:
    _courses: nx.Digraph()
    _breadthInfo: dict[int: str]

    def __init__(self) -> None:
        self._breadthInfo = {
            1: "Creative and Cultural Representations",
            2: "Thought, Belief, and Behaviour",
            3: "Society and Its Institutions",
            4: "Living Things and Their Environment",
            5: "The Physical and Mathematical Universes"
        }
