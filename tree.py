import os
import re
from pathlib import Path


class Tree(object):

    def __init__(self, tree_path: Path):
        self.tree_path = tree_path
        with open(self.tree_path, encoding="utf8") as file:
            self.tree_data = file.read()

    @classmethod
    def get_tree_level(cls, tree_line: str) -> int:
        return len(re.findall(r'\s?[├│└ ][\s─]{2}', tree_line))

    @classmethod
    def get_tree_name(cls, tree_line: str) -> str:
        match = re.search(r'^((\s?[├│└ ][\s─]{2})+\s)?(.*)', tree_line)
        return match.group(3) if match else ""

    def un_tree(self, folder_root: Path, ignore_level: int = 0, ignore_line_flag: str = "#") -> None:
        """
        通过 tree 文件的关系反向生成文件夹

        :param folder_root: 文件夹存放根目录
        :param ignore_level: 文件夹忽略层级
        :param ignore_line_flag: tree 文件中注释标识
        :return:
        """
        tree_lines = self.tree_data.splitlines()
        path_list = []
        ignore_level = max(ignore_level, 0)
        for line in tree_lines:
            if line.startswith(ignore_line_flag):
                continue
            # 文件夹层级
            tree_level = Tree.get_tree_level(line)

            if tree_level < ignore_level:
                continue
            # 文件夹名称
            tree_name = Tree.get_tree_name(line)
            if len(tree_name) == 0 or tree_name.isspace():
                continue

            path_list.insert(tree_level, tree_name)
            path_list = path_list[ignore_level:tree_level + 1]
            folder_path = folder_root.joinpath(*path_list)

            os.makedirs(folder_path, exist_ok=True)

            print("success" if folder_path.exists() else "fail", folder_path)
