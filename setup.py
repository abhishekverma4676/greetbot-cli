from setuptools import setup, find_packages

setup(
    name="greetbot-cli",
    version="0.1.0",
    description="A friendly CLI greeting tool",
    author="Your Name",
    py_modules=["greetbot"],
    entry_points={
        "console_scripts": [
            "greetbot=greetbot:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)