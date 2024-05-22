from typing import Any


def sorted_products_list(list_of_products: list, category_parameter: str = "None") -> Any:
    """Функция принимает на вход список продуктов и, опционально, категорию продукта.
    Возвращает отсортированный по убыванию список продуктов с, опционально, выбранной категорией"""

    if category_parameter != "None":
        filtered_category_list = []
        for product in list_of_products:
            if product["category"] == category_parameter:
                filtered_category_list.append(product)
        sorted_products_list = sorted(filtered_category_list, key=lambda words: words["price"], reverse=True)
        return sorted_products_list
    elif category_parameter == "None":
        sorted_products_list = sorted(list_of_products, key=lambda words: words["price"], reverse=True)
        return sorted_products_list
