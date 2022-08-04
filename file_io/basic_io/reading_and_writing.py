# open a reader and writer
with open("song.txt", "r") as reader:
    with open("song_abbreviated.txt", "w") as writer:
        # get a list of the lines in the file
        songLines = reader.readlines()

        # loop over the list
        for line in songLines:
            if not ("[4x]" in line):
                writer.write(line)
            else:
                print(f"Ignored the line - {line}", end='')

