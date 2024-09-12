from typing import Set

from networkx import MultiDiGraph
from pyformlang.finite_automaton import EpsilonNFA, NondeterministicFiniteAutomaton
from pyformlang.regular_expression import Regex
from pyformlang.finite_automaton import DeterministicFiniteAutomaton
from pyformlang.finite_automaton import State


def regex_to_dfa(regex: str) -> DeterministicFiniteAutomaton:
    epsilon_nfa: EpsilonNFA = Regex(regex).to_epsilon_nfa()
    dfa: DeterministicFiniteAutomaton = epsilon_nfa.to_deterministic()
    return dfa


def graph_to_nfa(
        graph: MultiDiGraph, start_states: Set[int], final_states: Set[int]
) -> NondeterministicFiniteAutomaton:
    nfa: NondeterministicFiniteAutomaton = (
        NondeterministicFiniteAutomaton.from_networkx(graph).remove_epsilon_transitions())

    [nfa.add_start_state(State(node)) for node in start_states]
    [nfa.add_final_state(State(node)) for node in final_states]

    return nfa
