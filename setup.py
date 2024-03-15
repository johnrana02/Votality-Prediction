from setuptools import find_packages,setup
from typing import List

Hypen_E_Dot = '-e .'
def get_requirements(file_path:str)->List[str]:

    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n"," ") for req in requirement]


        if Hypen_E_Dot in requirement:
            requirement.remove(Hypen_E_Dot)

        return requirement    


setup(
    name= 'Volatility prediction Project',
    version = '0.0.1',
    author = 'Anuj Rana',
    author_email ='anujrana89114@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirement.txt')

)