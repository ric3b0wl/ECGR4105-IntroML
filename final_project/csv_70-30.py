csv_data = []
with open ('dataset_70k.csv') as file:
    csv_data.append(file.read())
csv_data = (''.join(csv_data)).split("\n")
header = csv_data[0]
csv_data = csv_data[1:]
temp_list = []
add_header = True
for i in csv_data:
    if len(temp_list) == 0:
        temp_list.append(i)
    elif i.split(',')[0] == temp_list[0].split(',')[0]:
        temp_list.append(i)
    else:
        file_length = len(temp_list)
        line_count = int((0.7*file_length)+1)
        if line_count == 1:
            with open("train.csv","a+") as file1:
                if add_header:
                    add_header = False
                    file1.write(header+'\n')
                file1.write(temp_list[0]+'\n')
        else:
            seventy_perc_lines = temp_list[:line_count]
            thirty_perc_lines = temp_list[line_count:]
            if add_header:
                seventy_perc_lines.insert(0,header)
                thirty_perc_lines.insert(0,header)
                add_header = False
            with open("train.csv","a+") as file1:
                for j in range(len(seventy_perc_lines)):
                    file1.write(seventy_perc_lines[j]+'\n')
            if len(thirty_perc_lines) != 0:
                with open("test.csv","a+") as file2:
                    for j in range(len(thirty_perc_lines)):
                        file2.write(thirty_perc_lines[j]+'\n')
        temp_list = []
        temp_list.append(i)