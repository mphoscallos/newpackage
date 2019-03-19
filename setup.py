from setuptools import setup, find_packages

setup(
    name='newpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='project python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/mphoscallos/newpackage.git',
    author='<Mpho Sello>',
    author_email='<mphoscallos.mm@gmail.com>'
)
