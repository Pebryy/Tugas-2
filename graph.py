# Graph sederhana

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

print("Tetangga node A:", graph["A"])