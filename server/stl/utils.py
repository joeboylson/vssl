from solid2 import cube


def generate_steps(start, end, number_of_steps):
    """Generates a list of numbers equally spaced across a range

    Args:
        numbers: A list of numbers.
        start: The number to start from
        end: The number to end at
        number_of_steps: the number of steps required in between

    Returns:
        A list of numbers equally spaced across a range
    """

    if number_of_steps < 2:
        raise ValueError("Number of steps must be at least 2.")

    step_size = (end - start) / (number_of_steps - 1)
    return [start + i * step_size for i in range(number_of_steps)]


def generate_starting_model():
    """Returns a cube of size 0

    Args:

    Returns:
        A solid2 cube
    """

    return cube(0)
