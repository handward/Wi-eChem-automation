import DeviceSingleOperation as op


def needle_clean(worker_id, volume, process_data):
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 44, 50)
    process_data[str(len(process_data) + 1)] = op.robot(worker_id, 43, 10)
    if volume == 0:
        process_data[str(len(process_data) + 1)] = op.motor(5, 'block4')
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 44, 50)
    else:
        process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'E', volume, 20.0, 2.0)
        process_data[str(len(process_data) + 1)] = op.pump(worker_id, 'O', -volume, 20.0, 2.0)
        process_data[str(len(process_data) + 1)] = op.motor(5, 'block4')
        process_data[str(len(process_data) + 1)] = op.robot(worker_id, 44, 50)
    return process_data
