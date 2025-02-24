def generate_pascal_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def main():
    num_rows = 5 
    triangle = generate_pascal_triangle(num_rows)
    print("Pascal's Triangle:")
    for row in triangle:
        print(row)

if __name__ == "__main__":
    main()