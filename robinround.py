class User:

    def __init__(self, id, bust_time, b_time, arrival_time):
        self.id = id
        self.bust_time = bust_time
        self.b_time = b_time
        self.arrival_time = arrival_time


def round_robin(processes: list, time_quantum: int):
    queue = []
    completed_processes = []
    report = []
    average_wait_time = 0
    current_time = 0
    # print("this is current",current_time)
    queue = processes
    queue_size = len(queue)

    while queue:
        current_transaction = queue.pop(0)
        if current_transaction.bust_time <= time_quantum:
            current_time += current_transaction.bust_time
            current_transaction.bust_time = current_time
            completed_processes.append(current_transaction)

        else:
            current_time += time_quantum
            remaining_time = current_transaction.bust_time - time_quantum
            current_transaction.bust_time = remaining_time
            queue.append(current_transaction)

    for i in range(queue_size):
        completed_tasks = completed_processes[i]
        name_of_completed_task = completed_tasks.id
        completed_tasks_bust_time_original = completed_tasks.b_time
        turn_around_time = completed_tasks.bust_time - completed_tasks.arrival_time
        wait_time = turn_around_time - completed_tasks_bust_time_original
        average_wait_time += wait_time
        print(name_of_completed_task, completed_tasks_bust_time_original, turn_around_time, wait_time)
        report.append(
            (name_of_completed_task, completed_tasks_bust_time_original, turn_around_time, wait_time))
    average_wait_time = average_wait_time / queue_size

    return {'report': report, 'average_wait_time': average_wait_time}

# test of case of the round_robin algorithm.
# sage = User('sage', 100, 100, 0)
# jerry = User('jerry', 100, 100, 0)
# round_robin([sage, jerry], 4)
