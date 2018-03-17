'''
A python package for EDA
'''
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()


# Main setup function
setup(
    name = "pykhoj",
    version = "1.0.dev",
    description = "Python package for exploratory data analysis",
    long_description=long_description,
    url = "https://github.com/bishal1995/pykhoj"
    author = ["Bishal Paul","Sagar Kar"],
    author_email = ["bishalpaul1905@gmail.com","sagarkar10@gmail.com"],
    classifiers=[
                #   3 - Alpha
                #   4 - Beta
                #   5 - Production/Stable
                'Development Status :: 3 - Alpha',

                # Who will use
                'Intended Audience :: Developers',
                'Topic :: Data Analysis :: Exploratory data analysis tool',

                # Licence type
                'License :: OSI Approved :: MIT License',

                # Specify the Python versions you support here. In particular, ensure
                # that you indicate whether you support Python 2, Python 3 or both.
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
            ],
    packages=find_packages(exclude=['tests']),  # Required
    # Include other packeges that pykhoj depends on
    install_requires=[],
    # Include optional data files needed for package
    package_data={  # Optional
                'sample': ['package_data.dat'],
            },
)
