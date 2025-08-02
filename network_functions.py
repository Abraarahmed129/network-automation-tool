# We are commenting out the netmiko import because we won't be using it for this mock version.

# This is our pre-written, fake data for the 'show version' command.
# It looks just like the real output from a Cisco router.
MOCK_SHOW_VERSION_OUTPUT = """
Cisco IOS XE Software, Version 16.09.03
Cisco IOS Software [Fuji], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.3, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2019 by Cisco Systems, Inc.
Compiled Wed 24-Jul-19 02:07 by mcpre

Router uptime is 3 weeks, 2 days, 1 hour, 32 minutes
System returned to ROM by reload
System image file is "bootflash:packages.conf"
Last reload reason: "Normal Reload"

This is a sandbox version.

Technology Package License Information for 'network-advantage'
-----------------------------------------------------------------
Technology    Technology-package          Technology-package
              Current       Type          Next reboot
------------------------------------------------------------------
network-advantage   network-advantage   Smart License         None
dna-advantage       dna-advantage       Subscription          None

"""

def get_device_info(device_credentials):
    """
    This is now a MOCK function.
    It IGNORES the credentials and returns pre-defined text.
    """
    print("--- MOCKING: Returning fake device info ---")
    return MOCK_SHOW_VERSION_OUTPUT

def configure_vlan(device_credentials, vlan_id, vlan_name):
    """
    This is now a MOCK function.
    It IGNORES the credentials and returns a fake success message.
    """
    print(f"--- MOCKING: Pretending to configure VLAN {vlan_id} named {vlan_name} ---")
    # We create a fake output string that looks like what a real router would return.
    output = f"""
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)# vlan {vlan_id}
Router(config-vlan)# name {vlan_name}
Router(config-vlan)# end
"""
    return output

# def get_device_info(device_credentials):
#     "Connects to a network device and returns its 'show version' output."
#     try:
#         with ConnectHandler(**device_credentials) as net_connect:
#             output = net_connect.send_command('show version', use_textfsm=True)
#             return output
#     except Exception as e:
#         return f"Failed to connect or get info: {e}"

# def configure_vlan(device_credentials, vlan_id, vlan_name):
#     """Connects to a device and configures a VLAN with a specific ID and name."""
#     try:
#         with ConnectHandler(**device_credentials) as net_connect:
#             commands_to_send = [
#                 f'vlan {vlan_id}',
#                 f'name {vlan_name}'
#             ]
#             output = net_connect.send_config_set(commands_to_send)
#             return output
#     except Exception as e:
#         return f"Failed to configure VLAN: {e}"
