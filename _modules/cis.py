# -*- coding: utf-8 -*-
'''
A module to CIS benchmark/audit your machines using SaltStack.

:maintainer:    Haije Ploeg
:maturity:      new
:platform:      rhel,debian
'''
# Import Python libs
from __future__ import absolute_import, print_function, unicode_literals
import logging
import pkg_resources

# Import salt libs
import salt


log = logging.getLogger(__name__)

# Define the module's virtual name
__virtualname__ = 'cis'


def __virtual__():
    '''
    Confine this module to Debian and RHEL based systems
    '''
    if __grains__['os_family'].lower() in ['redhat', 'debian']:
        return __virtualname__

    return(False, "Module cis: no RHEL or Debian based system detected")


def _parse_yaml(os, osmajorrelease):
    yaml = os + osmajorrelease
    template_file = pkg_resources.resource_filename(__name__, 'templates/centos7.yml')
    print(template_file)


def _get_os():
    return(__grains__['os'].lower())


def _get_osmajorrelease():
    return(__grains__['osmajorrelease'].lower())


def audit(level=1, kind='server'):
    '''
    Audits the machine based on the input level en kind. Defaults to server
    level 1.

    level
        CIS level to score

    kind
        choose between workstation and server


    CLI Example:

    .. code-block:: bash

        salt '*' cis.audit level=2 kind=server
    '''
    client = salt.client.Caller()
    os = _get_os()
    osmajorrelease = _get_osmajorrelease()
    _parse_yaml(os, osmajorrelease)
    return(client.cmd('cmd.run', ['whoami']))
