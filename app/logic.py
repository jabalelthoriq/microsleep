def decide_state(eye, mouth):
    if eye == "closed":
        return "MICROSLEEP"
    elif mouth == "yawn":
        return "YAWNING"
    else:
        return "NORMAL"
