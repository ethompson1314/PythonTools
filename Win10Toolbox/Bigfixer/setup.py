from setuptools import setup
setup(
    name = "Bigfixer",
    packages = ["Bigfixer"],
    scripts = ["bin/Bigfixer"],
    include_package_data = True,
    package_data = {
        "Bigfixer":
        [
            "Bigfixer/data/config/config.yaml",
        ]
    },
    version = "0.1.0",
    description = "Fixes Bixfix installs",
    author = "Ernest Thompson",
    author_email = "ernest@ibm.com",
    url = "https://github.com/ethompson1314/Bigfixer",
    download_url = "https://github.com/myname/myapp/zipball/master",
    keywords = ["Bigfixer"],
    packages = setuptools.find_packages(),
    license = 'LICENSE',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Help Desk",
        "Intended Audience :: Help Desk",
        "License :: MIT License",
        "Operating System :: Windows",
        "Topic :: Support",
        ],
    long_description = open('README').read()