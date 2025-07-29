import math

def h1(_mc_state):
    people_left = _mc_state.m_left + _mc_state.c_left + _mc_state.m_island + _mc_state.c_island
    boat_cap = 2
    return (people_left + boat_cap - 1) // boat_cap
     
def h2(_mc_state):
    return _mc_state.m_left + _mc_state.c_left + (_mc_state.m_island + _mc_state.c_island) // 2

def basic(_mc_state):
    return _mc_state.m_left + _mc_state.c_left // 2