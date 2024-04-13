from math import *
from constants import *


class System:

    def __init__(self, object_array):
        self.object_array = []
        for object in object_array:
            self.object_array.append(object)

    def __distance(self, id_1, id_2):
        object_1 = [obj for obj in self.object_array if obj.id == id_1][0]
        object_2 = [obj for obj in self.object_array if obj.id == id_2][0]
        distance = sqrt(pow(object_1.x - object_2.x, 2) + pow(object_1.y - object_2.y, 2))
        return distance
    
    def __sign(self, a):
        if a > 0:
            return 1
        elif a < 0:
            return -1
        else: 
            return 0


    def force(self, object_id):
        force_value = [0, 0]
        object = [obj for obj in self.object_array if obj.id == object_id][0]
        for obj in self.object_array:
            if(obj.id == object_id):
                continue
            else:
                force_value[0] += -1*G*(object.mass)*(obj.mass)/(pow(self.__distance(object_id, obj.id), 3))*(object.x - obj.x)
                force_value[1] += -1*G*(object.mass)*(obj.mass)/(pow(self.__distance(object_id, obj.id), 3))*(object.y - obj.y)
        return force_value
