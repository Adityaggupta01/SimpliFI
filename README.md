Assigment 1
# Logo Design
![image](https://github.com/user-attachments/assets/e3d917a2-3d27-4641-a8f3-a5adf074d79e)

## Overview

This project includes a simple HTML and CSS setup to create a visually appealing logo design. The design features a diamond shape with four differently colored sides and centered text. This layout demonstrates the use of CSS positioning, transformations, and styling to create a modern logo appearance.

## Project Structure

- `index.html` - The HTML file containing the structure of the logo and text.
- `styles.css` - The CSS file providing styling for the diamond shape and text.

## Features

- **Centered Diamond Shape**: A diamond shape created by rotating a square using CSS transforms.
- **Colorful Sides**: Four sides of the diamond with different colors to enhance visual appeal.
- **Centered Text**: The logo text is centrally positioned within the diamond shape.
- **Responsive Layout**: The design is centered within the viewport, ensuring it is well-positioned on various screen sizes.

## Files

### `index.html`

Contains the basic HTML structure of the logo and text:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logo Design</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="logo-container">
        <div class="diamond">
            <div class="side top-left"></div>
            <div class="side top-right"></div>
            <div class="side bottom-left"></div>
            <div class="side bottom-right"></div>
        </div>
        <div class="logo-text">
            <h1>HTML<span class="ampersand">&</span>CSS</h1>
            <p>design and build websites</p>
        </div>
    </div>
</body>
</html>


Assignment 2
![image](https://github.com/user-attachments/assets/e8141b6f-04f6-4154-bb32-7110ab1c6155)
# Ticket Route Finder

This project implements a simple route finder that uses depth-first search (DFS) to determine a valid travel route based on a set of tickets. Below is a detailed explanation of the code.

## Code Breakdown

### Imports

```python
from collections import defaultdict
add_edge(graph, src, dest): Adds an edge between two cities in the graph, making the graph bidirectional.

def add_edge(graph, src, dest):
    graph[src].append(dest)
    graph[dest].append(src)  # Because tickets are bidirectional


def find_route(graph, start_city, cities_to_visit):
find_route(graph, start_city, cities_to_visit): Finds a valid route starting from a specific city and visiting a list of cities.

def dfs(current_city, path):
dfs(current_city, path): A recursive function that explores the graph using depth-first search.

if len(path) == len(cities_to_visit):
            return path if path == cities_to_visit else None
Checks if the current path has visited all desired cities and returns it if valid.


for neighbor in graph[current_city]:
            if neighbor not in path:
                result = dfs(neighbor, path + [neighbor])
                if result:
                    return result
Iterates through neighboring cities, avoiding cycles, and recursively searches for a valid route.

def main():
Defines the main function where execution begins.

graph = defaultdict(list)
    for src, dest in tickets:
        add_edge(graph, src, dest)
Initializes an empty graph and builds it from the ticket list.

start_city = "Kiev"
    route = find_route(graph, start_city, cities_to_visit)
Sets the starting city and searches for a valid route.


if route:
        print("Route:", " -> ".join(route))
    else:
        print("No valid route found")
Prints the found route or a message indicating no valid route exists.
