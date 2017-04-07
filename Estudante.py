# Estudante.py
# Módulos necessários...
import array
import datetime
from random import *

"""
    Programa por: Leo Neto
    Este ficheiro contém a definição para um objecto de nome Estudante.

    Informação Útil:

    TOKENS:
    As listas com o nome Token são utilizadas para gerar os IDs de cada instância da classe Estudante.
    Cada ID tem o comprimento de 10 dígitos. Os IDs devem começar com uma das letras L, Z, R, ou S.

    CriarID() é o método utilizado gerar os IDs a partir dos tokens.
    A estrutura para a criação dos IDs é a seguinte:
    (ltoken) + (comprimento do nome) + (ttoken) + (2 x mtoken) + (ztoken) + (dtoken)
    Exemplo:   R 10 74 MP 5 EN

    Info():
    O método Info() permite mostrar os dados sobre cada instância da classe Estudante.

    Exemplo da função ----------
    Nome: Jonathan Daniel
    Tel.: 555 555 5555
    Email: jonathandaniel@uluz.edu
    Curso: Ciências da Computação
    Especialidade: Software
    Inscrição: Janeiro de 2015
    Graduação: Dezembro de 2019
    ID: L3014UI9MZ
    ----------------------------

    MUDAR:
    Estas funções permitem alterar certas propriedades do objecto.

    Salvar():
    Todas as instâncias da classe Estudante podem ser salvas utilizando este método.

    ReportarHack():
    Se alguém tentar mudar certos atributos de uma instância da classe Estudante sem as devidas permissões,
    este método irá criar um relatório da actividade com o nome do usuário, bem como o tipo de alteração que
    o usuário tentou realizar.

"""

######## Classe Estudante________________

class Estudante(object):
    # ___________Propriedades__________________
    ltoken = ['L','Z','R','S']                                                          # Code: 1
    mtoken = ['M','N','P','W','Q','D','F','C','B','T','V','X','Y']                      # Code: 2
    dtoken = ['EN','CI','LG','CM','ST','FI','EC']                                       # Code: 3
    ttoken = [30,42,16,81,61,72,15,50,38,49,14,55,74,62,24,64,32,93,95,59,44,11,10,77]  # Code: 4
    ztoken = [0,1,2,3,4,5,6,7,8,9]                                                      # Code: 5
    master = ['A','G','H','J','K','U','E','I']                                          # Code: 6

    #_____________ Métodos____________________

    # Constructor para a classe Estudante
    def __init__(self, nome, sobrenome):
        object.__init__(self)
        self.nome = nome.capitalize()
        self.sobrenome = sobrenome.capitalize()
        self.email = self.nome.lower() + self.sobrenome.lower() + '@uluz.edu'
        self.tel   = 0                       # Não mostrar se o valor for o pre-definido
        self.curso = "Undefined"             # Não mostrar se o valor for o pre-definido
        self.especialidade = "Undefined"     # Não mostrar se o valor for o pre-definido
        self.inscricao = 11999               # Não mostrar se o valor for o pre-definido
        self.graduacao = 11999               # Não mostrar se o valor for o pre-definido
        self.id = self.CriarID()
        self.criacao = datetime.date.today()
        self.SalvarEstudante()



    def NomeCompleto(self):
        return '{} {}'.format(self.nome, self.sobrenome)


    def LetrasNoNome(self):
        total = len(self.NomeCompleto()) - 1
        if(total<10):
            variacao = 10-total
            total=total + variacao
        return total


    def CriarID(self):
        limite  = len(self.ltoken)
        bloco1 = str(self.ltoken.pop(randrange(limite)))
        bloco2 = str(self.LetrasNoNome())

        limite  = len(self.ttoken)
        bloco3 = str(self.ttoken.pop(randrange(limite)))

        limite  = len(self.mtoken)
        bloco4 = str(self.mtoken.pop(randrange(limite)))

        limite  = len(self.ztoken)
        bloco5 = str(self.ztoken.pop(randrange(limite)))

        limite  = len(self.dtoken)
        bloco6 = str(self.dtoken.pop(randrange(limite)))

        id = bloco1 + bloco2 + bloco3 + bloco4 + bloco5 + bloco6
        return id # retorna uma 'string' com o ID do Estudante...


    def CriarEmail(self):
        self.numero = randint(0, 99)
        self.numero = str(self.numero)
        self.email = self.nome.lower() + self.sobrenome.lower() + self.numero + '@uluz.edu'
        print(self.email)



    def Info(self):
        print("Nome: {}".format(self.NomeCompleto()))
        if(self.tel!=0):
            print("Tel.: {}".format(self.tel))
        print("Email: {}".format(self.email))
        if(self.curso!= "Indefinido"):
            print("Curso: {}".format(self.curso))
        if(self.especialidade!= "Indefinido"):
          print("Especialidade: {}".format(self.especialidade))
        if(self.inscricao!=11999):
            print("Inscrição: {}".format(self.inscricao))
        if(self.graduacao!=11999):
            print("Graduação: {}".format(self.graduacao))
        print("ID: {}".format(self.id))


    def MudarCurso(self, c):
        self.curso = c
        self.SalvarCurso()


    def MudarEspecialidade(self, e):
        self.especialidade = e


    def MudarInscricao(self, data):
        self.inscricao = data


    def MudarGraduacao(self, grad):
        self.graduacao = grad


    def MudarID(self):
        # Uma palavra-passe será necessária
        if(self.Permissao()):
            self.id = self.CriarID()
        else:
            self.ReportarHack("ID")


    def MudarEmail(self):
        if (self.Permissao()):
            self.email = self.CriarEmail()
        else:
            self.ReportarHack("Email")


    def Salvar(self):
        with open('Estudante.txt', 'a') as file:
            if file != "":
                file.write("\n") # adding space between each student entry
            file.write("{}\n".format(self.nome))
            file.write("{}\n".format(self.sobrenome))
            file.write("{}\n".format(self.email))
            file.write("{}\n".format(self.curso))
            file.write("{}\n".format(self.especialidade))
            file.write("{}\n".format(self.inscricao))
            file.write("{}\n".format(self.graduacao))
            file.write("{}\n".format(self.id))
            file.close()


    def ReportarHack(self, systemInfo):
        print("Permissão negada.\n")

        hoje = datetime.date.today()
        hora_actual = hoje.toordinal()

        with open('Reporte-de-Hacks.txt', 'a') as file:
            file.write("ERRO: O usuário {}, com o ID {}, tentou mudar o seu {}.\n".format(self.NomeCompleto(), self.id, systemInfo))
            file.write("A chave utilizada foi: '{}'.\n".format(self.UsedToken()))
            file.write("O acidente aconteceu aos {}.\n".format(hoje))
            file.close()



    def SalvarEstudante(self):
        with open ('Alteracoes.txt', 'a') as file:
            hoje = datetime.date.today()
            file.write('{} foi adicionado aos {}.\n'.format(self.NomeCompleto(), hoje))
            file.close()



    def SalvarID(self):
        with open ('ChangeLog.txt', 'a') as file:
            thisDate = datetime.date.today()
            file.write('Novo ID gerado para {} aos {}.\n'.format(self.NomeCompleto(), thisDate))
            file.close()



    def SalvarCurso(self):
        with open ('Alteracoes.txt', 'a') as file:
            thisDate = datetime.date.today()
            file.write('Curso, {}, adicionado à {} aos {}.\n'.format(self.curso, self.NomeCompleto(), thisDate))
        file.close()



    def SalvarEspecialidade(self):
        with open ('Alteracoes.txt', 'a') as file:
            thisDate = datetime.date.today()
            file.write('Speciality, {}, added to {} on {}.\n'.format(self.curso, self.NomeCompleto(), thisDate))
        file.close()



    def Permissao(self):
        codigo = input("Código: ")
        self.CodigoUtilizado(codigo)
        if(codigo == "UEI644"):
            permissao = True
        else:
            permissao = False
        return permissao



    def CodigoUtilizado(self, token):
        self.__codigo = token


    def UsedToken(self):
        return self.__codigo

######## Fim da classe Estudante _______________________




def main():
    nome = input("Nome: ")
    sobrenome  = input("Sobrenome: ")
    pessoa    = Estudante(nome, sobrenome)
    pessoa.Info()


if __name__ == "__main__":
    main()
