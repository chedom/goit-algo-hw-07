from node import insert, max_tree_value


def main():
    # prefill tree
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root = insert(root, key)

    max_value = max_tree_value(root)
    print(f"Max value is: {max_value}")  # 30


if __name__ == '__main__':
    main()
