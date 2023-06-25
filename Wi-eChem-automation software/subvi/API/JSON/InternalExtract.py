import DeviceSingleOperation as op


def internal_extract(worker_id, process_data):
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 1, 100)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 2, 10)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 34, 50)
    process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', 0.2, 2.0, 0.0)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 24, 10)
    process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', 0.5, 10.0, 1.0)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 34, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 1, 100)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 2, 10)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 9, 100)
    return process_data
