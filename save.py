import json

class saves:
    def __init__(Self):
        super().__init__()
        
       
    def salvar_posicao(self, personagem_posicao):
        with open('save.json', 'w') as arquivo:
            json.dump(personagem_posicao, arquivo)

    def carregar_posicao(self):
        try:
            with open('save.json', 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            # Se o arquivo não for encontrado, retorna uma posição padrão
            print("Não há arquivo de save")
            return {'x': 52, 'y': 552}
        except json.JSONDecodeError:
            # Se houver um erro ao decodificar o JSON, retorna uma posição padrão
            print("Erro ao decodificar o arquivo de save")
            return {'x': 52, 'y': 552}