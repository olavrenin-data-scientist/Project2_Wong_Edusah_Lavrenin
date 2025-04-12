import nbformat

# Load both notebooks
nb1 = nbformat.read("Oleksii.ipynb", as_version=4)
nb2 = nbformat.read("Jimmy.ipynb", as_version=4)

# Combine
nb1.cells.extend(nb2.cells)

# Save result
with open("project2.ipynb", "w") as f:
    nbformat.write(nb1, f)
