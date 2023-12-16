import os
import copy
from model import *
import random
import shutil


base_path = "D:/AtomicHack/DATASET/"
frame_path = "FRAMES/"
classes_path = "metadata/classes.cfg"
path_set = "metadata/set.cfg"
path_test_set = "metadata/test_set.cfg"


def search_files(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".bmp"):
                file_path = os.path.join(root, file)
                file_list.append(file_path)
    return file_list

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def remove_newline(lines):
    return [line.rstrip('\n') for line in lines]

def check_dataset(pictures):
    count_exists_file = 0
    count_not_exists_file = 0

    for picture in pictures:
        path = picture.find_real_path(base_path + frame_path)
        if os.path.exists(path):
            count_exists_file += 1
        else:
            count_not_exists_file += 1

    print(f"Файлов существует {count_exists_file}")
    print(f"Файлов не существует {count_not_exists_file}")


def get_pictures(info):
    parsed_picture = []
    current_file = None
    
    for item in info:
        if item.endswith('.frame') or item.endswith('.bmp') :
            if current_file is not None:
                parsed_picture.append(copy.deepcopy(current_file))
            
            current_file = None   
            current_file = PictureFrame(item)
        else:
            line_number = item.split(', ')
            defect = Defect(line_number[2], line_number[0], line_number[1])
            current_file.set_defect(defect)
    return parsed_picture


def create_and_write_file(file_path: str, lines: list):
    try:
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        return f"Файл {file_path} успешно создан и записаны строки."
    except Exception as e:
        return f"Ошибка при создании файла и записи строк: {str(e)}"



def create_data(pictures_list, destination_path):
    file_number = 0
    for picture in pictures_list:
        file_number = file_number + 1
        originals_full_path = picture.find_real_path(base_path + frame_path)
        picture_dist = f"{destination_path}images/"
        
        if  not os.path.exists(picture_dist):
            os.makedirs(picture_dist)
        
        shutil.copy(originals_full_path, picture_dist + f"{file_number}_{picture.get_file()}.bmp")
        
        label_dist = f"{destination_path}/labels/"
        if  not os.path.exists(label_dist):
            os.makedirs(label_dist)
        
        create_and_write_file(label_dist + f"{file_number}_{picture.get_file()}.txt", picture.get_defects_list())



files_from_disk = remove_newline(search_files(base_path + frame_path))
filtered_frames_files_from_disk = [frame for frame in files_from_disk if ".bmp" in frame]

classes_info = remove_newline(read_file(base_path + classes_path))
set_info = remove_newline(read_file(base_path + path_set))
test_set_info = remove_newline(read_file(base_path + path_test_set))

#Изображения
pictures_set = get_pictures(set_info)
pictures_set = [frame for frame in pictures_set if frame.exists(base_path + frame_path)]
#pictures_test_set = get_pictures(test_set_info)


#print(f"Датасет для обучения")
check_dataset(pictures_set)

pictures_set = [element for element in pictures_set if not element.defect_list_broken()]

random.shuffle(pictures_set)
to_validate = pictures_set[:80]
del pictures_set[:100]

to_test= pictures_set[:600]
del pictures_set[:700]

to_train = pictures_set


create_data(to_train,"D:/AtomicHack/UniProject/ModelYolo/train/")
create_data(to_test,"D:/AtomicHack/UniProject/ModelYolo/test/")
create_data(to_validate,"D:/AtomicHack/UniProject/ModelYolo/valid/")



