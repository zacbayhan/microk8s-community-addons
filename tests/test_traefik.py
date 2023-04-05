import pytest
import platform

from utils import (
    microk8s_disable,
    microk8s_enable,
    wait_for_pod_state,
)


class TestTraefik(object):
    @pytest.mark.skipif(platform.machine() == "s390x", reason="Not available on s390x")
    def test_traefik(self):
        """
        Sets up and validates traefik.
        """
        print("Enabling traefik")
        microk8s_enable("traefik")
        print("Validating traefik")
        self.validate_traefik()
        print("Disabling traefik")
        microk8s_disable("traefik")

    def validate_traefik(self):
        """
        Validate traefik
        """
        wait_for_pod_state(
            "", "traefik", "running", label="app.kubernetes.io/name=traefik"
        )
