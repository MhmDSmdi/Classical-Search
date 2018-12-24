from SearchAlgorithms.algorithms.base_search_algorithm import SearchAlgorithm


def get_best_state(open_list):
    import math
    min_int = math.inf
    best_state = None
    for s in open_list:
        total_cost = s.total_cost
        if total_cost < min_int:
            min_int = total_cost
            best_state = s
    return best_state


class Uniform_Cost(SearchAlgorithm):
    def search(self, problem):
        initial_state = problem.get_initial_state()
        if problem.is_final_state(initial_state):
            return initial_state

        open_list = [initial_state]
        self.visited_list.append(initial_state)

        while open_list:
            self.memory_usage = max(self.memory_usage, len(open_list) + len(self.expanded_list))
            s = get_best_state(open_list)
            open_list.remove(s)
            if problem.is_final_state(s):
                self.final_state = s
                return s
            self.expanded_list.append(s)
            for action in s.action_list():
                next_state = action.next_state
                if self.is_addable(next_state, open_list):
                    self.visited_list.append(next_state)
                    open_list.insert(0, next_state)
        return None
