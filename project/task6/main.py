import networkx as nx
from autopep8 import Tuple
from networkx.classes import MultiDiGraph
from pyformlang.cfg import Production, CFG, Epsilon

from tests.autotests.constants import LABEL


def cfg_to_weak_normal_form(cfg: CFG) -> CFG:
    normal_form = cfg.to_normal_form()

    weak = normal_form
    if cfg.generate_epsilon():
        # Add eps word
        start_symbol = normal_form.start_symbol

        cfg_eps = CFG(
            {start_symbol}, None, start_symbol, [Production(start_symbol, [])]
        )
        weak = normal_form.union(cfg_eps)

    return weak


def hellings_based_cfpq(
    cfg: CFG,
    graph: nx.DiGraph,
    start_nodes: set[int] = None,
    final_nodes: set[int] = None,
) -> set[tuple[int, int]]:
    def get_edge_label(first: int, second: int) -> str | None:
        edge = graph.get_edge_data(first, second)
        if edge:
            return edge[0]["label"]

        return None

    weak = cfg_to_weak_normal_form(cfg)

    r = list()
    for first in list(graph):
        for second in list(graph):
            for production in weak.productions:
                if first == second and Epsilon in production.body:
                    r.append((production.head, first, first))

                label = get_edge_label(first, second)
                if len(production.body) == 1 and production.body[0].value == label:
                    r.append((production.head, first, second))

    new = r.copy()
    while new:
        (N, n, m) = new.pop(0)
        for (M, k, p) in r:
            for production in weak.productions:
                if p == n and len(production.body) == 2 and production.body[0].value == M and production.body[1] == N:
                    if (production.head, k, m) not in r:
                        new.append((production.head, k, m))
                    if (production.head, k, m) not in r:
                        r.append((production.head, k, m))

        for (M, k, p) in r:
            for production in weak.productions:
                if k == m and len(production.body) == 2 and production.body[0].value == N and production.body[1] == M:
                    if (production.head, m, p) not in r:
                        new.append((production.head, m, p))
                    if (production.head, m, p) not in r:
                        r.append((production.head, m, p))

    resultt = set()
    for (N, f, s) in r:
        if f in start_nodes and s in final_nodes:
            resultt.add((f, s))

    return resultt