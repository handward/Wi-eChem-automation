import DeviceSingleOperation as op


def sample_from_reactor(worker_id, volume, process_data):
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 38, 50)
    process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', 0.2, 2.0, 0.5)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 60, 5)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 64, 5)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 68, 5)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 72, 5)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 34, 5)
    process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', volume, 10.0, 2.0)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, worker_id + 38, 50)
    return process_data
