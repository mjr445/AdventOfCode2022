from sys import argv

def build_queue(raw_queue):
    queues = {}
    stack_names = raw_queue[-1].strip().split()
    number_of_stacks = int(stack_names[-1])
    for stack_name in stack_names:
        queues[stack_name] = []
    cargo_indices = [1]
    for _ in range(number_of_stacks - 1):
        cargo_indices.append(cargo_indices[-1] + 4)
    for line in reversed(raw_queue[:-1]):
        for stack_name, index in enumerate(cargo_indices):
            value = line[index]
            if value.strip():
                queues[str(stack_name + 1)].append(value)

    return queues

def main():
    raw_queue = []
    queue_built = False
    with open(argv[1], 'r', encoding='utf8') as input_file:
        for line in input_file.readlines():
            if not queue_built:
                if not line.strip():
                    queues = build_queue(raw_queue)
                    queue_built = True
                else:
                    raw_queue.append(line)
            else:
                line_list = line.strip().split()
                number_of_cargo_moved = int(line_list[1])
                source_stack = line_list[3]
                destination_stack = line_list[5]

                moving_stack = []
                for _ in range(number_of_cargo_moved):
                    cargo_being_moved = queues[source_stack].pop()
                    moving_stack.append(cargo_being_moved)
                for _ in range(number_of_cargo_moved):
                    queues[destination_stack].append(moving_stack.pop())

    for stack in queues.values():
        print(stack.pop(), end='')
    print()

if __name__ == "__main__":
    main()
