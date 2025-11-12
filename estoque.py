# Classe responsável por gerenciar os produtos do estoque
class Estoque:
    def __init__(self):
        self.produtos = ['maçã', 'uva', 'pera']  # Lista inicial de produtos

    def cadastrar_produto(self):
        produto = input('Cadastre o produto: ')
        self.produtos.append(produto)
        print(f'Produto "{produto}" cadastrado com sucesso!')

    def consultar_estoque(self):
        print('\nLista de produtos:')
        if not self.produtos:
            print('(Estoque vazio)')
        else:
            for i, produto in enumerate(self.produtos, start=1):
                print(f'{i}. {produto}')

    def remover_produto(self):
        if not self.produtos:
            print('Não há produtos para remover.')
            return

        print('\n=== Remover Produto ===')
        self.consultar_estoque()

        try:
            indice = int(input('\nDigite o número do produto que deseja remover: '))
            # Verifica se o número digitado é válido
            if 1 <= indice <= len(self.produtos):
                # Remove o produto da lista (índices começam em 0)
                produto_removido = self.produtos.pop(indice - 1)
                print(f'Produto "{produto_removido}" removido com sucesso!')
            else:
                print('Número inválido!')
        except ValueError:
            # Caso o usuário digite algo que não seja número
            print('Entrada inválida! Digite um número válido.')


# Classe responsável pelo sistema de login
class SistemaLogin:
    def __init__(self, usuario='admin', senha='1234'):
        self.usuario = usuario
        self.senha = senha
        self.ativo = True  # Controla se o login está habilitado

    def autenticar(self):
        while True:
            usuario = input('Digite o nome do usuário: ')
            senha = input('Digite sua senha: ')
            # Confere usuário e senha
            if usuario == self.usuario and senha == self.senha and self.ativo:
                print('Acesso liberado!')
                return True
            else:
                print('Acesso negado, tente novamente.')


# Classe principal que une login e estoque
class SistemaEstoque:
    def __init__(self):
        self.login = SistemaLogin()  # Instancia o sistema de login
        self.estoque = Estoque()     # Instancia o estoque

    def menu(self):
        while True:
            print('''\n==== MENU PRINCIPAL ====
1. Cadastrar produto
2. Consultar estoque
3. Remover produto
4. Sair''')

            opcao = input('Escolha uma opção: ')

            # Executa a opção escolhida
            if opcao == '1':
                self.estoque.cadastrar_produto()
            elif opcao == '2':
                self.estoque.consultar_estoque()
            elif opcao == '3':
                self.estoque.remover_produto()
            elif opcao == '4':
                print('Saindo...')
                break
            else:
                print('Opção inválida!')


# --- Execução do programa ---
sistema = SistemaEstoque()

# Faz o login antes de mostrar o menu
if sistema.login.autenticar():
    sistema.menu()
