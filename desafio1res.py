#Desenvolva um programa em Python que apure o resultado de uma votação para determinar o personagem favorito do desenho “The Simpsons”. Suponha que existam 2 candidatos cujos códigos são:
#
#1 - Bart
#2 - Homer
# 
#Considere que existe uma função que recebe e escreve em um arquivo .txt ou em uma lista/vetor os votos de 5 pessoas. Um voto é representado pelo #código de identificação do candidato.
#
#Na sequência, uma função para leitura deverá ser implementada, a qual deverá apresentar, como resultado:
#
#    o nome e a quantidade de votos do candidato mais votado
#    o nome e a quantidade de votos do menos votado
#    quantidade de votos nulos (um voto nulo é um voto cujo código de identificação é um valor diferente de 1 e 2). 

def registrar_votos(votos):
    for i in range(5):
        voto = int(input(f"Digite seu voto (1 para Bart, 2 para Homer: "))
        votos.append(voto)

def apurar_resultado(votos):
    total_bart = 0
    total_homer = 0
    votos_nulos = 0

    for voto in votos:
        if voto == 1:
            total_bart +=1
        elif voto == 2:
            total_homer += 1
        else:
            votos_nulos += 1
    
    if total_bart > total_homer:
        mais_votado = "Bart"
        votos_mais_votado = total_bart
        menos_votado = "Homer"
        votos_menos_votado = total_homer
    else:
        mais_votado = "Homer"
        votos_mais_votado = total_homer
        menos_votado = "Bart"
        votos_menos_votado = total_bart
    
    return (mais_votado, votos_mais_votado, menos_votado, votos_menos_votado, votos_nulos)

votos = []
registrar_votos(votos)

mais_votado, votos_mais_votado, menos_votado, votos_menos_votado, nulos = apurar_resultado(votos)

print(f"Candidato mais votado: {mais_votado} com {votos_mais_votado} votos")
print(f"Candidato menos votado: {menos_votado} com {votos_menos_votado} votos")
print(f"Votos nulos: {nulos}")