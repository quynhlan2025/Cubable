def cook_element(element: tuple, replace_string):
    locator = element[0]
    value = element[1]
    new_value = value % replace_string
    return (locator, new_value)


def cook_element_locator(element: tuple, replace_string):
    y = list(element)
    new_value = y[1] % replace_string
    return tuple(y)
