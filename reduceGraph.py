from rdflib import Graph, URIRef

# Filtro mais agressivo: mantemos apenas as relações de influência / orientação intelectual.
# Isso reduz fortemente o arquivo mantendo o núcleo semântico da rede de conhecimento.
KEEP_PREDICATES = {
    "http://dbpedia.org/ontology/influencedBy",
    "http://dbpedia.org/ontology/influenced",
    "http://dbpedia.org/ontology/doctoralAdvisor",
    "http://dbpedia.org/ontology/doctoralStudent",
    "http://dbpedia.org/ontology/academicAdvisor",
    "http://dbpedia.org/ontology/academicStudent"
}


def reduzir_nt(input_file, output_file):
    g = Graph()
    g.parse(input_file, format="nt")

    total = len(g)
    out = Graph()
    kept = 0

    for s, p, o in g:
        if str(p) in KEEP_PREDICATES and isinstance(o, URIRef):
            out.add((s, p, o))
            kept += 1

    out.serialize(destination=output_file, format="nt")
    print(f"Total de triplas originais: {total}")
    print(f"Triplas preservadas: {kept}")
    print(f"Redução final: {100 * kept / total:.1f}% do original")
    print(f"Arquivo reduzido salvo em: {output_file}")


if __name__ == "__main__":
    reduzir_nt("rede_intelectual.nt", "rede_intelectual_reduzida.nt")
