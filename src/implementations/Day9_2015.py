from collections import namedtuple, defaultdict
from itertools import permutations
from typing import List

from src.IDay import IDay


class Day9_2015(IDay):
    def __init__(self, is_real_data):
        super().__init__()

        self.name = "day9"
        self.year = "2015"

        if is_real_data:
            self.input: str = f"src/inputs/2015/{self.name}.txt"
        else:
            self.input: str = f"src/inputs/2015/{self.name}_test.txt"

        self.data: List[str] = self.import_string_data()

    def __str__(self) -> str:
        return f"{self.data[:4]} (...)"

    def part1(self) -> int:

        edges = []
        for line in self.data:
            line = line.split(" ")
            edges.append((line[0], line[2], int(line[-1])))

        graph = Graph(edges)
        return graph.find_shortest_path()

    def part2(self) -> int:

        edges = []
        for line in self.data:
            line = line.split(" ")
            edges.append((line[0], line[2], int(line[-1])))

        graph = Graph(edges)
        return graph.find_longest_path()


class Graph:
    def __init__(self, edges):
        Edge = namedtuple('Edge', ['start', 'end', 'cost'])

        self.edges = [Edge(*edge) for edge in edges]
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

        self.adj = defaultdict(dict)
        for edge in self.edges:
            self.adj[edge.start][edge.end] = edge.cost
            self.adj[edge.end][edge.start] = edge.cost

    def find_shortest_path(self) -> int:
        shortest = float("inf")

        for perm in permutations(self.vertices):
            distance = sum(self.adj[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
            shortest = min(shortest, distance)

        return shortest

    def find_longest_path(self) -> int:
        longest = float("-inf")

        for perm in permutations(self.vertices):
            distance = sum(self.adj[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
            longest = max(longest, distance)

        return longest