def export_result(result):
    with open("results.txt", "a") as f:
        f.write(result + "\n")