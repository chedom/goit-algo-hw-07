from node import insert, sum_tree_value


def main():
    # prefill tree
    root = None
    keys = [10, 20, 30, 25, -4, 28, 27, -1]

    for key in keys:
        root = insert(root, key)

    sum_value = sum_tree_value(root)
    print(f"Sum value is: {sum_value}")  # 135


if __name__ == '__main__':
    main()
