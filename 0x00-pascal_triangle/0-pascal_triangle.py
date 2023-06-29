#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n)
    """
    triangle = []
    
    if n > 0:
        for i in range(1, n + 1):
            row = []
            coeff = 1
            
            for j in range(1, i + 1):
                row.append(coeff)
                coeff = coeff * (i - j) // j
            
            triangle.append(row)
    
    return triangle
