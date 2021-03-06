# Importando leitor de instâncias
from leitor_instancias import Leitor

import numpy as np

# Lendo arquivo com as instâncias
x, y, d, q, e, l, t, n, Cap = Leitor('AA3_toy').dados_instancia

# Criando variáveis com valores atualizados a cada inserção

# Pedidos não atendidos
L = list(range(1,n+1))

# Solução com as rotas -> Inicia-se com uma única rota vazia com os nós do depósito central, para poder iterar desde a primeira iteração
S = [ [0, 2*n + 1] ]

# Quantidade de requests atendidos
qtd_atendidos = 0

# Custo total da solução
FO = 0

# Enquanto todos os pedidos não tiverem sido atendidos
while qtd_atendidos < n:

    # O número do pedido a ser inserido nas rotas é simplesmente o primeiro daqueles que ainda não foram atendidos -> há alguma forma melhor de ordenar?
    request = L[0]

    # Índice do nó de pickup correspondente ao request
    no_pickup = request

    # Índice do nó de delivery correspondente ao request
    no_delivery = request + n

    # Variável que guardará o delta mínimo de incremento da função objetivo para cada rota com nova inserção
    deltas_minimos = []

    # Variável que guardará a rota correspondente ao delta mínimo para cada rota da solução
    rotas_delta_minimo = []

    # Variável que controlará o número de rotas factíveis encontradas
    num_rotas_factiveis = 0

    # Para cada rota da solução, serão testadas todas as posições de inserção possíveis (rotas criadas paralelamente)
    for rota in S:

        # Variável para controlar o delta mínimo para cada rota (variações no valor da função objetivo dados pela inserção de um novo request na rota)
        delta_minimo = 10e5

        # Variável que guardará a rota com delta mínimo gerada na iteração pelas inserções
        rota_delta_minimo = []

        for pos_insercao_no_pickup in range(1, len(rota) + 1):

            for pos_insercao_no_delivery in range(1, len(rota) + 1):

                # Testando apenas índices de inserção válidos: índice de delivery maior do que o de pickup (precedence) e diferente dele!
                # A iteração começa em 1 e termina no tamanho da rota porque não se considera a primeira e última posição da rota, que são o depósito
                if (pos_insercao_no_pickup != pos_insercao_no_delivery) and (pos_insercao_no_pickup < pos_insercao_no_delivery):

                    # Rota testada para a inserção
                    rota_teste = rota.copy()

                    # Inserindo nós na rota, nas posições da iteração
                    rota_teste.insert(pos_insercao_no_pickup, no_pickup)
                    rota_teste.insert(pos_insercao_no_delivery, no_delivery)

                    # Checando factibilidade da rota
                    # *OBS: não é necessário testar pairing e precedence, porque os pedidos são inseridos em pares nas rotas e a inserção já assegura precedência

                    # Variável booleana, que controla a factibilidade
                    factivel = True

                    # Capacidade atual do veículo na rota (inicia como 0)
                    cap_atual = 0

                    # Tempo atual da rota (inicia como 0)
                    t_atual = 0

                    # Para cada nó da rota teste
                    for index in range(1, len(rota_teste)):

                        no_atual = rota_teste[index - 1]
                        no_seguinte = rota_teste[index]

                        # Checando se ir para o nó seguinte irá violar as restrições de capacidade e time window
                        if (cap_atual + q[no_seguinte] > Cap) or (l[no_seguinte] < t_atual + t[no_atual][no_seguinte]):

                            # Atribuindo valor falso para a variável de factibilidade e quebrando o laço for
                            factivel = False
                            break

                        else:
                            # Atualizando valores

                            # Capacidade
                            cap_atual += q[no_seguinte]

                            # Tempo
                            # Caso haja adiantamento (tempo de chegada menor que a janela de tempo de abertura)
                            if (t_atual + t[no_atual][no_seguinte]) < e[no_seguinte]:

                                t_atual = e[no_seguinte]

                            else:

                                t_atual += t[no_atual][no_seguinte]

                    # Caso a solução seja factível, calcula-se o delta
                    if factivel:

                        # Incrementando variável de número de rotas factíveis
                        num_rotas_factiveis += 1

                        # Variação da função objetivo pela inserção dos nós nas posições da iteração

                        delta_pickup = (t[rota_teste[pos_insercao_no_pickup - 1]][rota_teste[pos_insercao_no_pickup]] + t[rota_teste[pos_insercao_no_pickup]][rota_teste[pos_insercao_no_pickup + 1]] - t[rota_teste[pos_insercao_no_pickup - 1]][rota_teste[pos_insercao_no_pickup + 1]])
                        delta_delivery = (t[rota_teste[pos_insercao_no_delivery - 1]][rota_teste[pos_insercao_no_delivery]] + t[rota_teste[pos_insercao_no_delivery]][rota_teste[pos_insercao_no_delivery + 1]] - t[rota_teste[pos_insercao_no_delivery - 1]][rota_teste[pos_insercao_no_delivery + 1]])

                        delta = delta_pickup + delta_delivery

                        # Se o delta for menor que o delta mínimo já registrado, atualizam-se os valores de delta mínimo e a rota correspondente
                        if delta < delta_minimo:
                            delta_minimo = delta
                            rota_delta_minimo = rota_teste.copy()

                    # Caso contrário, passa-se para a próxima posição de inserção da iteração
                    else:

                        pass

        # Guardando valores de delta mínimo e rota correspondente
        deltas_minimos.append(delta_minimo)
        rotas_delta_minimo.append(rota_delta_minimo)

    # Checando qual rota da iteração teve o menor incremento na função objetivo

    indice_rota_delta_minimo = np.argmin(deltas_minimos)
    rota_delta_minimo = rotas_delta_minimo[indice_rota_delta_minimo]

    # Caso tenha sido encontrada ao menos uma posição de inserção factível
    if num_rotas_factiveis > 0:

        # Atribuindo rota para a solução
        S[indice_rota_delta_minimo] = rota_delta_minimo

    # Caso contrário, isso significará que não foram encontradas posições de inserção factíveis para as rotas em questão
    # fazendo-se necessária uma nova rota
    else:

        S.append([0, no_pickup, no_delivery, 2 * n + 1])

    # Atualizando quantidade de pedidos atendidos
    qtd_atendidos += 1

    # Removendo pedido de L
    L.pop(0)

# Printando solução
for rota in S:

    print(rota)






