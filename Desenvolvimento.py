import random

palavras = [
    "BOA VIAGEM", "RECIFE ANTIGO", "SANTO ANTONIO", "IBURA", "CORDEIRO",
    "ILHA DO LEITE", "NOVA DESCOBERTA", "DERBY", "ESPINHEIRO", "AREIAS",
    "GRACAS", "JAQUEIRA", "PARNAMIRIM", "TAMARINEIRA", "CASA FORTE",
    "APIPUCOS", "MONTEIRO", "CAXANGA", "JOANA BEZERRA", "MADALENA"
]

max_erros = 20

while True:
    print("\n=== JOGO DA FORCA ===")
    nome = input("Qual é o seu nome? ")
    print("\n=== BEM VINDO AO JOGO,", nome, "===")
    print("1 - Nova partida")
    print("2 - Sair")
    opcao = input("Escolha uma opção: ").strip()