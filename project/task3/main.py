from pyformlang.finite_automaton import NondeterministicFiniteAutomaton


class AdjacencyMatrixFA:

    def __init__(self, automata: NondeterministicFiniteAutomaton):
        self._index_to_state, self._state_to_index = self._numerate_states(automata)
        self.matrices = self._init_adjacency_matrices(automata)

    def print_adjacency_matrix(self):
        for label in self.matrices:
            print(label, ":")
            print(
                "\n".join(
                    [
                        "\t".join([str(cell) for cell in row])
                        for row in self.matrices[label]
                    ]
                )
            )
            print()

    def _get_state_by_index(self, num: int):
        return self._index_to_state[num]

    def _get_index_by_state(self, state: str):
        return self._state_to_index[state]

    def _numerate_states(self, automata: NondeterministicFiniteAutomaton):
        index_to_state = dict()
        state_to_index = dict()

        for idx, x in enumerate(automata.states):
            index_to_state[idx] = x
            state_to_index[x] = idx

        return (index_to_state, state_to_index)

    def _init_adjacency_matrices(self, automata: NondeterministicFiniteAutomaton):
        matrices = dict()
        for sym in automata.symbols:
            matrices[sym] = [
                [False for _ in range(automata.__len__())]
                for _ in range(automata.__len__())
            ]

        for x in automata:
            start, label, end = x
            i, j = self._get_index_by_state(start), self._get_index_by_state(end)
            matrices[label][i][j] = True

        return matrices
