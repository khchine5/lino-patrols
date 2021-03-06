"""
Examples how to run these tests::

  $ python setup.py test
  $ python setup.py test -s tests.DocsTests
  $ python setup.py test -s tests.DocsTests.test_debts
  $ python setup.py test -s tests.DocsTests.test_docs
"""
from unipath import Path

ROOTDIR = Path(__file__).parent.parent

# load  SETUP_INFO:
execfile(ROOTDIR.child('lino_patrols', 'project_info.py'), globals())

from lino.utils.pythontest import TestCase


class BaseTestCase(TestCase):
    django_settings_module = "lino_patrols.settings.demo"
    #~ default_environ = dict(DJANGO_SETTINGS_MODULE="lino_patrols.demo.settings")
    project_root = ROOTDIR
    
    
class DemoTests(BaseTestCase):
    """
    $ python setup.py test -s tests.DemoTests.test_admin
    """
    def test_admin(self):
        # self.run_django_admin_test('lino_patrols.settings.demo')
        self.run_django_manage_test()


class DocsTests(BaseTestCase):

    def test_general(self):
        return self.run_docs_doctests('tested/general.rst')

    def test_patrols(self):
        return self.run_docs_doctests('tested/patrols.rst')

class PackagesTests(BaseTestCase):
    def test_packages(self): 
        self.run_packages_test(SETUP_INFO['packages'])

