# Importando leitor de instâncias
from leitor_instancias import Leitor

# Lendo arquivo com as instâncias
x, y, d, q, e, l, t, n, Cap = Leitor('AA25').dados_instancia


# Criando variáveis com valores atualizados a cada inserção

# Pedidos não atendidos
L = list(range(1,n+1))

# Solução com as rotas -> Inicia-se com uma única rota vazia com os nós do depósito central, para poder iterar desde a primeira iteração
S = [ [0, 2*n + 1] ]

# Capacidade do veículo na roda
Cap_atual = 0

# Tempo atual da rota
Tempo_atual = 0

# Quantidade de requests atendidos
qtd_atendidos = 0

# Custo total da solução
FO = 0

# Enquanto todos os pedidos não tiverem sido atendidos
while qtd_atendidos < n:

    # O número do pedido a ser inserido nas rotas é simplesmente o primeiro daqueles que ainda não foram atendidos
    request = L[0]

    # Índice do nó de pickup correspondente ao request
    no_pickup = request

    # Índice do nó de delivery correspondente ao request
    no_delivery = request + n

    # Para cada rota da solução (rotas criadas paralelamente)
    for rota in S:

        # considerando que um nó de delivery pode ser no mínimo inserido na segunda (1) posição e no máximo na última
        for pos_insercao_no_delivery in range(1, len(rota) + 1):

            # considerando que um nó de pickup pode ser no mínimo inserido na primeira (0) posição e no máximo na penúltima
            for pos_insercao_no_pickup in range(0, len(rota)):


                print('Hello world!')
                # Variação da função objetivo pela inserção dos nós x_request e y_request nas posições da iteração
                #delta = (t[rota[pos_insercao_no_pickup]][no_pickup] + t[no_pickup][rota[pos_insercao_no_pickup+1]] - t[rota[pos_insercao_no_pickup]][rota[pos_insercao_no_pickup]+1]) + (t[rota[pos_insercao_no_delivery]][no_delivery] + t[no_delivery][rota[pos_insercao_no_delivery+1]] - t[rota[pos_insercao_no_delivery]][rota[pos_insercao_no_delivery]+1])
                #print(delta)








