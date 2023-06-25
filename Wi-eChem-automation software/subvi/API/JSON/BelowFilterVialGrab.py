import DeviceSingleOperation as op


def below_filter_vial_grab(worker_id, process_data):
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 1, 100)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 2, 10)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 3, 100)
    process_data[str(len(process_data) + 1)] = op.robot_efg(worker_id, 13)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 4, 50)
    process_data[str(len(process_data) + 1)] = op.robot_efg(worker_id, 16)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 3, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 5, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 6, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 7, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 8, 50)
    process_data[str(len(process_data) + 1)] = op.robot_efg(worker_id, 10)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 7, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 6, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 5, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 1, 100)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 2, 10)
    return process_data
