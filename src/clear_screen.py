import os


def clear_screen():
    """Clears the terminal screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')