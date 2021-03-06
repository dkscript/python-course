'''
Exercício 1 - Removendo elementos repetidos

Escreva a função remove_repetidos que recebe como parâmetro uma lista 
com números inteiros, verifica se tal lista possui elementos repetidos e os remove. 
A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. 
A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
'''


def remove_repetidos(lista):
    tamanho = len(lista)
    lista = sorted(lista)
    if tamanho <= 2:
        return lista
    else:
        posicao1 = 0
        posicao2 = 1
        valor_posicao1 = lista[posicao1]
        valor_posicao_2 = lista[posicao2]
        limite_p1 = tamanho - 2
        limite_p2 = tamanho - 1
        while posicao1 != limite_p1 and posicao2 != limite_p2:
            
            if valor_posicao1 == valor_posicao_2:
                del(lista[posicao2])
                tamanho = len(lista)
                limite_p1 = tamanho - 2
                limite_p2 = tamanho - 1
                valor_posicao_2 = lista[posicao2]
            else:
                posicao1 += 1
                posicao2 = posicao1 + 1
                valor_posicao1 = lista[posicao1]
                valor_posicao_2 = lista[posicao2]
                
        if valor_posicao1 == valor_posicao_2:
            del (lista[posicao2])

        return lista
    
    
lista = [1,2,1,3,3]

print(remove_repetidos(lista))
