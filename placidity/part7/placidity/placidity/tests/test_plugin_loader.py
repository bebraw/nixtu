from mock import Mock
from placidity.plugin_loader import PluginLoader

class TestPluginLoader:

    def test_load_plugins(self):
        class Plugin1: pass
        class Plugin2: pass

        plugin_dir = Mock()
        plugin1_dir = self.create_plugin_dir('plugin1', Plugin1)
        plugin2_dir = self.create_plugin_dir('plugin2', Plugin2)
        plugin_dir.children = (plugin1_dir, plugin2_dir)

        plugin_loader = PluginLoader()

        assert plugin_loader.load(plugin_dir) == [Plugin1, Plugin2]

    def create_plugin_dir(self, name, plugin_class):
        plugin_dir = Mock()
        plugin_dir.name = name
        plugin_dir.children = Mock()

        plugin_file = self.create_plugin_file(name, plugin_class)
        plugin_dir.find.return_value = plugin_file

        return plugin_dir

    def create_plugin_file(self, name, klass):
        plugin_file = Mock()
        plugin_file.classes = {name: klass, }

        return plugin_file
