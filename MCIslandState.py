from MCState import MCState 

class MCIslandState(MCState):
    def __init__(self, m_left, c_left, boat_side, total_m, total_c, m_island=0, c_island=0):
        super().__init__(m_left, c_left, boat_side, total_m, total_c)
        self.m_island = m_island
        self.c_island = c_island

    def get_neighbors(self):
        moves = [(1,0), (0,1), (1,1), (2,0), (0,2)]
        neighbors = []
        for m, c in moves:
            if self.boat_side == 'L':
                if m <= self.m_left and c <= self.c_left:
                    new = MCIslandState(
                        self.m_left - m, self.c_left - c, 'I',
                        self.total_m, self.total_c,
                        self.m_island + m, self.c_island + c
                    )
                    if new.is_valid():
                        neighbors.append((new, 1))
            elif self.boat_side == 'I':
                # I -> L
                if m <= self.m_island and c <= self.c_island:
                    newL = MCIslandState(
                        self.m_left + m, self.c_left + c, 'L',
                        self.total_m, self.total_c,
                        self.m_island - m, self.c_island - c
                    )
                    if newL.is_valid():
                        neighbors.append((newL, 1))
                # I -> R
                if m <= self.m_island and c <= self.c_island:
                    newR = MCIslandState(
                        self.m_left, self.c_left, 'R',
                        self.total_m, self.total_c,
                        self.m_island - m, self.c_island - c
                    )
                    if newR.is_valid():
                        neighbors.append((newR, 1))
            elif self.boat_side == 'R':
                m_r = self.total_m - self.m_left - self.m_island
                c_r = self.total_c - self.c_left - self.c_island
                if m <= m_r and c <= c_r:
                    new = MCIslandState(
                        self.m_left, self.c_left, 'I',
                        self.total_m, self.total_c,
                        self.m_island + m, self.c_island + c
                    )
                    if new.is_valid():
                        neighbors.append((new, 1))
        return neighbors

    def is_valid(self):
        parts = [
            (self.m_left, self.c_left),
            (self.m_island, self.c_island),
            (self.total_m - self.m_left - self.m_island,
             self.total_c - self.c_left - self.c_island)
        ]
        for m, c in parts:
            if m < 0 or c < 0:
                return False
            if m > 0 and c > m:
                return False
        return True

    def __hash__(self):
        return hash((self.m_left, self.c_left, self.m_island, self.c_island, self.boat_side))

    def __eq__(self, other):
        return (self.m_left == other.m_left and
                self.c_left == other.c_left and
                self.m_island == other.m_island and
                self.c_island == other.c_island and
                self.boat_side == other.boat_side)

    def get_state_str(self):
        m_r = self.total_m - self.m_left - self.m_island
        c_r = self.total_c - self.c_left - self.c_island
        return (f"L:{self.m_left}M{self.c_left}C "
                f"I:{self.m_island}M{self.c_island}C "
                f"R:{m_r}M{c_r}C "
                f"{self.boat_side}")
