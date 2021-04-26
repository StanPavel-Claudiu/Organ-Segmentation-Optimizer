import sys, cv2

#program to convert from image to input file
path = r'C:\Users\TiCk3t\PycharmProjects\DICOM_segm_optimizer\input3\121.2-seg.jpg'
multi_seg_demo = cv2.imread(path, 0)

ret, thresh = cv2.threshold(multi_seg_demo, 127, 255, 0)
output = []
out_file = open(sys.argv[2], 'w')
for i in range(len(thresh)):
    for j in range(len(thresh)):
        if thresh[i][j] != 0:
            output.append("1 ")
        else:
            output.append("0 ")
    if i < len(thresh) - 1:
        output.append("\n")

out_file.writelines(output)


