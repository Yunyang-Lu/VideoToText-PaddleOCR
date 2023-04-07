from EditDistance import editDistDP

def getAvgEditDist (file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    linecount = 0
    ED = 0
    totalEdit = 0

    #readline of two files and compare the edit distance
    while True: 
        line1 = f1.readline()
        line2 = f2.readline()

        if line1 == "" and line2 == "":     #indicates end of the files
            return totalEdit/linecount
        elif line1 == "" and line2 != "" or line1 != "" and line2 == "":    #file with different linecount
            print("two files having different line count!")
            return 0
        else:
            linecount += 1
            print (line1, end ="")
            print (line2, end ="")
            # Adding the Edit distance of the current line
            ED = editDistDP(line1, line2, len(line1), len(line2))
            print("Minimum Edit Distance: ", ED)
            print()
            totalEdit += ED


print("Average Edit distance: ", getAvgEditDist("./result.txt", "./resultGT.txt"))