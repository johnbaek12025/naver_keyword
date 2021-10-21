# TODO: 새로운 유닛 테스트 모듈을 사용하자!!!

from setuptools import setup
from setuptools.command.test import test as TestBase


class NoInstallTest(TestBase):
    """Just like a normal test, but never install packages"""
    def run(self):
        self.distribution.install_requires = []
        return TestBase.run(self)

setup(
    name='skm',
    description      = 'SKM',
    author           = 'ThinkPool',
    url              = 'http://www.thinkpool.com/',
    test_suite       = 'tests',
    platforms        = 'any',
    include_package_data=True,
    cmdclass={
        'test': NoInstallTest,
    },


 )
