import glob
import json

from setuptools import setup, find_packages


with open('.project_metadata.json') as meta_file:
    project_metadata = json.loads(meta_file.read())

with open('README.rst') as readme_file:
    long_description = readme_file.read()
    long_description_content_type = 'text/x-rst'

setup(
    name=project_metadata['name'],
    version=project_metadata['release'],
    author=project_metadata['author'],
    author_email=project_metadata['author_email'],
    description=project_metadata['description'],
    url=project_metadata['url'],
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    license=project_metadata['license'],
    install_requires=[
        'flask',
        'pyjwt',
        'pendulum',
        'passlib',
        'flask-buzz',
    ],
    extras_require={
        'dev': [
            'flake8',
            'flask-sqlalchemy',
            'freezegun',
            'pytest',
            'pytest-flask',
            'sphinx',
        ],
    },
    include_package_data=True,
    packages=find_packages(),
    scripts=glob.glob('bin/*'),
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
