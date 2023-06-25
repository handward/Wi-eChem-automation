import xlrd
from os import path


def robot(worker_id, action_no, speed):
    root = path.abspath(path.dirname(__file__))
    file_path = path.join(root, 'RobotActionNo.xlsx')
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheets()[0]
    values = worksheet.row_values(action_no)
    # According to action_no read parameters
    command = 'x = ' + str(values[2]) + ', y = ' + str(values[3]) + ', z = ' + str(values[4]) + ', r = ' + str(values[5]) + ', speed = ' + str(speed) + ', rough = ' + str(values[6])
    robot_para = {'device': 'robot', 'operation': {'ID': worker_id, 'command': command}}
    return robot_para


def pump(worker_id, channel, volume, rate, wait_time):
    command = 'channel = ' + channel + ', volume = ' + str(volume) + ', rate = ' + str(rate) + ', wait_time = ' + str(wait_time)
    pump_para = {'device': 'pump', 'operation': {'ID': worker_id, 'command': command}}
    return pump_para


def power_supply(worker_id, voltage):
    command = str(voltage)
    if worker_id == 1 or worker_id == 2:
        power_supply_para = {'device': 'power_supply1', 'operation': {'ID': worker_id, 'command': command}}
    else:
        power_supply_para = {'device': 'power_supply2', 'operation': {'ID': worker_id, 'command': command}}
    return power_supply_para


def motor(worker_id, block):
    motor_para = {'device': 'motor', 'operation': {'ID': worker_id, 'command': block}}
    return motor_para


def robot_efg(worker_id, distance):
    command = 'distance = ' + str(distance)
    robot_efg_para = {'device': 'robot_efg', 'operation': {'ID': worker_id, 'command': command}}
    return robot_efg_para


def public_device_occupy(worker_id, public_device, skip_value):
    public_device_occupy_para = {'device': 'public_device_occupy',
                                 'operation': {'ID': worker_id, 'command': public_device, 'skip command': skip_value}}
    return public_device_occupy_para


def public_device_unoccupy(worker_id, public_device):
    public_device_unoccupy_para = {'device': 'public_device_unoccupy',
                                   'operation': {'ID': worker_id, 'command': public_device}}
    return public_device_unoccupy_para


def wait(worker_id, value):
    wait_para = {'device': 'wait'+str(worker_id), 'operation': value}
    return wait_para


def skip_latter(value):
    skip_para = {'device': 'skip_latter', 'operation': value}
    return skip_para


def skip_former(value):
    skip_para = {'device': 'skip_former', 'operation': value}
    return skip_para
