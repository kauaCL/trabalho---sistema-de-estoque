class Estoque:
    def __init__(self):
        self.produtos = ['maçã', 'uva', 'pera']

    def cadastrar_produto(self):
        produto = input( 'Cadastre o produto: ' )
        self.produtos.append( produto )
        print( f'Produto "{produto}" cadastrado com sucesso!' )

    def consultar_estoque(self):
        print( '\nLista de produtos:' )
        if not self.produtos:
            print( '(Estoque vazio)' )
        else:
            for i, produto in enumerate( self.produtos, start=1 ):
                print( f'{i}. {produto}' )

    def remover_produto(self):
        if not self.produtos:
            print( 'Não há produtos para remover.' )
            return

        print( '\n=== Remover Produto ===' )
        self.consultar_estoque()

        try:
            indice = int( input( '\nDigite o número do produto que deseja remover: ' ) )
            if 1 <= indice <= len( self.produtos ):
                produto_removido = self.produtos.pop( indice - 1 )
                print( f'Produto "{produto_removido}" removido com sucesso!' )
            else:
                print( 'Número inválido!' )
        except ValueError:
            print( 'Entrada inválida! Digite um número válido.' )


class SistemaLogin:
    def __init__(self, usuario='admin', senha='1234'):
        self.usuario = usuario
        self.senha = senha
        self.ativo = True

    def autenticar(self):
        while True:
            usuario = input( 'Digite o nome do usuário: ' )
            senha = input( 'Digite sua senha: ' )
            if usuario == self.usuario and senha == self.senha and self.ativo:
                print( 'Acesso liberado!' )
                return True
            else:
                print( 'Acesso negado, tente novamente.' )


class SistemaEstoque:
    def __init__(self):
        self.login = SistemaLogin()
        self.estoque = Estoque()

    def menu(self):
        while True:
            print( '''\n==== MENU PRINCIPAL ====
1. Cadastrar produto
2. Consultar estoque
3. Remover produto
4. Sair''' )

            opcao = input( 'Escolha uma opção: ' )

            if opcao == '1':
                self.estoque.cadastrar_produto()
            elif opcao == '2':
                self.estoque.consultar_estoque()
            elif opcao == '3':
                self.estoque.remover_produto()
            elif opcao == '4':
                print( 'Saindo...' )
                break
            else:
                print( 'Opção inválida!' )


# --- Execução do programa ---
sistema = SistemaEstoque()

if sistema.login.autenticar():
    sistema.menu()