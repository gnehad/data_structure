"""
Étant donné un tableau d'élément, générer un nouveau tableau dont chaque
élément sera égal au produit des éléments du tableau, sauf lui-même
"""

"""
    Version avec les divisions
    Calculer le produit des éléments du tableau
    Pour chaque élément : lui affecter le produit / sa valeur
    Si l'élément est nul, le résultat est nul.
"""

def print_list(elements):
    output = "["
    length = len(elements)
    for i in range(length):
        output = output + str(elements[i])
        if(i != length - 1):
            output = output + ","
        else:
            output = output + "]"
    print(output)
def perform_product(elements):
    product = 1
    for element in elements:
        product = product * element
    return product

def generate_product_elements(elements):
    product = perform_product(elements)
    product_elements = []
    for element in elements:
        if(element != 0):
            product_elements.append(product / element)
        else: 
            product_elements.append(element)
    return product_elements

values = [1, 2, 3, 5, 10, 19]
generated_values = generate_product_elements(values)
print_list(generated_values)