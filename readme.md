# un-tree

依据 tree 命令生成的文件夹结构数据反向创建文件夹

## 使用

```shell
# 准备 tree 文件
tree -d > dir.tree
# 修改脚本内容
# 运行脚本
python main.py
```

```python
from pathlib import Path

import tree

if __name__ == '__main__':
    # 创建 tree 对象 并指定 tree 文件路径
    tree = tree.Tree(tree_path=Path("./dir.tree"))
    # 通过 tree 文件内容反向创建文件夹
    tree.un_tree(folder_root=Path('./'), ignore_level=0, ignore_line_flag="#")
```

## 注意

tree文件中所有的记录只会被当成`文件夹`生成，请自行排除`文件`的记录

```text
root
 ├── BT
 └── a.png (需要自行筛选)
```

又或者 生成tree 文件时使用命令排除`文件`，只展现`文件夹`

```shell
tree -d > dir.tree
```
