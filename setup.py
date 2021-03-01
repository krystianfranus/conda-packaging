import setuptools

with open('VERSION', 'r') as f:
    version = f.read().strip()

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    install_requires = f.read().split('\n')

setuptools.setup(
    name='my-package',
    version='1.0.0',
    author='John Doe',
    author_email='john.doe@example.com',
    description='A small example package',
    long_description=long_description,
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['my-command=my_package.command_line:main'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
)
