class PluginLoader:
 
    def load(self, directory):
        ret = []
 
        for plugin in directory.children:
            plugin_file = plugin.children.find(name=plugin.name)
            plugin_class = plugin_file.classes[plugin.name]
            ret.append(plugin_class)
 
        return ret
