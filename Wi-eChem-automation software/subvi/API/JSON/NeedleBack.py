import DeviceSingleOperation as op


def needle_back(worker_id, process_data):
    j = len(process_data)
    process_data[str(j + 1)] = op.robot(worker_id, 9, 50)
    process_data[str(j + 2)] = op.robot(worker_id, 14, 50)
    process_data[str(j + 3)] = op.robot(worker_id, 13, 10)
    process_data[str(j + 4)] = op.robot(worker_id, 12, 50)
    process_data[str(j + 5)] = op.robot_efg(worker_id, 0)
    process_data[str(j + 6)] = op.robot(worker_id, 11, 100)
    process_data[str(j + 7)] = op.robot(worker_id, 10, 100)
    process_data[str(j + 8)] = op.robot(worker_id, 9, 100)
    return process_data
