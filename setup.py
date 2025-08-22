from http.server import executable

from cx_Freeze import setup, Executable
import os

path = "./assets"
assets_list = os.listdir(path)
game_assets_list = [os.path.join(path, assets).replace("\\", '/') for assets in assets_list]

print(game_assets_list)

executable = [Executable("main.py")]
files = {"include_files": game_assets_list, "packages": ["pygame"]}

setup(
    name = "The Speedster Bird Game",
    version = "1.0",
    description = "Speedster Bird Game",
    options = {"build.exe": files},
    executables = executable
)
