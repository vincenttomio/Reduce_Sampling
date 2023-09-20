# Bibliotecas
import numpy as np
import cv2
import sys

# Função para reduzir a amostragem pela média dos pixels em cada bloco
def reduce_by_average(image, new_height, new_width):
    # Cria uma matriz de zeros para a imagem reduzida
    reduced_image = np.zeros((new_height, new_width), dtype=np.uint8)

    # Loop pelas novas dimensões da imagem reduzida
    for i in range(new_height):
        for j in range(new_width):
            # Calcula as coordenadas de início e fim do bloco na imagem original
            row_start, row_end = i * image.shape[0] // new_height, (i + 1) * image.shape[0] // new_height
            col_start, col_end = j * image.shape[1] // new_width, (j + 1) * image.shape[1] // new_width

            # Extrai o bloco da imagem original
            block = image[row_start:row_end, col_start:col_end]

            # Calcula a média dos valores dos pixels no bloco e atribui à posição correspondente na imagem reduzida
            reduced_image[i, j] = np.mean(block)

    # Retorna a imagem reduzida
    return reduced_image

# Função para reduzir a amostragem pela mediana dos pixels em cada bloco
def reduce_by_median(image, new_height, new_width):
    reduced_image = np.zeros((new_height, new_width), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            row_start, row_end = i * image.shape[0] // new_height, (i + 1) * image.shape[0] // new_height
            col_start, col_end = j * image.shape[1] // new_width, (j + 1) * image.shape[1] // new_width
            block = image[row_start:row_end, col_start:col_end]

            # Calcula a mediana dos valores dos pixels no bloco e atribui à posição correspondente na imagem reduzida
            reduced_image[i, j] = np.median(block)

    return reduced_image

# Função para reduzir a amostragem pela moda dos pixels em cada bloco
def reduce_by_mode(image, new_height, new_width):
    reduced_image = np.zeros((new_height, new_width), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            row_start, row_end = i * image.shape[0] // new_height, (i + 1) * image.shape[0] // new_height
            col_start, col_end = j * image.shape[1] // new_width, (j + 1) * image.shape[1] // new_width
            block = image[row_start:row_end, col_start:col_end]

            # Calcula a moda (valor mais comum) dos valores dos pixels no bloco e atribui à posição correspondente na imagem reduzida
            reduced_image[i, j] = np.bincount(block.flatten()).argmax()

    return reduced_image


def reduce_sampling(image, percentage, technique, sample_name):
    # Calcula o novo tamanho da imagem
    new_width = int(image.shape[1] * (1 - percentage / 100))
    new_height = int(image.shape[0] * (1 - percentage / 100))
    
    # Usando a técnica de quantização especificada, reduz a amostragem
    match(technique):
        case "media":
            reduced_image = reduce_by_average(original_image, new_height, new_width)
            # reduced_image = cv2.resize(original_image, (new_width, new_height), interpolation=cv2.INTER_AREA)
        case "mediana":
            reduced_image = reduce_by_median(original_image, new_height, new_width)
            # reduced_image = cv2.resize(original_image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
        case "moda":
            reduced_image = reduce_by_mode(original_image, new_height, new_width)
            # reduced_image = cv2.resize(original_image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)
        case _:
            raise ValueError("Técnica de quantização inválida. Use 'media', 'mediana' ou 'moda'.")

    # Salva a imagem reamostrada
    output_image_name = "reduced_" + str(percentage)  + "_" + technique + "_" + sample_name
    cv2.imwrite(output_image_name, reduced_image)
    return str(output_image_name)
    


if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise ValueError("Uso: python reduce_script.py <nome_da_imagem> <percentual_de_reducao> <tecnica_de_quantizacao>")
        
        # Parametros
        image_name = sys.argv[1]
        reduction_percentage = float(sys.argv[2])
        quantization_technique = sys.argv[3].lower()

        # Abre a imagem em escala de cinza
        original_image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)

        # Verifica se a imagem foi carregada corretamente
        if original_image is None:
            raise ValueError("Não foi possível carregar a imagem.")

        # Chama a funcao principal
        output = reduce_sampling(original_image, reduction_percentage, quantization_technique, image_name)
        print(f"Imagem reamostrada com sucesso e salva como {output}")

    except Exception as e:
        print(f"Erro: {e}")
