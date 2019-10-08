import salt


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
    minion_id = __salt__['grains.get']('id')
    os = __salt__['grains.get']('os')
    osmajorrelease = __salt__['grains.get']('osmajorrelease')

    return level, kind
