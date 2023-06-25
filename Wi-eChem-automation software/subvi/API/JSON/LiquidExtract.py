import DeviceSingleOperation as op


def liquid_extract(worker_id, source_id, volume, process_data):
    k = ord(source_id)
    # A→65
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 1, 100)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 2, 10)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, k - 40, 100)
    process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', 0.2, 2.0, 0.0)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, k - 50, 10)
    process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', volume, 10.0, 3.0)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, k - 40, 50)
    # process_data[str(len(process_data) + 1)] = op.robot(worker_id, k - 40, 50)
    # process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', 0.2, 2.5, 1.0)
    # process_data[str(len(process_data) + 1)] = op.robot(worker_id, k - 50, 8)
    # process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', volume, 2.5, 1.0)
    # process_data[str(len(process_data) + 1)] = op.robot(worker_id, k - 40, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 1, 100)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 2, 10)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 9, 100)
    return process_data
