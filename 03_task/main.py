from node import insert, min_tree_value


def main():
    # prefill tree
    root = None
    keys = [10, 20, 30, 25, -4, 28, 27, -1]

    for key in keys:
        root = insert(root, key)

    min_value = min_tree_value(root)
    print(f"Min value is: {min_value}")  # -4


if __name__ == '__main__':
    main()
