def ms_to_min_sec(ms):
    minutes = int(ms // 60000)
    seconds = int((ms % 60000) // 1000)
    return f"{minutes}:{seconds:02}"

