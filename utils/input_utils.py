def list_select(options):
    for i, item in enumerate(options):
        print(i, item)

    selection = int(input("Type the index of desired item: "))
    return options[selection]


def list_select_index(options) -> int:
    for i, item in enumerate(options):
        print(i, item)

    selection = int(input("Type the index of desired item: "))
    return selection