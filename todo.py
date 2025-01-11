to_do_list = []

def add_task(task):
    to_do_list.append(task)
    return f'Added: {task}'

def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        return f'Removed: {task}'
    return f'Task not found: {task}'

def view_tasks():
    if not to_do_list:
        return 'Your to-do list is empty.'
    return '\n'.join(f'{i + 1}. {task}' for i, task in enumerate(to_do_list))
