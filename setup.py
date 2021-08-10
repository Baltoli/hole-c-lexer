from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name                            = "hole-c-lexer",
    version                         = "0.0.2",
    author                          = "Bruce Collie",
    author_email                    = "brucecollie82@gmail.com",
    description                     = "Lexer for the C with syntactic holes",
    long_description                = long_description,
    long_description_content_type   = "text/markdown",
    url                             = "https://github.com/Baltoli/hole-c-lexer",
    packages                        = find_packages(),
    install_requires                = [
        "pygments"
    ],
    classifiers                     = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires                 = ">=3.6",
    entry_points                    =
    """
    [pygments.lexers]
    hole_c_lexer = hole_c_lexer.lexer:HoleCLexer
    """,
)
