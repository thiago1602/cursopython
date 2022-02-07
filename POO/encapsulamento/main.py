class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]
bd = BaseDeDados()
bd.inserir_cliente(1, 'Thiago')
bd.inserir_cliente(2, 'Leticia')
bd.inserir_cliente(3, 'Laissa')
bd.apaga_cliente(3)
bd.lista_clientes()