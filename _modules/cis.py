# -*- coding: utf-8 -*-
'''
A module to CIS benchmark/audit your machines using SaltStack.

:maintainer:    Haije Ploeg
:maturity:      new
:platform:      rhel,debian
'''
from __future__ import absolute_import, print_function, unicode_literals

import logging

# Import salt libs
import salt

log = logging.getLogger(__name__)

# Define the module's virtual name
__virtualname__ = 'cis'


def __virtual__():
    '''
    Confine this module to Debian and RHEL based systems
    '''
    try:
        os_family == __grains__['os_family'].lower()

        if 'redhat' == os_family or 'debian' == os_family:
            return __virtualname__
        return(False, "Module cis: no RHEL or Debian based system detected")
    except Exception:
        return(False, "Module cis: no RHEL or Debian based system detected")


def audit(level=1, kind='server'):
    '''
    Audits the machine based on the input level en kind. Defaults to server
    level 1.

    CLI Example:
    .. code-block:: bash

        salt '*' cis.audit level=2 kind=server
    '''
    minion_id = __salt__['grains.get']('id')

    return(minion_id, level, kind)
