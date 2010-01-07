import inspect
import imp
import os
import tempfile
from node import TreeNode

class File(TreeNode):

    def __init__(self, path=None):
        super(File, self).__init__()

        self.classes = {}

        self.__init_classes(path)
        self.__init_structure(path)

    def __init_classes(self, path):
        with open(path, 'r') as f:
            file_content = f.read()

            # http://docs.python.org/library/tempfile.html#tempfile.mktemp
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.py')
            temp_file.write(file_content)
            temp_file.close()

            try:
                module = imp.load_source('', temp_file.name)
            except Exception, e:
                print e

            module_classes = inspect.getmembers(module, inspect.isclass)

            for name, klass in module_classes:
                self.classes[name.lower()] = klass

            os.unlink(temp_file.name)
            os.unlink(temp_file.name + 'c')

    def __init_structure(self, path):
        if not isinstance(path, str) or not path:
            return

        current_node = self
        parts = path.split('/')

        for part in reversed(parts):
            current_node.name = part
            current_node.parent = File()
            current_node = current_node.parent
