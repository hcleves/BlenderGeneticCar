## Gerador 1

Esse é o primeiro tipo de gerador testado. Foi implementado com uma rede neural mais complexa. Trata-se de uma rede neural fully-connected com 2 camadas escondidas de 4 neurônios cada e com função de ativação sigmóide. As características desse programa estão listadas a seguir:
* Em uma dada Geração, todos os carros rodam por um mesmo período de tempo, independente de sua performance durante a geração
* A câmera segue o carro que foi melhor em performance da geração anterior. Na primeira geração, é escolhido um carro aleatoriamente
* Utiliza uma rede neural mais complexa
* Foi capaz de andar em Interlagos, no Treinamento, e em Mônaco, no teste, na primeira tentativa
* Tempo de treinamento é bem superior, pois todos os carros ficam ativos durante toda a geração, resultando em um custo computacional mais alto e FPS menores e constantes.
