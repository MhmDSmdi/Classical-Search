class State:
    def __init__(self, total_cost, parent_state, action_description, distance=0):
        self.total_cost = total_cost
        self.parent_state = parent_state
        self.action_desc = action_description
        if distance is not 0:
            self.root_distance = distance + 1
        else:
            self.root_distance = 0

    def action_list(self):
        pass

    def equal_state(self, state):
        pass

