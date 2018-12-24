from SearchAlgorithms.problem.base_problem import Problem
from SearchAlgorithms.graph.state import State
from SearchAlgorithms.graph.action import Action
from SearchAlgorithms.algorithms.a_star import A_Star
from SearchAlgorithms.algorithms.iddfs import IDDFS_SearchAlgorithm


class Problem_test(Problem):

    def get_initial_state(self):
        return ProblemState(1, None, 0)

    def is_final_state(self, state):
        return state.state_name == 6

    def get_final_states(self):
        return ProblemState(6)

    def heuristic_cost(self, state):
        return 0


class ProblemState(State):
    def __init__(self, name, parent, distance=1, total_cost=0, action_description=""):
        super().__init__(state_name=name, total_cost=total_cost, parent_state=parent,
                         action_description=action_description, distance=distance)
        self.state_name = name
        self.parent_state = parent
        pass

    def action_list(self):
        action_list = []
        if self.state_name is 1:
            action_list.append(Action(ProblemState(name=2, parent=self)))
            action_list.append(Action(ProblemState(name=3, parent=self)))
        elif self.state_name is 2:
            action_list.append(Action(ProblemState(name=4, parent=self)))
            action_list.append(Action(ProblemState(name=7, parent=self)))
        elif self.state_name is 3:
            action_list.append(Action(ProblemState(name=4, parent=self)))
            action_list.append(Action(ProblemState(name=5, parent=self)))
        elif self.state_name is 4:
            action_list.append(Action(ProblemState(name=6, parent=self)))
            action_list.append(Action(ProblemState(name=7, parent=self)))
        elif self.state_name is 5:
            action_list.append(Action(ProblemState(name=6, parent=self)))

        return action_list

    def equal_state(self, state):
        if self.state_name is state.state_name:
            return True
        else:
            return False


if __name__ == '__main__':
    test = Problem_test()
    search_algo = A_Star().set_graph_search()
    search_algo.search(test)

    for i in search_algo.get_best_path():
        print(i)
