import networkx as nx
from pyformlang.cfg import Production, CFG

def cfg_to_weak_normal_form(cfg: CFG) -> CFG:
    normal_form = cfg.to_normal_form()

    weak = normal_form
    if cfg.generate_epsilon():
        # Add eps word
        start_symbol = normal_form.start_symbol

        cfg_eps = CFG({start_symbol}, None, start_symbol, [Production(start_symbol, [])])
        weak = normal_form.union(cfg_eps)

    return weak

def hellings_based_cfpq(
  cfg: CFG,
  graph: nx.DiGraph,
  start_nodes: set[int] = None,
  final_nodes: set[int] = None,
) -> set[tuple[int, int]]:
   pass