import os
from PIL import Image

class Defect:
    def __init__(self, class_num: int, X: int, Y: int):
        self.class_num = class_num
        self.X = int(X)
        self.Y = int(Y)


    def prepare_opposite_point(self, value):
        return round(value, 6)

    
    def get_opposite_points(self, width, height):
        w = self.prepare_opposite_point(160 / width)
        h = self.prepare_opposite_point(160 / height)
        x = self.prepare_opposite_point(self.X / width)
        y = self.prepare_opposite_point(self.Y / height)
        
        return [x, y, w, h]

class PictureFrame:
    def __init__(self, file_path: str):
        self.file_path = file_path.replace(".frame",".bmp")
        self.defects = []
        self.full_path_drive = ""

    def set_defect(self, defect: Defect):
        self.defects.append(defect)
        
    def find_real_path(self, path:str):
        result_path = (path + self.file_path.replace('0\\', '')).replace("\\", '/')
        self.full_path_drive = result_path
        return result_path

    def get_file(self):
        base_name = os.path.basename(self.full_path_drive)
        return os.path.splitext(base_name)[0]

    def exists(self, path:str):   
        return os.path.exists(self.find_real_path(path))  

    def get_resolution(self):
        with Image.open(self.full_path_drive) as img:
            width, height = img.size
            return width, height

    def get_defects_list(self):
        width, height = self.get_resolution()
        defect_info = []
        for defect in self.defects:
            if defect.class_num == '0':
                continue

            points = defect.get_opposite_points(width, height)
            string_with_spaces = ' '.join(map(str, points))
            defect_info.append(f"{defect.class_num} {string_with_spaces}")
        return defect_info
    
    def defect_list_broken(self):
        list_detects_data = self.get_defects_list()
        for data in list_detects_data:
            if "1." in data:
                return True
        
        return False
        
