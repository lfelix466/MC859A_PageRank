from rdflib import Graph
import networkx as nx

def nt_to_gexf(input_file, output_file):
    # Carregar o grafo RDF
    rdf_graph = Graph()
    rdf_graph.parse(input_file, format="nt")

    # Criar um grafo NetworkX
    G = nx.DiGraph()

    # Percorrer as triplas (sujeito, predicado, objeto)
    for subj, pred, obj in rdf_graph:
        s = str(subj)
        p = str(pred)
        o = str(obj)

        # Adicionar nós e arestas
        G.add_node(s)
        G.add_node(o)
        G.add_edge(s, o, label=p)

    # Exportar para GEXF
    nx.write_gexf(G, output_file)
    print(f"Arquivo convertido salvo em: {output_file}")

# Exemplo de uso
nt_to_gexf("rede_intelectual_reduzida.nt", "grafo.gexf")