# 🎮 Jogo da Forca — Bairros do Recife

Um jogo da forca interativo desenvolvido em **Python**, executado no terminal e com temática baseada em **20 bairros do Recife**. O jogador terá até **10 tentativas** para descobrir o bairro sorteado.

## 🚀 Funcionalidades

- Menu inicial com identificação do jogador.
- Opções de **Nova partida** e **Sair**.
- Sorteio aleatório entre 20 bairros do Recife.
- Desenho da forca com 11 estágios (de 0 a 10 erros).
- Exibição das letras já utilizadas.
- Contagem de erros e tentativas restantes.
- Identificação das condições de vitória ou derrota.

## 📋 Regras do jogo

1. O jogo sorteia aleatoriamente um bairro do Recife e exibe os espaços correspondentes às letras.
2. A cada rodada, o jogador deve digitar uma letra para tentar descobrir o nome do bairro.
3. Se a letra existir no nome, todas as suas ocorrências serão reveladas.
4. Se a letra não existir ou a entrada for inválida, será contabilizado 1 erro e o desenho da forca avançará um estágio.
5. O jogador poderá cometer até 10 erros.

### 🏆 Condições de resultado

- **Vitória:** descobrir todas as letras do bairro antes de atingir o limite de erros.
- **Derrota:** atingir 10 erros antes de descobrir o nome completo do bairro.