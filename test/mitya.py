def main(x):
    x = x.split(" ")
    for i in range(0, len(x)):
        if x[i] != "None":
            return int(x[i])
    return None

print(main("None None None"))