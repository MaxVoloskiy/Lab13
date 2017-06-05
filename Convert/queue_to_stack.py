from Convert.pyliststack import Stack


def queue_to_stack(queue):
    """
    Convert Queue to Stack
    """
    stack = Stack()
    check_list = []

    while len(queue) != 0:
        check_list.append(queue.dequeue())

    check_list.reverse()

    while check_list != []:
        stack.push(check_list[0])
        check_list.remove(check_list[0])
