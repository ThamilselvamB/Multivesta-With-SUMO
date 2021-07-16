#  Wiedemann  Krauss  IDM   
import fileinput
replaceValue = """carFollowModel="Wiedemann" """
replaceToValue = """carFollowModel="Krauss" """
for i in range(1,21):
 filename = "cross_"+str(i) +".rou.xml"
 with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(replaceValue, replaceToValue), end='')
