from conans import ConanFile


class spdlogConan(ConanFile):
    name = "spdlog"
    version = "0.10.0"
    license = "MIT"
    url = "https://github.com/memsharded/conan-spdlog"

    def source(self):
       self.run("git clone https://github.com/gabime/spdlog.git")
       self.run("cd spdlog && git checkout v0.10.0")

    def package(self):
        self.copy("*", dst="include", src="spdlog/include")
