# find the biggest product of n numbers next to each other
# check runs that go left to right and runs that go top to bottom
# for each row, slide a window of size n and multiply those n numbers
# for each column, slide a window of size n and multiply those n numbers
# keep track of the biggest product seen
# return the biggest product

def largest_product(grid, n):
    if not grid or not grid[0]:
        return 0

    row_count = len(grid)
    col_count = len(grid[0])

    max_product = None

    # check left to right
    for row in range(row_count):
        for start_col in range(col_count - n + 1):
            product = 1
            for step in range(n):
                product *= grid[row][start_col + step]

            if max_product is None or product > max_product:
                max_product = product

    # check top to bottom
    for col in range(col_count):
        for start_row in range(row_count - n + 1):
            product = 1
            for step in range(n):
                product *= grid[start_row + step][col]

            if max_product is None or product > max_product:
                max_product = product

    return max_product


grid = [
    [1, 2,  3,  4,  5],
    [6, 7,  8,  9,  8],
    [1, 99, 88, 77, 5],
    [1, 2,  3,  4,  5],
    [1, 6,  7,  8,  9],
]
n = 3
expected = 670824  # 99 * 88 * 77
assert largest_product(grid, n) == expected

grid = [
    [1, 2,  3,  4],
    [5, 6,  7,  8],
    [9, 10, 11, 12]
]
n = 3
expected = 1320  # 10 * 11 * 12
assert largest_product(grid, n) == expected

grid = [
    [13, 0, 9],
    [2,  6, 10],
    [3,  7, 11],
    [4,  8, 12]
]
n = 3
expected = 1320  # 10 * 11 * 12
assert largest_product(grid, n) == expected

grid = [
    [1, 99, 9],
    [2, 77, 10],
    [3, 22, 11],
    [4, 0,  12]
]
n = 2
expected = 7623  # 99 * 77
assert largest_product(grid, n) == expected

grid = [
    [1, 2, 3],
    [4, 5, 6]
]
n = 3
expected = 120  # 4 * 5 * 6
assert largest_product(grid, n) == expected

grid = [
    [-1],
    [2],
    [-3]
]
n = 2
expected = -2  # -1 * 2
assert largest_product(grid, n) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
