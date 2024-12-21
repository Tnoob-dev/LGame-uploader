def ask_on_off(num: int):
    while True:
        if num == 1:
            # Online
            return True
        elif num == 2:
            # Offline
            return False
        else:
            # Any other answer
            return None