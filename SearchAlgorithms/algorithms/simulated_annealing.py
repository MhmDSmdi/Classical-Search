from SearchAlgorithms.algorithms.base_search_algorithm import SearchAlgorithm
import random
import math


def random_neighbors(state):
    if len(state.action_list()) is not 0:
        rand_index = random.randint(0, len(state.action_list()) - 1)
        return state.action_list()[rand_index].next_state
    return state


class SimulatedAnnealing(SearchAlgorithm):
    def __init__(self, cost_func):
        super().__init__()
        self.cost_func = cost_func
        self.T = 1
        self.T_min = 0.0001

    def search(self, problem):
        initial_state = problem.get_initial_state()
        if problem.is_final_state(initial_state):
            self.final_state = initial_state
            print(initial_state)
            return initial_state
        self.visited_list.append(initial_state)
        s = initial_state

        while self.T > self.T_min:
            self.memory_usage = max(self.memory_usage, len(self.expanded_list))
            self.expanded_list.append(s)
            new_state = random_neighbors(s)
            old_cost = self.cost_func(s)
            new_cost = self.cost_func(new_state)
            a = self.acceptance_probability(old_cost, new_cost)
            if a > random.uniform(0, 1):
                self.visited_list.append(new_state)
                if problem.is_final_state(new_state):
                    self.final_state = new_state
                    print(new_state)
                    return new_state
                s = new_state
            # self.T = self.T * 0.9
        return None

    def acceptance_probability(self, old_cost, new_cost):
        return math.pow(math.e, ((new_cost - old_cost) / self.T))
