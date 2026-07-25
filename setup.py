from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> list:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            requirement = line.split('#', 1)[0].strip()
            if not requirement:
                continue
            if requirement.startswith('-e ') or requirement.startswith('--'):
                continue
            requirements.append(requirement)
    return requirements


setup(
    name='ml_project',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Rahul Singh',
    author_email='rahul.singh.7920000@gmail.com'
    )

