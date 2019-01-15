class FileNode:

    def __init__(self, name):
        self.name = name

    def longest_path(self):
        return self.name


class DirNode:

    def __init__(self, name):
        self.name = name
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def longest_path(self):
        longest_file = max([f.longest_path()
                            for f in self.files], key=len) if self.files else ''
        return self.name + '\\' + longest_file


def parse_name(string):
    name = ''
    index = 0
    while index < len(string) and (string[index].isalnum() or string[index] == '.'):
        name += string[index]
        index += 1
    return name, string[index:]


def parse_level(string):
    index = 1
    level = 0
    while index < len(string) and string[index] == '\t':
        level += 1
        index += 1
    return level, string[index:]


def create_dirtree(string):
    current_level = 0
    name, rest = parse_name(string)
    current_node = DirNode(name)
    parent_nodes = [current_node]
    while rest:
        level, rest = parse_level(rest)
        name, rest = parse_name(rest)
        if '.' in name:
            node = FileNode(name)
            parent_nodes[level-1].add_file(node)
        else:
            node = DirNode(name)
            parent_nodes[level-1].add_file(node)
            if len(parent_nodes) - 1 < level:
                parent_nodes.append(node)
            else:
                parent_nodes[level] = node
    return parent_nodes[0]


if __name__ == '__main__':
    tree = create_dirtree("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
    print(tree.longest_path())
    tree = create_dirtree(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    print(tree.longest_path())
