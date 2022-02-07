class Pessoa:
    ano_atual = 2022

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


    @staticmethod
    def gera_id():
        rand = randint(1000, 19999)
        return rand
p1 = Pessoa.por_ano_nascimento('Thiago', 26)
print(p1)
print(p1.nome)
