import os
import shutil
def rename(path, file_list=None):
    _tmp_dir_name = ''
    _file_list = file_list or []
    ff = os.walk(path)
    for root, dirs, files in ff:
        if dirs:
            _tmp_dir_name = dirs[0]
        for file in files:
            _rawname = os.path.join(root, file)
            # _rename =
            shutil.move(_rawname, os.path.join('C:\\Users\\admin\\Downloads\\Video', f'{_tmp_dir_name}_{file}'))

            # print(_tmp_dir_name + '_' + file)
            # print(dir(file))
            # break
            # print(_rawname, '==', _rename)
            # os.rename(_rawname, _rename)

            # _file_list.append(_rename)
    return _file_list

xx = rename("C:\\Users\\admin\\Downloads\\Video")
# print(xx)
# print(walk("C:\\Users\\admin\\Downloads\\Video"))

