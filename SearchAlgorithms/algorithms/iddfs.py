from SearchAlgorithms.algorithms.base_search_algorithm import SearchAlgorithm


class IDDFS_SearchAlgorithm(SearchAlgorithm):
    def search(self, problem):
        initial_state = problem.get_initial_state()
        if problem.is_final_state(initial_state):
            self.final_state = initial_state
            return initial_state
        open_list = [initial_state]
        depth_limit = 1
        current_state = last_state = None
        while True:
            print("depth_limit is {}".format(depth_limit))
            open_list.clear()
            open_list.append(initial_state)
            self.visited_list.append(initial_state)
            current_state = initial_state
            while open_list:
                self.memory_usage = max(self.memory_usage, len(open_list) + len(self.expanded_list))
                s = open_list.pop(0)
                if s.root_distance < depth_limit:
                    for action in s.action_list():
                        next_state = action.next_state
                        if self.is_addable(next_state, open_list):
                            self.visited_list.append(next_state)
                            if problem.is_final_state(next_state):
                                self.final_state = next_state
                                return next_state
                            open_list.insert(0, next_state)
                            current_state = next_state
            if current_state == last_state:
                return None
            else:
                last_state = current_state
            depth_limit += 1


