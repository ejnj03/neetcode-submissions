class Path(object):
    def __init__(self, path="", is_file=False):
        self.path = path
        self.is_file = is_file
        if is_file:
            self.file_content = ""
        else:
            self.dir_content = dict()

class FileSystem:

    def __init__(self):
        self.root = Path()

    def create_list(self, path):
        return path.split("/")[1:] 

    def find_path(self, paths, curr, parent):
        print(paths, curr, parent)
        if len(paths) == 0 or paths[curr] == '':
            return self.root
        if curr == len(paths) - 1:
            return parent.dir_content[paths[curr]]
        return self.find_path(paths, curr + 1, parent.dir_content[paths[curr]])
    
    def ls(self, path: str) -> List[str]:
        #path is a valid file path
        paths = self.create_list(path)
        ret = self.find_path(paths, 0, self.root)
        if ret.is_file:
            return [ret.path]
        return sorted(list(ret.dir_content.keys()))

    def create_path(self, paths, curr, parent):
        if curr > len(paths) - 1:
            return
        path = paths[curr]
        if path not in parent.dir_content:
            parent.dir_content[path] = Path(path, is_file=False)
        self.create_path(paths, curr + 1, parent.dir_content[path])        

    def mkdir(self, path: str) -> None:
        paths = self.create_list(path)
        self.create_path(paths, 0, self.root)
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        file_path = self.create_list(filePath)
        par_dir = self.find_path(file_path[:-1], 0, self.root)
        file_name = file_path[-1]
        if file_name not in par_dir.dir_content:
            par_dir.dir_content[file_name] = Path(file_name, is_file=True)
        par_dir.dir_content[file_name].file_content += content

    def readContentFromFile(self, filePath: str) -> str:
        file_path = self.create_list(filePath)
        par_dir = self.find_path(file_path[:-1], 0, self.root)
        file_name = file_path[-1]
        return par_dir.dir_content[file_name].file_content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
