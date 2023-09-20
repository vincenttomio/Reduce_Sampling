# Reduce Sampling Script

Este é um programa em Python que permite a redução da amostragem em uma imagem monocromática com base nos parâmetros fornecidos, incluindo o nome da imagem, o percentual de redução e a técnica de quantização.

## Requisitos

- Python 3.x
- Biblioteca OpenCV (cv2)
- Biblioteca NumPy

Certifique-se de ter o Python instalado em seu sistema e instale as bibliotecas OpenCV e NumPy usando os seguintes comandos:

```bash
pip install opencv-python
pip install numpy
```

## Utilização

Para usar o programa, siga estas etapas:

1. Abra o terminal.
2. Navegue até o diretório onde o script `reduce_script.py` está localizado.
3. Execute o script com os seguintes parâmetros:

```bash
python reduce_script.py <nome_da_imagem> <percentual_de_reducao> <tecnica_de_quantizacao>
```

Substitua `<nome_da_imagem>` pelo nome do arquivo de imagem que você deseja reamostrar, `<percentual_de_reducao>` pelo valor de redução desejado (0 a 100) e `<tecnica_de_quantizacao>` pela técnica de quantização desejada (media, mediana ou moda).

Exemplo:

```bash
python reduce_script.py imagem.png 50 media
```

Isso reduzirá a imagem "imagem.png" em 50% usando a técnica de quantização média e salvará a imagem reamostrada com um nome semelhante a "reduced_50_media_imagem.png" no mesmo diretório.

## Conclusão

Este script oferece uma maneira simples de reduzir a amostragem de uma imagem monocromática com diferentes técnicas de quantização. Você pode ajustar o percentual de redução e a técnica de acordo com suas necessidades. Certifique-se de fornecer os parâmetros corretos ao executar o programa para obter os resultados desejados.
