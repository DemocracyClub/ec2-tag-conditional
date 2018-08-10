import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from ec2_tag_conditional import __version__


CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Environment :: Other Environment",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Systems Administration",
    "Topic :: Utilities",
]

# read long description
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()


class PyTestCommand(TestCommand):
    user_options = [
        ("flakes", None, "Use Flakes")
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.flakes = True

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests']
        if self.flakes:
            self.test_args += ['--flakes', '--cov', 'ec2_tag_conditional']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='ec2_tag_conditional',
    version=__version__,

    description='Tests for EC2 tags',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sym Roe',
    author_email='sym.roe@democracyclub.org.uk',
    license='MIT',

    python_requires='>=3.6',
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    cmdclass={'test': PyTestCommand},

    entry_points="""
    [console_scripts]
    instance-tags=ec2_tag_conditional.util:command_line
    """,
    install_requires=[
        'boto'
    ]
)
