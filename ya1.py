class Robot:

    def __init__(self, point):
        if not (isinstance(point[0],int) and isinstance(point[1],int)):
            raise ValueError("Incorrect type!")

        if (point[0] or point[1])<0 or (point[0] or point[1])>100:
            raise ValueError("Incorrect value range!")
        self.init_point = point        
        self.robot_path = [self.init_point]
        self.directions = {'N':(0,1),'S':(0,-1), 'W':(-1,0),'E':(1,0)} 


    def move(self, path):
        #if ()
        current_point = self.init_point
        for direction in path:            
            current_point = self.__sum_points__(current_point, self.directions[direction])
            self.robot_path.append(current_point)
        return self.robot_path[-1]

    def __round_edge__(self, edge):
        if edge > 100:
            edge = 100
        if edge < 0:
            edge = 0
        return edge

    def __sum_points__(self, first_point, second_point):        
        raw_point = tuple(map(sum, zip(first_point, second_point)))         
        point = (self.__round_edge__(raw_point[0]), self.__round_edge__(raw_point[1]))        
        return point

    def path(self):        
        return tuple(self.robot_path)



r= Robot((0,0))
print(r.move(''))
print(*r.path())  