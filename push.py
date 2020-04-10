#!/usr/bin/env python

def get_commands(x, y):
    command = []       
    command.append('vlan ' + x)   
    command.append('name ' + y)
    return command


def push_commands(x, y):
    print('Connecting to device: ' + x)
    for cmd in y:
        print('Sending command: ' + cmd)


if __name__ == "__main__":

    devices = ['switch1', 'switch2', 'switch3']

    vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'}, {'id': '30', 'name': 'WLAN'}]

    for vlan in vlans:
        vid = vlan.get('id')
        name = vlan.get('name')
        print('\n')
        print('CONFIGURING VLAN:' + vid)
        
        commands = get_commands(vid, name)
        for device in devices:
            push_commands(device, commands)
            print('\n')

