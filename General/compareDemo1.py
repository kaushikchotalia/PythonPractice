with open("file1.txt", encoding="utf8") as f:
    with open("file2.txt", encoding="utf8") as fe:
        for line in f:
            for linefe in fe:
                if (line != linefe):
                    print(line)
                    break
                else:
                    break