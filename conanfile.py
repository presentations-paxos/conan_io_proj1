from conans import ConanFile, CMake, tools
import os

class Proj1Conan(ConanFile):
    name = os.environ['PROJ1_NAME']
    version = os.environ['PROJ1_VER']

    license = "Public Domain"
    url = "http://gitlab:8080/demo/proj1"
    description = "Say Hello Library"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    requires = "boost_format/[>1.63.0,=~1.68.0]@bincrafters/stable"

    def source(self):
        self.run("git clone http://gitlab:8080/demo/proj1.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="proj1")
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include", src="proj1")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["proj1"]

