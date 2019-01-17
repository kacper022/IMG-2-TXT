import cv2

nazwa = input("Przeciagnij plik: ")
img = cv2.imread(nazwa)
file = open("converted.txt", 'w+')

for y in range(0, img.shape[0]):
    for x in range(0, img.shape[1]):
        srednia = img[y][x][0]+img[y][x][1]+img[y][x][2]
        if(srednia/3>25 and srednia/3<=54):
            file.write('@')
        elif(srednia/3>=55 and srednia/3<=72):
            file.write('$')
        elif(srednia>=73 and srednia<=127):
            file.write('#')
        else:
            file.write(' ')
    file.write('\n')
