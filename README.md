# sparxDB
sparxDB is a implementation of hybrid datastorage view using NoSQL type inside traditional databases.

[![Build Status](https://travis-ci.org/CleverInsight/sparxDB.png?branch=master)](https://travis-ci.org/CleverInsight/sparxDB)



## Package

Basic structure of package is

```
├── README.md
├── sparxDB
│   ├── __init__.py
│   ├── sparxDB.py
│   └── version.py
├── pytest.ini
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── helpers
    │   ├── __init__.py
    │   └── my_helper.py
    ├── tests_helper.py
    └── unit
        ├── __init__.py
        ├── test_example.py
        └── test_version.py
```

## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

## Tests

Testing is set up using [pytest](http://pytest.org) and coverage is handled
with the pytest-cov plugin.

Run your tests with ```py.test``` in the root directory.

Coverage is ran by default and is set in the ```pytest.ini``` file.
To see an html output of coverage open ```htmlcov/index.html``` after running the tests.

## Travis CI

There is a ```.travis.yml``` file that is set up to run your tests for python 2.7
and python 3.2, should you choose to use it.

