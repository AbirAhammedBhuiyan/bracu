#!/usr/bin/env python3



#####################################################
##### Name     : Abir Ahammed Bhuiyan ###############
##### ID       : 20101197             ###############
##### Course   : CSE422               ###############
##### Section  : 05                   ###############
##### Semester : Spring 2024          ###############
#####################################################



import heapq



class AStar:
    def __init__(self, fileName, start, dest):
        self.start = start.lower()
        self.dest = dest.lower()
        self.city_info, self.heuristic = self.TakeInput(fileName)



    def run(self):
        path = self.FindPath(self.start, self.dest, self.city_info, self.heuristic)

        if path:
            distance = self.CalculateDistance(path, self.city_info)
            printPath = "Path: "
            for place in path:
                printPath +=  f"{place.capitalize()} -> "
            print(printPath[:-4])
            print(f"Total distance: {distance} km")
        else:
            print("NO PATH FOUND\n")


    
    def TakeInput(self, fileName):
        with open(fileName, 'r') as input_file:
            city_info = {}
            heuristic = {}
            
            while True:
                line = input_file.readline().lower()

                if not line:
                    break

                city_and_distance = line.split()
                heuristic[city_and_distance[0]] = int(city_and_distance[1])

                for i in range(2, len(city_and_distance), 2):
                    if city_and_distance[0] not in city_info:
                        city_info[city_and_distance[0]] = {}
                    city_info[city_and_distance[0]][city_and_distance[i]] = int(city_and_distance[i+1])

        return city_info, heuristic



    def CalculateDistance(self, path, graph):
        distance = 0
        for i in range(len(path)-1):
            distance += graph[path[i]][path[i+1]]

        return distance



    def FindPath(self, start, dest, graph, heuristic):
        need_visit = [(0, start)]
        visited = set()
        path_costs = {start: 0}
        parents = {start: None}

        while need_visit:
            f_score, current = heapq.heappop(need_visit)
            visited.add(current)

            if current == dest:
                path = []

                while current:
                    path.append(current)
                    current = parents[current]

                return path[::-1]

            for neighbor in graph[current]:
                if neighbor in visited:
                    continue
                calculated_path_cost = path_costs[current] + graph[current][neighbor]

                if neighbor not in [n[1] for n in need_visit]:
                    heapq.heappush(need_visit, (calculated_path_cost + heuristic[neighbor], neighbor))

                elif calculated_path_cost < path_costs[neighbor]:
                    index = [n[1] for n in need_visit].index(neighbor)
                    need_visit[index] = (calculated_path_cost + heuristic[neighbor], neighbor)

                parents[neighbor] = current
                path_costs[neighbor] = calculated_path_cost

        return None



if __name__ == "__main__":

    start = input("Start node: ")
    dest = input("Destination: ")

    AStar('./input.txt', start, dest).run()






