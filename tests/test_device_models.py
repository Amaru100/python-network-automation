from netauto.devices.device_models import NetworkDevice


def test_network_device_defaults_to_cisco_ios() -> None:
    device = NetworkDevice(name="SW1", host="192.168.10.11")

    assert device.device_type == "cisco_ios"
    assert device.port == 22
