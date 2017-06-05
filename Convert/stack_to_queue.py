from Convert.pylistqueue import Queue


def stack_to_queue(stack):
    """
    Convert Stack to Queue
    """
    queue = Queue()
    check_list = []

    while len(stack) != 0:
        check_list.append(stack.pop())

    check_list.reverse()

    while check_list != []:
        queue.enqueue(check_list[0])
        check_list.remove(check_list[0])
