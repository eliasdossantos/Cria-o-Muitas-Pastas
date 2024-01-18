import os

caminho_base = r'C:\Users\Documentos\Provas Correções'
nomes_pastas = [
    'Qualidade em Saúde e Segurança'
]

for nome in nomes_pastas:
    caminho_pasta = os.path.join(caminho_base, nome)
    if not os.path.exists(caminho_pasta):
        try:
            os.makedirs(caminho_pasta)
            print(f'Pasta {nome} criada em {caminho_base}')
        except OSError as e:
            print(f'Erro ao criar a pasta {nome}: {e}')
    else:
        print(f'A pasta {nome} já existe em {caminho_base}')