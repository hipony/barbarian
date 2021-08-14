from conans import ConanFile, tools
import os


class Package(ConanFile):
    name = "hipony-barbarian"
    homepage = "https://github.com/hipony/barbarian"
    description = "<<<SHORT_DESCRIPTION>>>"
    topics = ("test")
    license = "<<<LICENSE>>>"
    url = "https://github.com/hipony/barbarian"
    barbarian = {
        "description": {
            "format": "asciidoc",
            "text": '''\
<<<LONG_DESCRIPTION>>>
'''
        }
    }
    source_subfolder = "source_subfolder"

    def source(self):
        tools.get(
            **self.conan_data["sources"][self.version],
            strip_root=True, destination=self.source_subfolder)

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        pass

    def package(self):
        self.copy(
            pattern="LICENSE.txt", dst="licenses",
            src=self.source_subfolder)
        for pattern in ["*.h", "*.hpp", "*.hxx"]:
            self.copy(
                pattern=pattern, dst="include",
                src=os.path.join(self.source_subfolder, "include"))
        for pattern in ["*.lib", "*.so", "*.dylib", "*.a"]:
            self.copy(pattern=pattern, dst="lib", keep_path=False)
        for pattern in ["*.dll", "*.exe"]:
            self.copy(pattern=pattern, dst="bin", keep_path=False)
