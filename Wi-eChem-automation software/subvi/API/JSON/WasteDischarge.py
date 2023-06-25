import DeviceSingleOperation as op


def waste_discharge(worker_id, volume, process_data):
    if worker_id == 1 or worker_id == 3:
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 47, 50)
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 45, 10)
        process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'E', volume, 20.0, 2.0)
        process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', -volume, 20.0, 2.0)
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 47, 50)
    else:
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 48, 50)
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 46, 10)
        process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'E', volume, 20.0, 2.0)
        process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', -volume, 20.0, 2.0)
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 48, 50)
    return process_data
