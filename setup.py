import setuptools
from sparxDB.version import Version


setuptools.setup(name='sparxDB',
                 version=Version('1.0.0').number,
                 description='SparxDB - NoSQL using RDBMS',
                 long_description=open('README.md').read().strip(),
                 author='Bastin Robins J',
                 author_email='robin@cleverinsight.co',
                 url='http://sparxDB.readthedocs.io',
                 py_modules=['packagename'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='sparxDB package',
                 classifiers=['Packages', 'Database'])
