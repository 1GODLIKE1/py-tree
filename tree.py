import os
import json

class Tree:
    def __init__(self, DIR):
        self.DIR = DIR

    def tree(self):
        tree_obj = Tree.tree_objects(self, self.DIR)
        with open('tree.json', 'w', encoding="utf-8") as file:
            json.dump(tree_obj, file, ensure_ascii=False, sort_keys=False, indent=4)
        print(tree_obj)

    def tree_objects(self, *args):
        tree_obj = {'name': os.path.basename(args[0])}

        if os.path.isdir(args[0]):
            tree_obj['type'] = "directory"
            tree_obj['children'] = [Tree.tree_objects(self, os.path.join(args[0], x)) for x in os.listdir(args[0])]
        else:
            tree_obj['type'] = 'file'
        
        return tree_obj
    


if __name__ == "__main__":
    Tree("<PATH>").tree()