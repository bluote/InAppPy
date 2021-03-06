from setuptools import setup


setup(
    name='inapppy',
    version='0.6',
    packages=['inapppy'],
    install_requires=['rsa', 'requests'],
    description="In-app purchase validation library for Apple AppStore and GooglePlay.",
    keywords='in-app store purchase googleplay appstore validation',
    author='Lukas Šalkauskas',
    author_email='halfas.online@gmail.com',
    url='https://github.com/dotpot/InAppPy',
    long_description=open('README.rst').read(),
    license='MIT'
)
