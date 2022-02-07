class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo =comendo
        self.falando = falando

        variavel = 'Valor'
        print(variavel)
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando. ')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja esta comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando')

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} parou de comer')
            return
         
