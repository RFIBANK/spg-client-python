from setuptools import setup


setup(
    name='SPG client',
    version='0.0.1',
    description='Clint for RFI Partner API',
    long_description=open('README.md').read(),
    author='Daria Muravenko',
    author_email='led@papko.org',
    url='http://gitlab.fewerwords.org/rfi/spg_client',
    packages=['spg_client'],
    install_requires=['requests'],
)
