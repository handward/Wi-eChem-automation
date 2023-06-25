import DeviceSingleOperation as op
from SampleFromReactor import sample_from_reactor
from LiquidEject import liquid_eject


def reactor_clean(worker_id, process_data):
    process_data = sample_from_reactor(worker_id, 4.5, process_data)
    if worker_id == 1 or worker_id == 3:
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 47, 50)
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 45, 10)
        process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', -4.5, 20.0, 3.0)
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 47, 50)
    else:
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 48, 50)
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 46, 10)
        process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', -4.5, 20.0, 3.0)
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 48, 50)
    for i in range(1, 3):
        process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'E', 3.5, 20.0, 3.0)
        process_data = liquid_eject(worker_id, 3.5, process_data)
        process_data[str(len(process_data) + 1)] = op.motor(worker_id, 'block3')
        process_data = sample_from_reactor(worker_id, 4.0, process_data)
        if worker_id == 1 or worker_id == 3:
            process_data[str(len(process_data) + 1)] = op.robot(worker_id, 47, 50)
            process_data[str(len(process_data) + 1)] = op.robot(worker_id, 45, 10)
            process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', -4.0, 20.0, 3.0)
            process_data[str(len(process_data) + 1)] = op.robot(worker_id, 47, 50)
        else:
            process_data[str(len(process_data) + 1)] = op.robot(worker_id, 48, 50)
            process_data[str(len(process_data) + 1)] = op.robot(worker_id, 46, 10)
            process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', -4.0, 20.0, 3.0)
            process_data[str(len(process_data) + 1)] = op.robot(worker_id, 48, 50)
    return process_data
