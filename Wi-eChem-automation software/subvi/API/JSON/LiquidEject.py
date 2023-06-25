import DeviceSingleOperation as op


def liquid_eject(worker_id, volume, process_data):
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 38, 100)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 60, 10)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 64, 5)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 68, 5)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 72, 5)
    process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', -volume, 20.0, 2.0)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 38, 50)
    return process_data
