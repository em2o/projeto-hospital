class Pessoa:
    def __init__(self,nome,idade,genero):
        self.nome=nome
        self.idade=idade
        self.genero=genero

class Paciente(Pessoa):
    def __init__(self,nome,idade,genero, sintoma):
        super().__init__(nome,idade,genero)
        self.sintoma = sintoma

    def imprimir_sintoma(self):
        return print('sintoma:'+ self.sintoma)

class Medico(Pessoa):
    def __init__(self,nome,idade,genero,crm):
        super().__init__(nome,idade,genero)
        self.crm = crm 

    def imprimir_crm(self):
        return print('crm:' + self.crm)

    def imprimir_nome(self):
        return print('nome:'+ self.nome)

    def imprimir_idade(self):
        return print('idade:' + self.idade)

    def imprimir_genero(self):
        return print ('genero:' + self.genero)


medico_um = Medico('Emanoel', "12", 'm', "1234211")
medico_um.imprimir_crm()
medico_um.imprimir_genero()
medico_um.imprimir_idade()
medico_um.imprimir_nome()
