from conans import ConanFile, CMake


class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    scm =  {
        "type": "git",
        "url": "auto",
        "revision": "auto",
    }

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="create_sources_scm/src")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="create_sources_scm/src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]