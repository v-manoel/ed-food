def struct_item():
    """ Estrutura dos itens que serão cadastrados no sistema. """
    item = {
        "name" : "NaN",
        "price" : "NaN",
        "igredients" : "NaN",
        "estoque" : "NaN",
        "type_item" : "NaN",
        "type_drink" : "NaN",
        "flavor_drink" : "NaN",
        "type_protein" : "NaN",
        "protein_portion" : "NaN"
    }

    return item

def struct_menu():
    menu_prog = {
        "type_item" : {
            1 : "bebida",
            2 : "comida"
        },

        "type_drink" : {
            1 : "suco",
            2 : "refrigerante",
            3 : "água"
        },

        "type_protein" : {
            1 : "carne",
            2 : "peixe",
            3 : "vegano"
        }
    }

    return menu_prog

def struct_item_enum():
    itemType_enum ={
        "typeItem_drink" : {
            1 : "name",
            2 : "price",
            3 : "igredients",
            4 : "kcal",
            5 : "type_drink",
            6 : "flavor_drink"
        },

        "typeItem_protein" : {
            1 : "name",
            2 : "price",
            3 : "igredients",
            4 : "kcal",
            5 : "type_protein",
            6 : "protein_portion"
        }
    }

    return itemType_enum
