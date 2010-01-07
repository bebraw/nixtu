from mock import Mock, patch, sentinel
from placidity.file import File
 
def mock_with(mock, file_mock):
    mock.return_value = Mock()
    mock.return_value.__enter__ = Mock()
    mock.return_value.__enter__.return_value = file_mock
    mock.return_value.__exit__ = Mock()
 
def mock_with_read(mock, read_return=sentinel.file_contents):
    file_mock = Mock()
    file_mock.read.return_value = read_return
 
    mock_with(mock, file_mock)
 
class TestFile:
 
    @patch('__builtin__.open')
    def test_get_file_name(self, open_mock):
        mock_with_read(open_mock)
 
        file = File('/path/to/file')
 
        assert file.name == 'file'
 
    @patch('__builtin__.open')
    def test_get_file_parent(self, open_mock):
        mock_with_read(open_mock)
 
        file = File('/path/to/file')
 
        assert file.parent.name == 'to'
        assert file.parent.parent.name == 'path'
 
    @patch('__builtin__.open')
    def test_get_directory_children(self, open_mock):
        mock_with_read(open_mock)
 
        file = File('/path/to/file')
 
        directory = file.parent
 
        assert directory.children == [file, ]
 
    @patch('__builtin__.open')
    def test_find_child_by_name(self, open_mock):
        mock_with_read(open_mock)
 
        file = File('/path/to/file')
 
        directory = file.parent
 
        assert directory.find(name='file') == file
 
    @patch('__builtin__.open')
    def test_load_python_file(self, open_mock):
        read_return_value = '''
class Bar: flag = True
class Foo: flag = False
'''
        
        mock_with_read(open_mock, read_return_value)
 
        file = File(sentinel.filepath)
 
        assert 'bar' in file.classes
        assert file.classes['bar'].flag == True
        assert 'foo' in file.classes
        assert file.classes['foo'].flag == False
