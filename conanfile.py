from conans import ConanFile, CMake, tools
import os


class spdlogConan(ConanFile):
    name = "spdlog"
    version = "0.1"
    license = "<Put the package license here>"
    url = "https://github.com/memsharded/conan-spdlog"

    def source(self):
       self.run("git clone https://github.com/gabime/spdlog.git")
       self.run("cd spdlog && git checkout 33a185188c2ed59ff6077025a28fc320c4f2dbc4")

    def package(self):
        self.copy("*", dst="include", src="spdlog/include")
