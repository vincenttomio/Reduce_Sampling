# Bibliotecas
import cv2
import sys

def reduce_sampling(image, percentage, technique):
    # Calcula o novo tamanho da imagem
    new_width = int(image.shape[1] * (1 - percentage / 100))
    new_height = int(image.shape[0] * (1 - percentage / 100))
    
    # Usando a técnica de quantização especificada, reduz a amostragem
    match(technique):
        case "media":
            reduced_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
        case "mediana":
            reduced_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
        case "moda":
            reduced_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)
        case _:
            raise ValueError("Técnica de quantização inválida. Use 'media', 'mediana' ou 'moda'.")

    # Salva a imagem reamostrada
    output_image_name = "reduced_" + str(percentage)  + "_" + technique + "_" + image_name
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
        output = reduce_sampling(original_image, reduction_percentage, quantization_technique)
        print(f"Imagem reamostrada com sucesso e salva como {output}")

    except Exception as e:
        print(f"Erro: {e}")
