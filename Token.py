# Dicionário para armazenar os tokens válidos
tokens_validos = {
    "token123": "Usuário 01",
    "token456": "Usuário 02",
    "token789": "Usuário 03"
}

# Dicionário para armazenar os tokens utilizados
tokens_utilizados = {}

# Função para validar o token
def validar_token(token):
    if token in tokens_validos:
        usuario = tokens_validos[token]
        return True, usuario
    else:
        return False, None

# Loop para interagir com o usuário
while True:
    token_digitado = input("Digite o seu token de acesso: ")

    # Verifica se o token é válido
    valido, usuario = validar_token(token_digitado)

    if valido:
        print(f"[Token válido]\nBem-vindo, {usuario}!")

        # Registra o token utilizado
        tokens_utilizados[token_digitado] = usuario

        acessar_tokens = input("Deseja acessar a lista de tokens válidos? (S/N): ")
        if acessar_tokens.upper() == "S":
            # Exibe os tokens válidos após a validação
            print("\nTokens válidos:")
            for token in tokens_validos.keys():
                print(token)

        acessar_utilizados = input("Deseja acessar a lista de tokens utilizados? (S/N): ")
        if acessar_utilizados.upper() == "S":
            # Exibe os tokens utilizados após a validação
            print("\nTokens utilizados:")
            for token, usuario in tokens_utilizados.items():
                print(f"Token: {token} - Usuário: {usuario}")

    else:
        print("Token inválido. Por favor, insira um token válido.")

    continuar = input("Deseja continuar? (S/N): ")
    if continuar.upper() != "S":
        break
