from setuptools import setup, find_packages

setup(
    name='easy-docs',
    version='1.0.3',
    license="MIT Licence",
    description="",

    author='Yaronzz',
    author_email="yaronhuang@foxmail.com",

    packages=find_packages(),
    platforms="any",
    include_package_data=True,
    install_requires=["requests"],
    entry_points={'console_scripts': ['easy-docs = easy_docs:main', ]}
)
