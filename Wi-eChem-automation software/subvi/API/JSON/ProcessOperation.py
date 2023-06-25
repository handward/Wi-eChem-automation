import DeviceSingleOperation as op
from NeedleGrab import needle_grab
from LiquidExtract import liquid_extract
from LiquidEject import liquid_eject
from NeedleClean import needle_clean
from WasteDischarge import waste_discharge
from NeedleBack import needle_back
from BelowFilterVialGrab import below_filter_vial_grab
from SampleFromReactor import sample_from_reactor
from SampleToFilterVial import sample_to_filter_vial
from UpperFilterVialGrab import upper_filter_vial_grab
from ReactorClean import reactor_clean
from InternalExtract import internal_extract


def preparation(source_id, volume, worker_id, process_data):
    process_data[str(len(process_data) + 1)] = op.public_device_occupy(worker_id, 'robot, pump, relay', 'liquid extract from ' + str(source_id) + str(worker_id))
    process_data[str(len(process_data) + 1)] = op.skip_former('liquid extract from ' + str(source_id) + str(worker_id))
    process_data = needle_grab(worker_id, process_data)
    # 7
    process_data = liquid_extract(worker_id, source_id, volume, process_data)
    process_data = liquid_eject(worker_id, 4.2, process_data)
    process_data[str(len(process_data) + 1)] = op.motor(worker_id, 'block1')
    process_data[str(len(process_data) + 1)] = op.skip_latter('liquid extract from ' + str(source_id) + str(worker_id))
    process_data = waste_discharge(worker_id, 4.5, process_data)
    # 5
    process_data = needle_clean(worker_id, 0, process_data)
    # 4
    process_data = needle_back(worker_id, process_data)
    # 8
    process_data[str(len(process_data) + 1)] = op.public_device_unoccupy(worker_id, 'robot, pump, relay')
    process_data['number of steps'] = len(process_data)
    return process_data


def reaction(worker_id, voltage, time, process_data):
    j = len(process_data)
    process_data[str(j + 1)] = op.power_supply(worker_id, voltage)
    process_data[str(j + 2)] = op.wait(worker_id, time)
    process_data[str(j + 3)] = op.power_supply(worker_id, 0)
    process_data['number of steps'] = len(process_data)
    return process_data


def sample(worker_id, process_data):
    process_data[str(len(process_data) + 1)] = op.public_device_occupy(worker_id, 'robot, pump, relay', 'sample')
    process_data = below_filter_vial_grab(worker_id, process_data)
    process_data = needle_grab(worker_id, process_data)
    process_data = internal_extract(worker_id, process_data)
    # add internal
    process_data[str(len(process_data) + 1)] = op.motor(worker_id, 'block2')
    process_data = liquid_eject(worker_id, 0.4, process_data)
    process_data[str(len(process_data) + 1)] = op.motor(worker_id, 'block1')
    process_data = needle_clean(worker_id, 1.0, process_data)
    process_data[str(len(process_data) + 1)] = op.motor(worker_id, 'block2')
    process_data = sample_from_reactor(worker_id, 0.5, process_data)
    process_data = sample_to_filter_vial(worker_id, process_data)
    process_data = needle_clean(worker_id, 1.0, process_data)
    process_data = needle_back(worker_id, process_data)
    process_data = upper_filter_vial_grab(worker_id, process_data)
    process_data[str(len(process_data) + 1)] = op.public_device_unoccupy(worker_id, 'robot, pump, relay')
    process_data['number of steps'] = len(process_data)
    return process_data


def clean(worker_id, process_data):
    process_data[str(len(process_data) + 1)] = op.public_device_occupy(worker_id, 'robot, pump, relay', 'clean' + str(worker_id))
    process_data[str(len(process_data) + 1)] = op.skip_former('clean' + str(worker_id))
    process_data = needle_grab(worker_id, process_data)
    # 7
    process_data = reactor_clean(worker_id, process_data)
    process_data[str(len(process_data) + 1)] = op.skip_latter('clean' + str(worker_id))
    process_data = waste_discharge(worker_id, 4.5, process_data)
    process_data = needle_clean(worker_id, 0, process_data)
    process_data = needle_back(worker_id, process_data)
    process_data[str(len(process_data) + 1)] = op.public_device_unoccupy(worker_id, 'robot, pump, relay')
    process_data['number of steps'] = len(process_data)
    return process_data
