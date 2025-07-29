class MCState:
    def __init__(self, m_left, c_left, boat_side, total_m, total_c):
        self.m_left = m_left
        self.c_left = c_left
        self.boat_side = boat_side  # 'L' or 'R'
        self.total_m = total_m
        self.total_c = total_c

    def get_neighbors(self):
        moves = [(1,0), (0,1), (1,1), (2,0), (0,2)]
        neighbors = []
        for m, c in moves:
            if self.boat_side == 'L':
                new_state = MCState(self.m_left - m, self.c_left - c, 'R',
                                    self.total_m, self.total_c)
            else:
                new_state = MCState(self.m_left + m, self.c_left + c, 'L',
                                    self.total_m, self.total_c)
            if new_state.is_valid():
                neighbors.append((new_state, 1))  # cost = 1 per crossing
        return neighbors

    def is_valid(self):
        m_right = self.total_m - self.m_left
        c_right = self.total_c - self.c_left
        if not (0 <= self.m_left <= self.total_m and 0 <= self.c_left <= self.total_c):
            return False
        if not (0 <= m_right <= self.total_m and 0 <= c_right <= self.total_c):
            return False
        if self.m_left > 0 and self.m_left < self.c_left:
            return False
        if m_right > 0 and m_right < c_right:
            return False
        return True

    def __hash__(self):
        return hash((self.m_left, self.c_left, self.boat_side))

    def __eq__(self, other):
        return (self.m_left == other.m_left and
                self.c_left == other.c_left and
                self.boat_side == other.boat_side)

    def get_state_str(self):
        return f"{self.m_left}M {self.c_left}C {self.boat_side}"
