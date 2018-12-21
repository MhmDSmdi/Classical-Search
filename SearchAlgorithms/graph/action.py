class Action:
    def __init__(self, next_state, action_cost=1):
        self.action_cost = action_cost
        self.next_state = next_state

    def __iter__(self):
        return self;

    def get_cost(self):
        return self.action_cost
    def get_next_stae(self):
        return self.next_state