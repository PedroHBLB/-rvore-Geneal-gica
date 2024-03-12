from aima3.logic import expr, FolKB, fol_fc_ask

clauses = []

# Casal Pedro e Antonia
# 4 filhos - João, Clara, Francisco e Ana
# Ana
# 2 filhas - Helena e Joana
# João
# 1 filho - Mário
# Casal Helena e Mário
# 1 filho - Carlos
# Casal Francisco e Milene
# 0 filhos
# Clara
# 2 filhos - Pietro e Enzo
# Casal Pietro e Francisca
# Casal Enzo e Antonia

clauses.append(expr("Sexo(Clara, Feminino)"))
clauses.append(expr("Sexo(Antonia, Feminino)"))
clauses.append(expr("Sexo(Ana, Feminino)"))
clauses.append(expr("Sexo(Helena, Feminino)"))
clauses.append(expr("Sexo(Joana, Feminino)"))
clauses.append(expr("Sexo(Milene, Feminino)"))
clauses.append(expr("Sexo(Francisca, Feminino)"))
clauses.append(expr("Sexo(Pedro, Masculino)"))
clauses.append(expr("Progenitor(Pedro, Antonia)"))
clauses.append(expr("Progenitor(x,y) ==> Pessoa(x)"))
clauses.append(expr("Progenitor(x,y) ==> Pessoa(y)"))
clauses.append(expr("Irmandade(Pedro,Antonia) & Sexo(x, Masculino) ==> Pessoa(João, Francisco)"))
clauses.append(expr("Irmandade(Pedro,Antonia) & Sexo(y, Feminino) ==> Pessoa(Clara, Ana)"))
clauses.append(expr("Progenitor(x,y) & Sexo(x, Feminino) ==> Mae(x,y)"))

Genealogia = FolKB(clauses)

perguntas = [
    "Sexo(x, Feminino)",
    "Sexo(Pedro, x)",
    "Progenitor(x, Antonia)",
    "Irmandade(Pedro, Antonia) & Sexo(y, Feminino)"
]

for i in perguntas:
    resposta = fol_fc_ask(Genealogia, expr(i))
    print("%s -> %s" %(i, (list(resposta))))
