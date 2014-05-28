import sys,os
import csv
for ls_cmd in sys.stdin:
    filename = ls_cmd.rstrip()
    if not filename.endswith('.csv'):
        continue

    print filename 
    csv_file = open(filename, 'r')
    ofile = open('./data/'+filename, 'wb')
    file_content = []
    data_file = csv.reader(csv_file)
    temp = next(data_file)
    target_id = temp[0][10:-1]
    target_gender = temp[2]
    n_hex = 0
    n_features = 2

    for hex_info in data_file:
        if(hex_info):
            file_content.append(hex_info)
            n_hex = n_hex + 1

    ofile.write(''.join(str(n_hex) + ' ' + str(n_features) + ' ' + target_id + ' ' + target_gender + '\n'))
    for i in range(1, n_hex):
        ofile.write(''.join(file_content[i][0] + ' ' + file_content[i][2] + ' ' + file_content[i][2+int(file_content[i][2])+2]) + '\n')
    csv_file.close()
    ofile.close()
