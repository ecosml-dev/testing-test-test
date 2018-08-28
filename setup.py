import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "testing_test_test",
    # update version whenever you create a new release
    version = "{{version}}",
    author = "jrmerz",
    description = ("this is a test, this is only a test"),
    license = "MIT",
    keywords = "",
    url = "http://localhost:3000/package/461fb100-f23f-4d61-a405-5393728c0382",
    packages=[
        'testing_test_test',
        'testing_test_test.main'
    ],
    package_data={
      'testing_test_test' : ['resources/*']
    },
    long_description=read('README.md'),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)