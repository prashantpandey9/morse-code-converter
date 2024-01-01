from setuptools import setup, find_packages

setup(
    name="morse_code_converter",
    version="1.1",
    packages=find_packages(),
    install_requires=[
        "pygame",
    ],
    include_package_data=True,
)
