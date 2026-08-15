class PathNode:
   def __init__(self, path, val):
        self.path = path
        self.val = val
        #self.children_paths = set()
        self.children = dict()

class FileSystem:

    def __init__(self):
        self.root = PathNode("", -1)

    def createPath(self, path: str, value: int) -> bool:
        paths = path.split("/")[1:]
        print(paths)
        parent = self.root
        for pi in range(len(paths)):
            p = paths[pi]
            if pi == len(paths) - 1:
                #if path already exists return false
                if p in parent.children:
                    break
                #parent.children_paths.add(p)
                parent.children[p] = PathNode(p, value)
                return True
            #not last
            if p in parent.children:
                parent = parent.children[p]
            else:
                break
        return False

    def get(self, path: str) -> int:
        paths = path.split("/")[1:]
        parent = self.root
        for pi in range(len(paths)):
            p = paths[pi]

            if p in parent.children:
                if pi == len(paths) - 1:
                    return parent.children[p].val
                parent = parent.children[p]
            else:
                break
        return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
