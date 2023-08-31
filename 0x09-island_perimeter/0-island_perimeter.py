#!/usr/bin/python3
"""Island perimeter.
"""
def island_perimeter(grid):
"""the perimeter of an island described in grid
"""
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    perimeter = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4  # Every land cell contributes 4 to the perimeter
                
                # Check left neighbor
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2  # Subtract 2 due to shared edge
                
                # Check top neighbor
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2  # Subtract 2 due to shared edge
