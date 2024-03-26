from lxml import etree

def print_tree(element, depth=0):
    """Рекурсивная печать древовидной структуры"""
    # вывод текущего элемента с соответствующим
    print("-" * depth + element.tag)

    # рекурсивная печать дочерних элементов с увеличенным отступом
    for child in element.iterchildren():
        print_tree(child, depth + 1)

# парсинг HTML-документа
tree = etree.parse("src/web_page.html")

# получение корневого элемента дерева
root = tree.getroot()

# вывод структуры дерева
print_tree(root)