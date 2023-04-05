from pathlib import Path

import tree

if __name__ == '__main__':
    # window
    window_tree = tree.Tree(tree_path=Path("./tree/window.tree"))
    window_tree.un_tree(folder_root=Path('./'))

    # linux
    linux_tree = tree.Tree(tree_path=Path("./tree/linux.tree"))
    linux_tree.un_tree(folder_root=Path('./'))
