#!/usr/bin/env python3
"""Exibe relatorio de criancas por atividades.

Imprimir a lista de criancas agrupadas por sala que frequenta cada uma
das atividades.
"""
__version__ = "0.1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Listar alunos em cada atividade por sala
atividades = [("Ingles",aula_ingles),("Musica",aula_musica),("Danca",aula_danca)]

for nome_atv,atividade in atividades:
    print("Atividade: ", nome_atv)
    #print(nome_atv,atividade)
    atv_sala1=[]
    atv_sala2=[]
    for aluno in atividade:
        if aluno in sala1:
            atv_sala1.append(aluno)
        else:
            atv_sala2.append(aluno)
    print("Sala1 ", atv_sala1)
    print("Sala2 ", atv_sala2)
    print("#" * 40)










# atividades = [("Ingles",aula_ingles),
              # ("Musica", aula_musica),
              # ("Danca", aula_danca)]
# 
# for nome_atividade, atividade in atividades:
    # print(f"Alunos da atividade {nome_atividade}")
    # print("-" * 40)
    # atividade_sala1 = []
    # atividade_sala2 = []
# 
    # for aluno in atividade:
        # if aluno in sala1:
            # atividade_sala1.append(aluno)
        # else:
            # atividade_sala2.append(aluno)
    # print("Sala1 ", atividade_sala1)
    # print("Sala2 ", atividade_sala2)
    # print()
    # print("#" * 40)

    
            
