from charmhelpers.core.hookenv import  status_set, log
from charms.reactive import set_flag, when, when_not, endpoint_from_flag
import charms.sshproxy


@when('sshproxy.configured')
@when_not('charm2.installed')
def install_charm2_proxy_charm():
    """Set the status to active when ssh configured."""
    set_flag('charm2.installed')
    status_set('active', 'Ready!')


@when('string.ready')
@when_not('charm2.file-created')
def create_file():
    """Create a file with passed string name."""
    err = ''
    try:
        string_interface = endpoint_from_flag('string.ready')
        strings = string_interface.receive_strings()
        filename = strings[0]
        cmd = ['touch {}'.format(filename)]
        result, err = charms.sshproxy._run(cmd)
    except:
        log('command failed: {}'.format(err))
    else:
        log({'output': result})
        set_flag('charm2.file-created')
