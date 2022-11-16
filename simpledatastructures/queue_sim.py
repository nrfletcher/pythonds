import random
from queue import Queue


# A simulation of a printer which has a queue that takes print requests and executes them if the printer is ready
class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, newtask):
        self.current_task = newtask
        self.time_remaining = newtask.get_pages() * 60/self.page_rate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, currenttime):
        return currenttime - self.timestamp


def simulation(num_seconds, pages_per_minute):
    printer = Printer(pages_per_minute)
    queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        # We use this to simulate randomness, an average of 1 print per 180 seconds
        if new_print_task():
            task = Task(current_second)
            queue.enqueue(task)

        # If the printer is free and a task is queued
        if not printer.busy() and not queue.is_empty():
            # Take out next task, append the initial time - current time to get wait time, and start said task
            next_task = queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            printer.start_next(next_task)

        printer.tick()

    average_wait = sum(waiting_times)/len(waiting_times)
    print("Average wait %6.2f secs %3d tasks remaining." % (average_wait, queue.size()))
    return [average_wait, queue.size()]


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulations():
    stats = []
    page_tests = [5, 10, 15, 20, 25]

    for i in range(len(page_tests)):
        sim = simulation(3600, page_tests[i])
        stats.append(['Average wait: ' + str(round(sim[0], 2)), 'Tasks left: ' + str(round(sim[1], 2))])

    return stats


print(simulations())
