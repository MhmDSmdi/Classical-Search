from SearchAlgorithms.algorithms.base_search_algorithm import AlgorithmSearch


class DLS_Search(AlgorithmSearch):
    def __init__(self, limited_depth):
        super().__init__()
        self.limited_depth = limited_depth

    def search(self, problem):
        initial_state = problem.get_initial_state()
        if problem.is_final_state(initial_state):
            return initial_state

        open_list = [initial_state]
        self.visited_list.append(initial_state)

        while open_list:
            self.memory_usage = max(self.memory_usage, len(self.expanded_list) + len(open_list))
            s = open_list.pop(0)
            # print(s.root_distance)
            # print(self.limited_depth)
            if s.root_distance < self.limited_depth:
                self.expanded_list.append(s)
                for action in s.action_list():
                    next_state = action.next_state
                    if self.is_addable(next_state, open_list):
                        self.visited_list.append(next_state)
                        if problem.is_final_state(next_state):
                            self.final_state = next_state
                            return next_state
                        open_list.insert(0, next_state)
            else:
                print("Can't access to final state using limited_depth={}".format(self.limited_depth))
                exit(0)
        return None
