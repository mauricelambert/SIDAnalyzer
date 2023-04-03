from setuptools import setup

setup(
    name="SIDAnalyzer",
    version="0.0.1",
    py_modules=["SIDAnalyzer"],
    install_requires=[],
    author="Maurice Lambert",
    author_email="mauricelambert434@gmail.com",
    maintainer="Maurice Lambert",
    maintainer_email="mauricelambert434@gmail.com",
    description="This script analyzes Microsoft SID.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mauricelambert/SIDAnalyzer",
    project_urls={
        "Executable": "https://mauricelambert.github.io/info/python/security/SIDAnalyzer.pyz",
    },
    classifiers=[
        "Topic :: Security",
        "Environment :: Console",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    scripts=[
        "SIDAnalyzer.py",
    ],
    python_requires=">=3.8",
    keywords=[
        "SID",
        "User",
        "Forensic",
        "Analysis",
        "Microsoft",
        "Identifier",
    ],
    platforms=["Windows", "Linux", "MacOS"],
    license="GPL-3.0 License",
)