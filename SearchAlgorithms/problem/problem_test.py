from SearchAlgorithms.problem.base_problem import Problem
from SearchAlgorithms.graph.state import State
from SearchAlgorithms.graph.action import Action
from SearchAlgorithms.algorithms.dls import DLS_Search
from SearchAlgorithms.algorithms.bfs import BFS_Search


class Problem_test(Problem):

    def get_initial_state(self):
        return ProblemState(1, None, 0)

    def is_final_state(self, state):
        return state.state_name == 6

    def get_final_states(self):
        return ProblemState(6)


class ProblemState(State):
    def __init__(self, name, parent, distance, total_cost=0, action_description=""):
        super().__init__(state_name=name, total_cost=total_cost, parent_state=parent,
                         action_description=action_description, distance=distance)
        self.state_name = name
        self.parent_state = parent
        pass

    def action_list(self):
        action_list = []
        if self.state_name is 1:
            action_list.append(Action(ProblemState(2, self, 1)))
            action_list.append(Action(ProblemState(3, self, 1)))
        elif self.state_name is 2:
            action_list.append(Action(ProblemState(4, self, 1)))
            action_list.append(Action(ProblemState(7, self, 1)))
        elif self.state_name is 3:
            action_list.append(Action(ProblemState(4, self, 1)))
            action_list.append(Action(ProblemState(5, self, 1)))
        elif self.state_name is 4:
            action_list.append(Action(ProblemState(6, self, 1)))
            action_list.append(Action(ProblemState(7, self, 1)))
        elif self.state_name is 5:
            action_list.append(Action(ProblemState(6, self, 1)))

        return action_list

    def equal_state(self, state):
        if self.state_name is state.state_name:
            return True
        else:
            return False


if __name__ == '__main__':
    test = Problem_test()
    search_algo = DLS_Search(3).set_graph_search()
    search_algo.search(test)

    for i in search_algo.get_best_path():
        print(i)
