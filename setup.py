from distutils.core import setup

setup(
    name='Converto',
    version='0.1dev',
    packages=['converto'],
    license='MIT',
    entry_points={
        'console_scripts': ['converto=converto.command_line:main'],
    }
    description=open('README.md').read(),
    data_files=[
        ('config', ['configuration/configuration.xml'])
    ],
    install_requires=[
        'menu',
        'ffmpy'
    ],
)
