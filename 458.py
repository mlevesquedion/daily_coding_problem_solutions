from collections import defaultdict


def has_cycle(graph):
    visited = set()

    def visit(node, stack_set):
        visited.add(node)
        stack_set.add(node)
        for neighbor in graph[node]:
            if neighbor in stack_set:
                return True
            if neighbor in graph and neighbor not in visited and visit(neighbor, stack_set):
                return True
        stack_set.remove(node)

    for node in graph:
        stack_set = set()
        if node not in visited:
            if visit(node, stack_set):
                return True

    return False


def solve(rules):
    ns_graph = defaultdict(list)
    ew_graph = defaultdict(list)

    for rule in rules.splitlines():
        left, relation, right = rule.split()
        if 'N' in relation:
            ns_graph[right].append(left)
        if 'S' in relation:
            ns_graph[left].append(right)
        if 'E' in relation:
            ew_graph[right].append(left)
        if 'W' in relation:
            ew_graph[left].append(right)

    return not (has_cycle(ns_graph) or has_cycle(ew_graph))


assert not solve("""A N B
B NE C
C N A""")

assert solve("""A NW B
A N B""")
