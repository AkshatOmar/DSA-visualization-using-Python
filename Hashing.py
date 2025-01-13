import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
4
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize hash table with empty lists
    
    def hash_function(self, key):
        """Simple hash function based on modulus."""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)
        self.table[index].append((key, value))
    
    def display(self):
        """Display the hash table as a dictionary."""
        return {i: self.table[i] for i in range(self.size)}

def visualize_2d(hash_table):
    """Visualize the hash table in 2D."""
    data = hash_table.display()
    
    plt.figure(figsize=(10, 7))
    for i, values in data.items():
        plt.scatter([i] * len(values), range(len(values)), s=300, c='skyblue', label=f"Index {i}" if i == 0 else "")
        for j, (key, value) in enumerate(values):
            plt.text(i, j, f"({key}, {value})", fontsize=10, ha='center')
    
    plt.title("Hash Table Visualization in 2D", fontsize=20)
    plt.xlabel("Hash Index")
    plt.ylabel("Stored Values")
    plt.xticks(range(hash_table.size))
    plt.legend()
    plt.show()

def visualize_3d(hash_table):
    """Visualize the hash table in 3D."""
    data = hash_table.display()
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    for i, values in data.items():
        for j, (key, value) in enumerate(values):
            ax.scatter(i, j, 0, color='skyblue', s=100)
            ax.text(i, j, 0, f"({key}, {value})", fontsize=10)
    
    ax.set_title("Hash Table Visualization in 3D", fontsize=20)
    ax.set_xlabel("Hash Index")
    ax.set_ylabel("Value Position")
    ax.set_zlabel("Depth (always 0)")
    plt.show()

if __name__ == "__main__":
    print("Enter the size of the hash table:")
    size = int(input())
    hash_table = HashTable(size)

    print("Enter key-value pairs (type 'done' to finish):")
    while True:
        user_input = input("Enter key and value separated by a space (e.g., key1 value1): ")
        if user_input.lower() == 'done':
            break
        try:
            key, value = user_input.split()
            hash_table.insert(key, value)
        except ValueError:
            print("Invalid input. Please enter a key and a value separated by a space.")

    print("Hash Table Contents:")
    print(hash_table.display())

    print("\nVisualizing in 2D...")
    visualize_2d(hash_table)

    print("\nVisualizing in 3D...")
    visualize_3d(hash_table)
