def list_select(options):
    for i, item in enumerate(options):
        print(i, item)

    selection = int(input("Type the index of desired item: "))
    return options[selection]