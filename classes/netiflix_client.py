class Cliente:
    def __init__(self, nome, gmail, plano):
        self.nome = nome
        self.gmail = gmail
        self.lista_plano = ['basic', 'premium']
        if plano in self.lista_plano:
            self.plano = plano
        else:
            raise Exception('Plano inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano = novo_plano

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print('Ver filme!')
        elif self.plano == 'premium':
            print('ver filme!')
        elif plano_filme == 'premium' and self.plano == 'basic':
            print('È necessario atualizar plano para acessar o filme!')
            up = str(input('Deseja atualizar seu plano [S/N]: ')).upper()
            if up in 'S':
                client.mudar_plano('premium')
                print('Mudança concluida')
            print('ate logo!')
        else:
            print('plano invalido!')

client = Cliente("Arthur", "Arturfas123@gmail.com", "basic")
print(client.plano)
client.ver_filme('Titanic', 'premium')
print(client.plano)
