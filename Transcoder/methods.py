import os
import importlib
import sys
# from imp import find_module,load_module
from Transcoder.Module import CoderInterface
import threading


class PluginManager(object):
    """Base class for plugin managers. Does not implement loadPlugins, so it
    may only be used with a static list of plugins.
    """
    name = "base"

    def __init__(self, plugins=(), config={}, info=0):
        self.__plugins = []
        self.infoPrint = info
        if plugins:
            self.addPlugins(plugins)

    def addPlugin(self, plug):
        if self.infoPrint >= 1: print('PluginManager add plugin:', plug)
        self.__plugins.append(plug)

    def addPlugins(self, plugins):
        for plug in plugins:
            self.addPlugin(plug)

    def delPlugin(self, plug):
        if plug in self.__plugins:
            self.__plugins.remove(plug)

    def delPlugins(self, plugins):
        for plug in plugins:
            self.delPlugin(plug)

    def getPlugin(self, name=None):
        if self.infoPrint >= 2: print('self.__plugins:', self.__plugins)
        for plugin in self.__plugins:
            if self.infoPrint >= 2: print('plugin.Name', plugin.Name)
            if (name is None or plugin.Name == name):
                return plugin
        return CoderInterface()

    def getPlugins(self, name=None):
        plugins = []
        if self.infoPrint >= 2: print('self.__plugins:', self.__plugins)
        for plugin in self.__plugins:
            if self.infoPrint >= 2: print('plugin.Name', plugin.Name)
            if (name is None or plugin.Name == name):
                plugins.append(plugin)
        return plugins
    def getPluginsName(self):
        pluginNameList=[]
        for plugin in self.__plugins:
            pluginNameList.append(plugin.Name)
        return pluginNameList

    def _loadPlugin(self, plug):
        loaded = False
        if self.infoPrint >= 2: print('******PluginManager  _loadPlugin ,', self.__plugins)
        for p in self.__plugins:
            if p.Name == plug.Name:
                loaded = True
                break
        if not loaded:
            self.addPlugin(plug)
            print("|| [Info]:%s: loaded plugin %s " % (self.name, plug.Name))

    def loadPlugins(self):
        pass


class CoderPluginManager(PluginManager):
    """Plugin manager that loads plugins from plugin directories.
    """
    name = "MethodsManager"

    def __init__(self, plugins=(), config={}, info=0):
        default_directory = os.path.join(os.path.dirname(__file__), "Methods")
        self.directories = config.get("directories", (default_directory,))
        print('================================<DirectoryPlugManager>================================')
        PluginManager.__init__(self, plugins, config, info)

        self.lock = threading.Lock()

    def loadPlugins(self):
        """Load plugins by iterating files in plugin directories.
        """
        plugins = []
        print('|| [Info]:Path of directories:', self.directories)
        for dir in self.directories:
            try:
                for f in os.listdir(dir):
                    if f.endswith(".py") and f != "__init__.py":
                        plugins.append((f[:-3], dir))
            except OSError:
                print("[Warning]:Failed to access: %s" % dir)
                continue

        print('|| [Info]:Directory all plugins:')
        for plugin in plugins:
            print('|| ', plugin)
        for (name, dir) in plugins:
            try:
                self.lock.acquire()

                # fh, filename, desc = find_module(name, [dir])
                mod = importlib.import_module("Transcoder.Methods." + name)
                if self.infoPrint >= 1: print(mod)
                cls = getattr(mod, name)

            finally:
                self.lock.release()

            if not issubclass(cls, CoderInterface):
                continue
            self._loadPlugin(cls())

        print('================================<DirectoryPlugManager>================================')

"""
class Coder:
    def __init__(self):
        self.folderPath = 'E:\\Smartcoder\\Methods\\'
        self.pluginNameList = os.listdir(self.folderPath)

    def plugin_load(self, pluginName: str, sep=':', package=None):
        m, _, c = pluginName.partition(sep)
        mod = importlib.import_module(m, package)
        print(mod)
        cls = getattr(mod, c)
        return cls()
"""

if __name__ == '__main__':
    Methods_manager = CoderPluginManager()
    Methods_manager.loadPlugins()
    plugins = Methods_manager.getPlugin("Morse Code")
