class Leitor:

    def __init__(self, nome_instancia):

        """Essa classe irá receber como parâmetro o nome do arquivo da instância e retornará,
           com o método "nome_instancia", os parâmetros de uma instância de PDPTW, na seguinte ordem:

           x -> Coordenada x de cada cliente "i" na instância;
           y - > Coordenada y de cada cliente "i" na instância;
           d -> Tempo de serviço de cada cliente "i";
           q -> Demanda de cada nó "i";
           e -> Início da janela de tempo de cada nó "i";
           l -> Fim da janela de tempo de cada nó "i";
           t -> Tempo de viagem (igual/proporcional à distância entre cada nó);
           n -> número de pedidos (pares pickup-delivery);
           Cap -> capacidade de cada veículo

           """

        # Lendo linhas do arquivo
        lines = open(nome_instancia, 'r').readlines()

        # Computando primeira linha, com parâmetros sem índice da instância
        first_line = list(map(int, lines[0].split()))

        # Computando demais parâmetros da instância
        instance = [list(map(float, line.split())) for line in lines[1:]]

        # Coordenada x de cada nó "i"
        x = [line[1] for line in instance]

        # Coordenada y de cada nó "i"
        y = [line[2] for line in instance]

        # Tempo de serviço de cada nó "i"
        d = [line[3] for line in instance]

        # Demanda de cada nó "i"
        q = [line[4] for line in instance]

        # Início da janela de tempo de cada nó "i"
        e = [line[5] for line in instance]

        # Fim da janela de tempo de cada nó "i"
        l = [line[6] for line in instance]

        # Número de requests
        n = first_line[1]

        # Capacidade de cada veículo
        Cap = first_line[3]

        # Tempo de viagem (igual/proporcional à distância entre cada nó): inicia-se como 0
        t = [[0 for i in range(0,2*n+2)] for j in range(0,2*n+2)]

        for i in range(0, 2*n+2):
            for j in range(0, 2*n+2):

                # Calculando distância euclidiana, arrendondando para 2 casas
                dist = round(((x[i]-x[j])**2 + (y[i]-y[j])**2)**(1/2),2)
                t[i][j] = dist


        # Método que retorna uma tupla com todos os dados da instância, na ordem especificada
        self.dados_instancia = (x, y, d, q, e, l, t, n, Cap)
