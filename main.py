from pathlib import Path

import tree

if __name__ == '__main__':
    # 创建 tree 对象 并指定 tree 文件路径
    tree = tree.Tree(tree_path=Path("./dir.tree"))
    # 通过 tree 文件内容反向创建文件夹
    tree.un_tree(folder_root=Path('./'), ignore_level=0, ignore_line_flag="#")
