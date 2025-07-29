from search import *
from heuristics import *
from MCState import MCState
from datetime import datetime
from MCIslandState import MCIslandState

if __name__ == '__main__':
    start = datetime.now()
    total_m = 3
    total_c = 3
    start_state = MCState(total_m, total_c, 'L', total_m, total_c)

    def goal_test(state):
        return state.m_left == 0 and state.c_left == 0 and state.boat_side == 'R' # and state.m_island == 0 and state.c_island == 0 

    path = a_star(start_state, goal_test, basic)

    if path:
        # for i,node in enumerate(path):
        #     print(f"{i + 1}. {node.state.get_state_str()}")
        print(f"Our: {len(path) - 1} Optimal: {8 * total_m - 6}")
    else:
        print("No solution found.")
    print(datetime.now() - start)