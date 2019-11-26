# BlenderGeneticCar

## table of contents

Adiconar depois utilizando o [site](https://ecotrust-canada.github.io/markdown-toc/)

## Uso

Para utilizar o programa, basta acessar o arquivo .blend dentro da pasta Blenders.

##### Importante: Para lançar o arquivo .blend utilize a linha de comando "blender <nome_do_arquivo>". Tentar abrir o arquivo com dois cliques ou outra maneira, irá resultar em uma simulação com defeitos, por motivos que não compreendo.

Nota-se que também é fácil criar um arquivo novo, basta colocá-lo dentro da pasta Blenders e copiar e colar o arquivo main.py na pasta scripts para o editor de texto do blender e executar o script. Caso seja um novo arquivo, é recomendado fazer os seguintes passos para melhorar a performance:

1. Vá na view de Properties, na Aba Render, procure por System
2. Nesse local desabilite "Use Frame Rate" e mude o Vsync para Off
3. Ainda na Aba Render, vá para "Display", que deve estar logo abaixo de System.
4. Habilite as caixas "Debug Properties" e "Framerate e Profile". Apesar dessas caixas não estarem ligadas a performance, oferecem informações importantes sobre o estado do programa

Em ambos os casos, seja um arquivo novo ou um arquivo antigo é essencial executar os seguintes comandos no console interativo python assim que abrir o arquivo. Do contrário o python irá lançar um erro de docstring durante a segunda vez que for realizada a simulação.

``` python
import numpy
import importlib
importlib.reload(numpy)
```

Para lançar a simulação, basta abrir uma janela do 3dView, colocar o mouse sobre ela e teclar "p". Certifique-se que o Blender está no modo Blender Game. Para sair da simulação, basta colocar o mouse sobre ela novamente e apertar ESC.

Para utilizar a camera do jogo no 3dView, pode-se utilzar a hotkey Numpad 0


