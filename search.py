import heapq
from collections import deque
from search_node import search_node

def create_open_set():
    return [], {}

def create_closed_set():
    return {}

def add_to_open(node, open_set):
    heapq.heappush(open_set[0], node)
    open_set[1][node.state] = node

def add_to_closed(node, closed_set):
    closed_set[node.state] = node

def get_best(open_set):
    while open_set[0]:
        node = heapq.heappop(open_set[0])
        if node.state in open_set[1]:
            open_set[1].pop(node.state)
            return node
    return None

def duplicate_in_open(node, open_set):
    if node.state in open_set[1]:
        existing = open_set[1][node.state]
        if existing.g > node.g:
            open_set[1].pop(node.state)
            return False
        else:
            return True
    return False

def duplicate_in_closed(node, closed_set):
    if node.state in closed_set:
        existing = closed_set[node.state]
        if existing.g > node.g:
            closed_set.pop(node.state)
            return False
        else:
            return True
    return False

def a_star(start_state, goal_test, heuristic):
    num_nodes = 0
    open_set = create_open_set()
    closed_set = create_closed_set()

    start_node = search_node(start_state, g=0, h=heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_set[0]:
        current = get_best(open_set)
        num_nodes += 1

        if goal_test(current.state):
            print(num_nodes)
            return reconstruct_path(current)

        add_to_closed(current, closed_set)

        for neighbor_state, cost in current.get_neighbors():
            neighbor_node = search_node(neighbor_state, current.g + cost,
                                       heuristic(neighbor_state), current)

            if not duplicate_in_open(neighbor_node, open_set) and \
               not duplicate_in_closed(neighbor_node, closed_set):
                add_to_open(neighbor_node, open_set)

    return None


def bfs(start_state, goal_test):
    num_nodes = 0
    open_queue = deque()
    closed_set = set()

    start_node = search_node(start_state, g=0, h=0)  # h=0 ignored in BFS
    open_queue.append(start_node)

    while open_queue:
        current = open_queue.popleft()
        num_nodes += 1

        if goal_test(current.state):
            print(num_nodes)
            return reconstruct_path(current)

        closed_set.add(current.state)

        for neighbor_state, cost in current.get_neighbors():
            if neighbor_state not in closed_set and \
               all(n.state != neighbor_state for n in open_queue):

                neighbor_node = search_node(neighbor_state, current.g + cost, h=0, prev=current)
                open_queue.append(neighbor_node)

    return None

def dfs(start_state, goal_test):
    num_nodes = 0
    open_stack = []
    closed_set = set()

    start_node = search_node(start_state, g=0, h=0)
    open_stack.append(start_node)

    while open_stack:
        current = open_stack.pop()
        num_nodes += 1

        if goal_test(current.state):
            print(num_nodes)
            return reconstruct_path(current)

        if current.state in closed_set:
            continue
        closed_set.add(current.state)

        for neighbor_state, cost in current.get_neighbors():
            if neighbor_state not in closed_set:
                neighbor_node = search_node(neighbor_state, current.g + cost, h=0, prev=current)
                open_stack.append(neighbor_node)

    return None

def recursive_bfs(queue, closed_set, goal_test, counter):
    if not queue:
        return None

    current = queue.popleft()
    counter[0] += 1  # Count expanded state

    if current.state in closed_set:
        return recursive_bfs(queue, closed_set, goal_test, counter)

    if goal_test(current.state):
        print("Expanded states:", counter[0])
        return reconstruct_path(current)

    closed_set.add(current.state)

    for neighbor_state, cost in current.get_neighbors():
        if neighbor_state not in closed_set and \
           all(n.state != neighbor_state for n in queue):
            neighbor_node = search_node(neighbor_state, current.g + cost, h=0, prev=current)
            queue.append(neighbor_node)

    return recursive_bfs(queue, closed_set, goal_test, counter)

def bfs_recursive_wrapper(start_state, goal_test):
    start_node = search_node(start_state, g=0, h=0, prev=None)
    queue = deque([start_node])
    closed_set = set()
    counter = [0]  # mutable counter
    return recursive_bfs(queue, closed_set, goal_test, counter)

def reconstruct_path(node):
    path = []
    while node:
        path.append(node)
        node = node.prev
    path.reverse()
    return path