from distutils.core import setup

# Dependencies are listed only in requirements.txt to maintain a single file.
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='dandelion',
    packages=['dandelion'],
    package_dir={'dandelion': 'src'},
    version='0.1',
    description='A rhyme detection package',
    author='Diego Vicente',
    author_email='mail@diego.codes',
    license='MIT',
    url='https://github.com/DiegoVicen/dandelion',
    download_url='https://github.com/DiegoVicen/dandelion/archive/0.1.tar.gz',
    install_requires=requirements,
    keywords=['rhyme', 'nlp', 'natural-language'],
    classifiers=[],
)
