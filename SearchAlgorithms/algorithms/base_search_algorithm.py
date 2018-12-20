class AlgorithmSearch:
    def __init__(self, is_graph_search=True):
        self.is_graph_search = is_graph_search
        self.visited_set = {}
        self.expanded_set = {}
        self.memory_usage = 0
        self.final_state = None

    def is_addable(self, state, open_set):
        for s in open_set:
            if s is state:
                return False

        if self.is_graph_search:
            for s in self.expanded_set:
                if s is state:
                    return False

        return True

    def search(self, problem):
        pass

    def run(self, problem):
        self.visited_set.clear()
        self.expanded_set.clear()
        self.final_state = self.search()
        if self.final_state is None:
            print("Access to final state impossible!")

    def get_best_path(self):
        if self.final_state is None:
            return None
        path = []
        state = self.final_state
        while state.parent_state is not None:
            path.append(state)
            state = state.parent_state
        return path

    def get_best_path_cost(self):
        if self.final_state is not None:
            return self.final_state.total_cost
        else:
            return None

    def get_final_state(self):
        return self.final_state

    def get_max_memory_usage(self):
        return self.memory_usage

    def visited_set_size(self):
        return len(self.visited_set)

    def expanded_set_size(self):
        return len(self.expanded_set)

