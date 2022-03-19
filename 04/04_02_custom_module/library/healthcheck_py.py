#!/usr/bin/python
# -*- coding: utf-8 -*-

import abc

from ansible.module_utils.basic import AnsibleModule
import requests
from requests import exceptions


DOCUMENTATION = r'''
---
module: healthcheck_py
author: Etoneja
short_description: healthcheck of site
description:
  - healthcheck of site with or without TLS
version_added: 0.0.1
requirements:
  - requests
  - python >= 3.6
options:
  addr:
    description:
      - Address of site we want to check
      - This is a required parameter
    type: str
  tls:
    description:
      - Whether site using certificates or not
      - Default value is True
    type: bool
'''

EXAMPLES = r'''
- name: Check availability of site
  healthcheck_py:
    addr: mysite.example
  connection: local

- name: Check availability of site without certs
  healthcheck_py:
    addr: mysite.example
    tls: false
  connection: local
'''

RETURN = r'''
msg:
  description: Errors if occured
  returned: always
  type: str
  sample: "Task executed successfully!"
result_str:
  description: State status
  returned: always
  type: str
  sample: "200"
rc:
  description: Return code
  returned: always
  type: int
  sample: 1
failed:
  description: Failed status
  returned: always
  type: bool
  sample: false
'''


class AbstractResult(abc.ABC):

    @property
    def changed(self):
        return False

    @property
    def failed(self):
        return self._failed

    @property
    def result_str(self):
        return self._result_str

    @property
    def rc(self):
        return self._rc

    @property
    def msg(self):
        return self._msg


class FailedResult(AbstractResult):

    _failed = True
    _result_str = "no result"
    _rc = 1

    def __init__(self, msg="Task failed"):
        super().__init__()
        self._msg = msg



class SuccessResult(AbstractResult):

    _failed = False
    _rc = 0

    def __init__(self, result_str, msg="Task executed successfully!"):
        super().__init__()
        self._result_str = result_str
        self._msg = msg



def check_addr_status_code(addr, tls):
    proto = "https" if tls else "http"
    url = "%s://%s" % (proto, addr)

    try:
        r = requests.get(url)
        result = SuccessResult(r.status_code)
    except exceptions.HTTPError as e:
        result = FailedResult(msg="HTTP error: %s" % str(e))
    except Exception as e:
        result = FailedResult(msg="Unexpected error: %s" % str(e))
    
    return result



def main():
    arguments = dict(
        addr=dict(required=True, type="str"),
        tls=dict(type="bool", default=True)
    )

    module = AnsibleModule(
        argument_spec=arguments,
        supports_check_mode=False
    )

    addr = module.params["addr"]
    tls = module.params["tls"]

    res = check_addr_status_code(addr, tls)

    if res.failed:
        module.fail_json(changed=res.changed,
                         failed=res.failed,
                         result_str=res.result_str,
                         rc=res.rc,
                         msg=res.msg)
    else:
        module.exit_json(changed=res.changed,
                         failed=res.failed,
                         result_str=res.result_str,
                         rc=res.rc,
                         msg=res.msg)


if __name__ == "__main__":
    main()
