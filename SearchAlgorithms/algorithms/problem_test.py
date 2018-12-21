from SearchAlgorithms.algorithms.base_problem import Problem
from SearchAlgorithms.graph.state import State
from SearchAlgorithms.graph.action import Action
from SearchAlgorithms.algorithms.bfs import BFS_SEARCH


class Problem_test(Problem):

    def get_initial_state(self):
        return ProblemState(1)

    def is_final_state(self, state):
        return state.state_name == 5

    def get_final_states(self):
        return ProblemState(6)


class ProblemState(State):
    def __init__(self, name, parent=None):
        self.state_name = name
        self.parent_state = parent
        pass

    def action_list(self):
        action_list = []
        if self.state_name is 1:
            action_list.append(Action(ProblemState(2, self)))
            action_list.append(Action(ProblemState(3, self)))
        elif self.state_name is 2:
            action_list.append(Action(ProblemState(4, self)))
            action_list.append(Action(ProblemState(7, self)))
        elif self.state_name is 3:
            action_list.append(Action(ProblemState(4, self)))
            action_list.append(Action(ProblemState(5, self)))
        elif self.state_name is 4:
            action_list.append(Action(ProblemState(6, self)))
            action_list.append(Action(ProblemState(7, self)))
        elif self.state_name is 5:
            action_list.append(Action(ProblemState(6, self)))

        return action_list

    def equal_state(self, state):
        if self.state_name is state.state_name:
            return True
        else:
            return False


if __name__ == '__main__':
    test = Problem_test()
    search_algo = BFS_SEARCH().set_graph_search()
    search_algo.search(test)

    for i in search_algo.get_best_path():
        print(i)
