# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, print_function)
__metaclass__ = type

import os
from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
        Ansible file jinja2 tests
    """

    def filters(self):
        return {
            'validate_file_sd': self.validate_file_sd,
        }

    def validate_file_sd(self, data, targets):
        """
        """
        result = []
        sublist = []
        config_files = []

        for scrape in data:
            """
            """
            file_sd = scrape.get("file_sd_configs", None)

            if isinstance(file_sd, list):
                file_sd = file_sd[0]
                files = file_sd.get("files", [])

                if len(files) > 0:
                    sublist.append(files)

        config_files = sum(sublist, [])

        display.v("  - files: {}".format(config_files))

        for f in config_files:
            name, extension = os.path.basename(f).split(".")
            if name not in targets or extension != "yml":
                result.append(os.path.basename(f))

        display.v("{}".format(result))

        return result
