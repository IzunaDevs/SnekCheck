# Stdlib
import os

# External Libraries
import configobj

__all__ = ("config", )

config = configobj.ConfigObj({  # pylint: disable=invalid-name
    "all": {
        "linters": [
            "flake8", "pylint", "yapf", "isort", "pyroma", "safety", "bandit",
            "dodgy", "pydocstyle", "vulture", "pytest", "pypi"
        ]
    },
    "pypi": {
        "TWINE_USERNAME": os.environ.get("TWINE_USERNAME", "abc"),
        "TWINE_PASSWORD": os.environ.get("TWINE_PASSWORD", "abc"),
        "sign": False,
        "TWINE_REPOSITORY": "pypi",
        "quiet": False
    },
    "flake8": {
        "max-line-length": 79,
        "exclude": ["build", "dist"],
        "ignore": ["D100", "D101"],
        "quiet": False
    },
    "pylint": {
        "quiet": False
    },
    "yapf": {
        "inplace": True,
        "quiet": False
    },
    "isort": {
        "line_length": 79,
        "inplace": True,
        "indent": '    ',
        "quiet": False
    },
    "bandit": {
        "quiet": False
    },
    "style": {
        "inplace": True,
        "quiet": False
    },
    "pyroma": {
        "quiet": False
    },
    "vulture": {
        "min-confidence": 60,
        "verbose": False,
        "exclude": [],
        "sort-by-size": False,
        "quiet": False
    }
})
