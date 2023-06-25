import DeviceSingleOperation as op


def sample_to_filter_vial(worker_id, process_data):
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 9, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 1, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 2, 10)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 50, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 49, 10)
    process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'E', 0.2, 20.0, 2.0)
    process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', -1.2, 20.0, 2.0)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 50, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 1, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 2, 10)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 9, 50)
    return process_data
