import os

path_basic = os.getcwd() # 현재 폴더
print(path_basic)

folder_1 = os.listdir(path_basic)
print(folder_1)

codes = []
with open('C예제코드.txt', 'w') as f_result: # 결과 저장
    for dirt in folder_1:
        print(dirt)
        f_result.write(dirt) # 몇 장인지 쓰기
        f_result.write("=====================")
        f_result.write('\n')
        if(os.path.isdir(dirt)):
            folder_2 = os.listdir(path_basic + '/' + dirt)
            # print(folder_2)

            for cfile in folder_2:
                if(cfile[-2:] == '.c' or cfile[-4:] == '.cpp' or cfile[-2:] == '.h'):
                    print(cfile)
                    # codes.append(cfile[:-2])
                    f_result.write(dirt)  # 몇 장인지 쓰기
                    f_result.write('-')
                    f_result.write(cfile)
                    f_result.write('\n')
                    cfile = path_basic + '/' + dirt + '/' + cfile
                    try:
                        with open(cfile, 'r', encoding='utf-8-sig') as f:
                            lines = f.readlines()
                            # codes.append(line)
                            f_result.writelines(lines)
                    except:
                        with open(cfile, 'r') as f:
                            lines = f.readlines()
                            # codes.append(line)
                            f_result.writelines(lines)
                    f_result.write('\n\n\n')


