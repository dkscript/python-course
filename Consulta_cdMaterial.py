from tkinter import *
import api_globo

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "20")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="CONSULTA ")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.cdMaterialLabel = Label(self.segundoContainer, text="Código de Material", font=self.fontePadrao)
        self.cdMaterialLabel.pack(side=LEFT)

        self.cdMaterialInput = Entry(self.segundoContainer)
        self.cdMaterialInput["width"] = 30
        self.cdMaterialInput["font"] = self.fontePadrao
        self.cdMaterialInput.pack(side=LEFT)

        #self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        #self.senhaLabel.pack(side=LEFT)

        #self.senha = Entry(self.terceiroContainer)
        #self.senha["width"] = 30
        #self.senha["font"] = self.fontePadrao
        #self.senha["show"] = "*"
        #self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Pesquisar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # Método verificar senha
    def verificaSenha(self):

        usuario = self.cdMaterialInput.get()
        #senha = self.senha.get()
        api_globo.GerarListaMateriais(str(usuario).split(','))

        #if usuario == "usuariodevmedia" and senha == "dev":
            #self.mensagem["text"] = "Autenticado"
        #else:
            #self.mensagem["text"] = "Erro na autenticação"


root = Tk()
Application(root)
root.mainloop()