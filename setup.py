from setuptools import setup

VERSION = "1.0.0"


DEPENDENCIES = [
    'json',
    'logging',
    'time',
    'uuid',
    'datetime',
    'six'
]

setup( name='structuredlogging',
       version=VERSION,
       description='The structuredlogging package',
       long_description='The structuredlogging package',
       license='MIT',
       author='Azure CAT E2E',
       author_email='azcate2esupport@microsoft.com',
       url='https://github.com/tushardhadiwal/structuredlogging',
       packages=['structuredlogging'],
       include_package_data=True,
       install_requires=DEPENDENCIES,
       zip_safe=False)

