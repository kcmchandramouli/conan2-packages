from conan import ConanFile
from conan.tools.files import get, copy

required_conan_version = ">=2.10.0"

class ApacheMavenConan(ConanFile):
    name = "7zip"
    version = "23.01"
    license = ("LGPL-2.1-or-later", "BSD-3-Clause", "UnRAR")
    homepage = "https://www.7-zip.org"
    description = "7zip sources"
    topics = ("zip", "unzip")
    settings = "os", "arch"

    def build(self):
        get(self, **self.conan_data["sources"][self.version][str(self.settings.os)][str(self.settings.arch)],
            destination=self.source_folder, strip_root=False)
        
    def package(self):
        copy(self, "*", src=self.source_folder, dst=self.package_folder)