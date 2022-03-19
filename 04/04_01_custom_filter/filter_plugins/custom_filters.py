#!/usr/bin/python

from ansible.errors import AnsibleFilterTypeError

import re


def normalize_mac(value):
    """
    Try normalize mac
    Raise on error
    """
    if not isinstance(value, str):
        raise AnsibleFilterTypeError("String type is expected, "
                                     "got type %s instead" % type(value))

    clean_value = re.sub(r"(?i)[^0-9a-z]+", "", value)

    re_match = re.match(r"(?i)^[0-9a-f]{12}$", clean_value)
    if not re_match:
        raise AnsibleFilterTypeError("Valid MAC-address expected, "
                                     "got %s" % value)

    mac_octets = [clean_value[i:i+2] for i in range(0, 12, 2)]
    mac = ":".join(mac_octets).upper()

    return mac


class FilterModule(object):
    def filters(self):
        custom_filters = {
            'normalize_mac': normalize_mac,
        }
        return custom_filters
