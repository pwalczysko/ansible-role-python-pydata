import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('module', [
    'matplotlib',
    'numpy',
    'pandas',
    'scipy',
    'skimage',
    'tables',
    'yaml',
])
def test_python_module(host, module):
    host.check_output('python3.12 -c "import %s"' % module)
