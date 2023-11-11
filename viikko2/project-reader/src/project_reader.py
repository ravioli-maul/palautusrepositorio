import tomlkit
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston TOML-muotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        # Parse TOML
        parsed = tomlkit.parse(content)
        project_data = parsed.get("tool", {}).get("poetry", {})
        dependencies_dict = project_data.get("dependencies", {})
        dev_dependencies_dict = project_data.get("group", {}).get("dev", {}).get("dependencies", {})
        
        # Assign data to variables
        name = project_data.get('name', 'Nameless project')
        description = project_data.get('description', 'No description')
        license = project_data.get('license', 'No license')
        authors = project_data.get("authors", [])
        dependencies =  list(dependencies_dict.keys())
        dev_dependencies = list(dev_dependencies_dict.keys())

        # return the Project object
        return Project(name, description, authors, license, dependencies, dev_dependencies)
