from dataclasses import dataclass
from typing import List, Optional
from uplink import Consumer, get, Path, returns


class GithubConsumer(Consumer):

    def __init__(self, *args, base_url: Optional[str] = None, **kwargs):
        super().__init__(base_url=base_url or "https://api.github.com", *args, **kwargs)

    @returns.json
    @get("/repos/{author}/{repo}/releases")
    def releases(self, author: Path, repo: Path):
        """ Get all releases of Github package (sorted by Release Date) """
        pass

    @returns.json
    @get("/repos/{author}/{repo}/releases/latest")
    def latest_release(self, author: Path, repo: Path):
        """ Get latest release of Github package """


class BioinformaticsPackage:
    pass


@dataclass
class Bowtie2:
    author: str = "BenLangmead"
    repository: str = "Bowtie2"
    os: str = "Linux"
    flavor: str = "ubuntu"
    version_tag: str = "latest"
    deps: List[str] = [
        "apt-utils",
        "ca-certificates",
        "curl",
        "dialog",
        "gcc",
        "g++",
        "perl",
        "python3.10",
        "make",
        "unzip",
        "zstd",
        "zlib1g-dev"
    ]
