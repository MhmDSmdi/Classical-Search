class Action:
    def __init__(self, action_cost, next_state):
        self.action_cost = action_cost
        self.next_state = next_state
    def get_cost(self):
        return self.action_cost
    def get_next_stae(self):
        return self.next_state