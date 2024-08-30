from collections import defaultdict

def add_edge(graph, src, dest):
    graph[src].append(dest)
    graph[dest].append(src)  # Because tickets are bidirectional

def find_route(graph, start_city, cities_to_visit):
    def dfs(current_city, path):
        if len(path) == len(cities_to_visit):
            return path if path == cities_to_visit else None
        
        for neighbor in graph[current_city]:
            if neighbor not in path:
                result = dfs(neighbor, path + [neighbor])
                if result:
                    return result
        return None
    
    return dfs(start_city, [start_city])

def main():
    tickets = [
        ("Paris", "Skopje"),
        ("Zurich", "Amsterdam"),
        ("Prague", "Zurich"),
        ("Barcelona", "Berlin"),
        ("Kiev", "Prague"),
        ("Skopje", "Paris"),
        ("Amsterdam", "Barcelona"),
        ("Berlin", "Kiev"),
        ("Berlin", "Amsterdam")
    ]
    
    cities_to_visit = ["Kiev", "Prague", "Zurich", "Amsterdam", "Barcelona", "Berlin"]

    graph = defaultdict(list)
    for src, dest in tickets:
        add_edge(graph, src, dest)

    start_city = "Kiev"
    route = find_route(graph, start_city, cities_to_visit)
    
    if route:
        print("Route:", " -> ".join(route))
    else:
        print("No valid route found")

if __name__ == "__main__":
    main()
