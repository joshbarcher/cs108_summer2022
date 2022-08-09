# open the file of points, remove duplicates, then write the unique points to a new file
with open("../datasets/points.txt", "r") as readFile:
    with open("../datasets/points_unique.txt", "w") as writeFile:
        lines = readFile.readlines()
        print(f"List: {lines}")
        print(f"Lines in original file: {len(lines)}")

        # declare an empty set
        set = set()

        for point in lines:
            set.add(point)

        for point in set:
            writeFile.write(point)

        print(f"Set: {set}")
        print(f"Number of unique points: {len(set)}")





