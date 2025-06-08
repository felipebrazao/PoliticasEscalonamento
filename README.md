# 🚀 Corrida de Processos - Simulador de Escalonamento
Um jogo interativo que simula algoritmos de escalonamento de processos em sistemas operacionais, desenvolvido em Python com curses.
Inspiração: Este projeto foi criado com base em ideias sugeridas pelo DeepSeek Chat para estruturar a simulação de forma lúdica e educativa.

# 🎯 Objetivo
Demonstrar visualmente como os algoritmos de escalonamento (FIFO, Round Robin, Prioridade) alocam tempo de CPU para processos competindo por recursos.

# ⚙️ Funcionalidades
3 Algoritmos Implementados:

## ⏳ FIFO (First In, First Out)

## 🔄 Round Robin (com quantum ajustável)

## ⚡ Por Prioridade (processos com prioridades aleatórias)

Interface Visual: Barra de progresso e status em tempo real.

Modo "Corrida": Processos competem até a conclusão.

# 📦 Bibliotecas Utilizadas
Biblioteca	Versão	Descrição	Referência Oficial
curses	-	Interface gráfica no terminal	Python Docs
random	-	Geração de números aleatórios	Python Docs
time	-	Controle de tempo/delay	Python Docs
collections.deque	-	Fila de processos eficiente	Python Docs
sys	-	Interação com o sistema	Python Docs


# 🛠️ Tecnologias
Python 3.x

Biblioteca curses (para interface no terminal)

Módulos: random, time, collections.deque

# 🚦 Como Executar
Clone o repositório:

bash
git clone https://github.com/felipebrazao/PoliticasEscalonamento.git  
cd PoliticasEscalonamento  
Execute o jogo:

bash
python Corrida.py  
# 🎮 Como Jogar
Escolha um algoritmo no menu.

Observe os processos sendo executados (barra de progresso e tempo).

Ao final, o primeiro processo concluído é declarado vencedor!

# 📜 Licença
MIT License - veja LICENSE.

✨ Créditos
Desenvolvido por Felipe Brazão.

Inspiração inicial: DeepSeek Chat (para estruturação do conceito do jogo).
