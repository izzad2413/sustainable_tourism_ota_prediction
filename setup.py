from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' # a constant variable
def get_requirements(file_path:str)->List[str]:
    '''
    takes a file path as input and returns 
    a list of requirements from requirements.txt file
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # read all the lines at a single go and then return them as each line a string element in a list
        requirements=[req.replace("\n","") for req in requirements] # removes the newline character, resulting in a clean list of requirements 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # remove the element existed
    
    return requirements

setup(
name='sustainable tourism ota prediction',
version='0.0.1',
author='nazmirul izzad nassir',
author_email='nazmirulizzadnassir@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt') # calls the function

)