from conans import ConanFile, CMake, tools

class Proj1Conan(ConanFile):
    #name = proj1 
    #version = 0.0.1 

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
        cmake = CMake(self,generator="Ninja")
        cmake.configure(source_folder="proj1")
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include", src="proj1")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.so", dst="lib", src="bin", keep_path=False)
        self.copy("*.dylib", dst="lib", src="bin", keep_path=False)
        self.copy("*.a", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["proj1"]

