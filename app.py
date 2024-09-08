import requests

def buscar_filme(titulo, chave_api):
    url = "http://www.omdbapi.com/"
    parametros = {
        't': titulo,
        'apikey': chave_api
    }
    
    resposta = requests.get(url, params=parametros)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        if dados['Response'] == 'True':
            return dados
        else:
            return f"Erro: {dados['Error']}"
    else:
        return f"Erro na requisição: {resposta.status_code}"

# Exemplo de uso
chave_api = 'e52a051e'
titulo_filme = 'Sting'
resultado = buscar_filme(titulo_filme, chave_api)

if isinstance(resultado, dict):  # Verifica se resultado é um dicionário válido
    print(f'Título: {resultado["Title"]}')
    print(f'Tipo: {resultado["Type"]}')
    print(f'País: {resultado["Country"]}')
    print(f'Sinopse: {resultado["Plot"]}')
    print(f'Atores: {resultado["Actors"]}')
    print(f'Gênero: {resultado["Genre"]}')
    print(f'Lançamento: {resultado["Released"]}')
    print(f'Ano: {resultado["Year"]}')
    print(f'Duração: {resultado["Runtime"]}')
    print(f'Escritor: {resultado["Writer"]}')
else:
    print(resultado)  # Imprime a mensagem de erro
