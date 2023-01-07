#==================================================
#Programa: Análise de pareto
#Programador: Ramon Cintas Gomes
#==================================================

dados = open("Arquivo.txt","r")
dados_brutos = dados.readlines()

L1=[] # lista bruta 
L2=[] # lista sem duplicata
L3=[] # lista com nr ocorrencia
L4=[] # lista de frequência %
L5=[] # lista ordenada por ordem decrescente
L6=[] # lista de frequência acumulada %
L7=[] # lista para formatar a frequência acumulada % em string de porcentagem
L8=[] # lista para juntar todas as listas
L9=[] # lista para printar os tipos de defeitos e a quantidade de Ocorrências

contTotal = 0 # variável para o total de número de Ocorrências
contTotalF = 0 # variável para o total de frequência %
contTotalA = 0 # variável para a frequência acumulada

for i in dados_brutos: # percorre a lista para retirar caracteres especiais e conta o total de ocorrencias
        L1.append(i.rstrip())
        contTotal = contTotal + 1
 
for i in L1: # Percorre a lista para remover as duplicatas
    if i not in L2:
        L2.append(i)

for i in L2:
    L3.append(L1.count(i)) # Percorre a lsita para contar o número de ocorrencias de cada tipo

for i in range(0,len(L3)): # Adiciona na lista l9 os dados da lista l2 e l3 que são tipo de defeito e nr ocorrencias
    L9.append([L2[i],L3[i]])

List_Ord=sorted(L9,key=lambda l:l[1], reverse=True) # cria uma lista ordenada com tipo de defeito e nr ocorrencia

L3.sort(reverse = True) # organiza a lista de nr ocorrencia para fazer os calculos de forma correta

for i in range(0,len(L2)): # percorre a lista l2
    L4.append((L3[i] / contTotal)) # adiciona cada item da lista l3 dividido pelo total de ocorrencias para encontrar a frequencia
    L5.append("{:.2%}".format(L4[i])) # formata os dados da l4 para printar de forma mais clara para o melhor entendimento
    contTotalA = contTotalA + L4[i] # #acumula a frequencia para formar a frequencia acumulada
    L6.append([contTotalA]) #adiciona o total da frequencia acumulada na l6
    L7.append("{:.2%}".format(contTotalA)) # formata a frequencia acumulada para printar de forma mais clara para o melhor entendimento
    
contTotalF = sum(L4) # aqui é a soma de todas as frequencias para obter o total das frequencias

for i in range(0,len(L3)): # percorre a lista l3
    L8.append([L5[i],L7[i]])# aqui é onde é adicionado na lista l8 a lista de frequencia normal e acumulada

def criarTabela(): # aqui é onde a tabela é criada e printa na tela
    print("\n---------------------------------------------------------------------------")
    print("|Tipo de dado|-|Nr Ocorrências|-|Frequência(%)|-|Frequência Acumulada|")
    print("---------------------------------------------------------------------------")
    for i in range(0,len(L8)):
        print("------------------->|=|",(List_Ord[i],L8[i]))
    print("------------------->|=| Total de NR Ocorrências:",contTotal)
    print("------------------->|=| Total de frequência (%):","{:.2%}".format(contTotalF))
    print("------------------->|=| Total de frequência acumulada (%):","{:.2%}".format(contTotalA))
    print("---------------------------------------------------------------------------")
    print("|Programa: Análise de pareto.\n|Programador: Ramon Cintas Gomes.")
    print("---------------------------------------------------------------------------")
criarTabela()
