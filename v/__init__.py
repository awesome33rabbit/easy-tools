from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("easy_tools")
except PackageNotFoundError:
    __version__ = "unknown version"

print(__version__)
