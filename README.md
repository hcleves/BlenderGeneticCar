# BlenderGeneticCar

## table of contents

Adiconar depois utilizando o [site](https://ecotrust-canada.github.io/markdown-toc/)

## Uso

Para utilizar o programa, basta acessar o arquivo .blend dentro da pasta Blenders.

Nota-se que tambem é facil criar um arquivo novo, basta coloca-lo dentro da pasta Blenders e copiar e colar o arquivo main.py na pasta scripts para o editor de texto do blender e executar o script. Caso seja um novo arquivo, é recomendado fazer os seguintes passos para melhorar a performance:

1. Vá na view de Properties, na Aba Render, procure por System
2. Nesse local desabilite "Use Frame Rate" e mude o Vsync para Off
3. Ainda na Aba Render, vá para "Display", que deve estar logo abaixo de System.
4. Habilite as caixas "Debug Properties" e "Framerate e Profile". Apesar dessas caixas não estarem ligadas a performance, oferecem informacoes importantes sobre o estado do programa

Em ambos os casos, seja um arquivo novo ou um arquivo antigo é essencial executar os seguintes comandos no console interativo python assim que abrir o arquivo. Do contrario o python irá lancar um erro de docstring durante a segunda vez que for realizada a simulacao.

``` python
import numpy
import importlib
importlib.reload(numpy)
```

Para lancar a simulacao, basta abrir uma janela do 3dView, colocar o mouse sobre ela e teclar "p". Certifique-se que o Blender está no modo Blender Game. Para sair da simulacao, basta colocar o mouse sobre ela novamente e apertar ESC.
