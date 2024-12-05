"""Fonctions pour lire un fichier"""
#### Imports et définition des variables globales

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    tab = []
    with open(filename, mode='r', encoding='utf8') as f:
        lines = f.readlines()
    for i in lines:
        string_tab = i.replace("\n","").split(";")
        int_tab = [int(x) for x in string_tab]
        tab.append(int_tab)
    return tab

def get_list_k(data, k):
    """Retourne la kième ligne du fichier"""
    return data[k]

def get_first(l):
    """Retourne la première liste du fichier"""
    return l[0]

def get_last(l):
    """Retourne la dernière liste du fichier"""
    return l[-1]

def get_max(l):
    """Retourne le max de la liste"""
    return max(l)

def get_min(l):
    """Retourne le min d'une liste"""
    return min(l)

def get_sum(l):
    """Retourne la somme d'une liste"""
    return sum(l)


#### Fonction principale


def main():
    """Tests de fonctions"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
