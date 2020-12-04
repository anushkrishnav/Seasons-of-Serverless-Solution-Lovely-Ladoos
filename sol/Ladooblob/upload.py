import os
import yaml
from azure.storage.blob import ContainerClient

def load_config():
    dir_root = os.path.dirname(os.path.abspath(__file__))
    with open(dir_root + "/config.yaml", "r") as yamlfile:
        return yaml.load(yamlfile, Loader=yaml.FullLoader)

configs = load_config()
print(* configs)
def get_files(dir):
    with os.scandir(dir) as enteries:
        for entry in enteries:
            if entry.is_file() and not entry.name.startswith("."):
                yield entry

ladoo_images = get_files(configs["source"])
# print(*ladoo_images)

