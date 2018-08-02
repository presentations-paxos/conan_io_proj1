from conans import ConanFile, CMake, tools

class Proj1Conan(ConanFile):
    # TODO: pull name and version from environment
    name = "proj1"
    version = "0.0.0-3-g5d6f7fd"

    license = "Public Domain"
    url = "http://gitlab/demo/proj1"
    description = "Say hello"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://gitlab:8080/demo/proj1.git")
        self.run("cd proj1 && git checkout static_shared")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("proj1/CMakeLists.txt", "PROJECT(MyProj1)",
                              '''PROJECT(MyProj1)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="proj1")
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include/proj1", src="proj1/proj1")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["proj1"]

