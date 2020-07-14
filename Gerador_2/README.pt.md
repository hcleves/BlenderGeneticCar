## Gerador 2

Esse é o segundo e último tipo de gerador testado, abaixo estão suas características:

* Rede neural mais simples, com apenas uma camada escondida de 4 neurônios
* Carros são eliminados ao longo da geração quando batem ou se não atingirem pontuação suficiente em um certo intervalo de tempo(ou seja, se estão muito lentos).
* Como os carros estão sendo eliminados, a simulação começa a ficar mais leve e pode ser executada a mais FPS. No efeito visual, parece que os carros estão acelerando, quando na verdade é apenas a simulação que está mais rápida.
* A simulação pode ser feita muito mais rapidamente que o gerador 1, já que dado uma certa geração, a maioria dos carros tende a falhar, e portanto a simulação roda com menos carros quanto mais tempo passa.
