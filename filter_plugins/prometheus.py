# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, print_function)
__metaclass__ = type

import os
import re
from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
        Ansible file jinja2 tests
    """

    def filters(self):
        return {
            'validate_file_sd': self.validate_file_sd,
            'prometheus_checksum': self.checksum,
            'validate_alertmanagers': self.validate_alertmanagers,
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

            display.v("    - name: {} / extenstion {}".format(name, extension))

            if name not in targets or extension not in ["yml", "yaml"]:
                result.append(os.path.basename(f))

        display.v("{}".format(result))

        return result

    def checksum(self, data, os, arch):
        """
        """
        checksum = None

        if isinstance(data, list):
            # filter OS
            # linux = [x for x in data if re.search(r".*prometheus-.*.{}.*.tar.gz".format(os), x)]
            # filter OS and ARCH
            checksum = [x for x in data if re.search(r".*prometheus-.*.{}-{}.tar.gz".format(os, arch), x)][0]

        if isinstance(checksum, str):
            checksum = checksum.split(" ")[0]

        # display.v("= checksum: {}".format(checksum))

        return checksum

    def validate_alertmanagers(self, data):
        """
        """
        display.v(f"validate_alertmanagers({data})")

        supported = ["static_configs"]
        known_sd_configs = [
            "azure_sd_configs", "consul_sd_configs","dns_sd_configs","ec2_sd_configs", "eureka_sd_configs", "file_sd_configs",
               "digitalocean_sd_configs", "docker_sd_configs",  "dockerswarm_sd_configs", "gce_sd_configs", "hetzner_sd_configs",
               "http_sd_configs",  "kubernetes_sd_configs", "lightsail_sd_configs","linode_sd_configs", "marathon_sd_configs",
"nerve_sd_configs", "nerve_sd_configs", "openstack_sd_configs", "puppetdb_sd_configs", "scaleway_sd_configs", "serverset_sd_configs",
"triton_sd_configs","uyuni_sd_configs", "static_configs",
                      ]
        present = []

        if isinstance(data, list):
            for d in data:
                keys = d.keys()
                display.v(f"  - name: {d}")
                display.v(f"  - name: {keys}")

                if keys in known_sd_configs:
                    azure_sd = d.get("azure_sd_configs", None)
                    consul_sd = d.get("consul_sd_configs", None)
                    dns_sd = d.get("dns_sd_configs", None)
                    ec2_sd = d.get("ec2_sd_configs", None)
                    eureka_sd = d.get("eureka_sd_configs", None)
                    file_sd = d.get("file_sd_configs", None)
                    digitalocean_sd = d.get("digitalocean_sd_configs", None)
                    docker_sd = d.get("docker_sd_configs", None)
                    dockerswarm_sd = d.get("dockerswarm_sd_configs", None)
                    gce_sd = d.get("gce_sd_configs", None)
                    hetzner_sd = d.get("hetzner_sd_configs", None)
                    http_sd = d.get("http_sd_configs", None)
                    kubernetes_sd = d.get("kubernetes_sd_configs", None)
                    lightsail_sd = d.get("lightsail_sd_configs", None)
                    linode_sd = d.get("linode_sd_configs", None)
                    marathon_sd = d.get("marathon_sd_configs", None)
                    nerve_sd = d.get("nerve_sd_configs", None)
                    openstack_sd = d.get("openstack_sd_configs", None)
                    puppetdb_sd = d.get("puppetdb_sd_configs", None)
                    scaleway_sd = d.get("scaleway_sd_configs", None)
                    serverset_sd = d.get("serverset_sd_configs", None)
                    triton_sd = d.get("triton_sd_configs", None)
                    uyuni_sd = d.get("uyuni_sd_configs", None)
                    static_configs = d.get("static_configs", None)

            display.v(f"  - name: {keys}")

            if azure_sd:
                present.append("azure")
            if consul_sd:
                present.append("consul")
            if dns_sd:
                present.append("dns")
            if static_configs:
                present.append("static_configs")



        return []
