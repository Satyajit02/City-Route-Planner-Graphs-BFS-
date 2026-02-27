from collections import deque

class CityRoutePlanner:
    def __init__(self):
        # Dictionary to store the graph (Adjacency List)
        self.adj_list = {}

    def add_road(self, u, v):
        # Dono cities ko ek doosre se connect kar rahe hain (Undirected)
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []
        
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def find_shortest_route(self, start, destination):
        # Agar city list mein nahi hai to error handle karo
        if start not in self.adj_list or destination not in self.adj_list:
            return "City map mein nahi hai!"

        # BFS ke liye Queue
        queue = deque([start])
        # Visited cities track karne ke liye
        visited = {start}
        # Rasta (Path) yaad rakhne ke liye
        parent = {start: None}

        while queue:
            current_city = queue.popleft()

            # Agar destination mil gaya
            if current_city == destination:
                return self.reconstruct_path(parent, destination)

            # Neighbors check karo
            for neighbor in self.adj_list[current_city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current_city
                    queue.append(neighbor)

        return "Koi rasta nahi mila."

    def reconstruct_path(self, parent, destination):
        path = []
        current = destination
        while current is not None:
            path.append(current)
            current = parent[current]
        
        # Path ulta hota hai isliye reverse kar rahe hain
        return " -> ".join(path[::-1])

# --- Project Testing ---
planner = CityRoutePlanner()

# Road Network (Example Data)
planner.add_road("Delhi", "Mumbai")
planner.add_road("Delhi", "Lucknow")
planner.add_road("Mumbai", "Bangalore")
planner.add_road("Lucknow", "Kolkata")
planner.add_road("Bangalore", "Chennai")
planner.add_road("Kolkata", "Chennai")

print("--- City Route Planner ---")
start_node = "Delhi"
end_node = "Chennai"

result = planner.find_shortest_route(start_node, end_node)
print(f"Shortest Route from {start_node} to {end_node}:")
print(result)