from datetime import datetime

def log_action(action, text, result):
    with open("results.txt", "a") as f:
        f.write("\n--- LOG ---\n")
        f.write(str(datetime.now()) + "\n")
        f.write("Action: " + action + "\n")
        f.write("Input: " + text + "\n")
        f.write("Result: " + result + "\n")