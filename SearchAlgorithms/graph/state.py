class State:
    def __init__(self, state_name, total_cost, parent_state, action_description, distance):
        self.total_cost = total_cost
        self.parent_state = parent_state
        self.action_desc = action_description
        self.state_name = state_name
        if distance is not 0:
            self.root_distance = distance + 1
        else:
            self.root_distance = 0

    def __str__(self):
        return "State {}".format(self.state_name)

    def __iter__(self):
        return self

    def action_list(self):
        pass

    def equal_state(self, state):
        pass
