#POTD 14112023, Spiral table rotation
def create_spiral(rows, cols):
    matrix = [[""] * cols for _ in range(rows)] #2D empty matrix ([""] * cols) is our first row

    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    """
    in graph terms as follows:
     x = [left, 1, 2, 3, ..., cols - 1],
                             y = [top,
                                    1,
                                    2,
                                    3,
                                    ...,
                                    rows - 1]
     """
    direction = 0
    num = 1

    largest_number = float('-inf') #lowest number ever, will be updated by loop later
    largest_number_position = None #null, will later be replaced if largest_number is found with direction

    while top <= bottom and left <= right: #for clockwise logic
        if direction == 0: #top row moving to the right.
            for i in range(left, right + 1):
                matrix[top][i] = (num, ">") # 2D, top is our y and i is our x.
                if num > largest_number:
                    largest_number = num
                    largest_number_position = (top, i)
                num += 1
            top += 1

        elif direction == 1: #right column moving down.
            for i in range(top, bottom + 1):
                matrix[i][right] = (num, "v") #same here
                if num > largest_number:
                    largest_number = num
                    largest_number_position = (i, right)
                num += 1
            right -= 1

        elif direction == 2:#bottom row moving to the left.
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = (num, "<") #same here
                if num > largest_number:
                    largest_number = num
                    largest_number_position = (bottom, i)
                num += 1
            bottom -= 1

        elif direction == 3:#left column moving up.
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = (num, "^") #same here
                if num > largest_number:
                    largest_number = num
                    largest_number_position = (i, left)
                num += 1
            left += 1

        direction = (direction + 1) % 4
        """ will keep the index within 0,1,2,3. it starts from zero(right) 
         because it initialized first and it returns to zero when direction is 4 """

    return matrix, largest_number_position
def print_matrix(matrix):
    for row in matrix: #filling rows
        row_str = []
        for cell in row: # filling first row
            num, direction = cell
            row_str.append(f"{num} ({direction})") #append for each cell
        print(" ".join(row_str)) #spacing
def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    spiral_matrix, largest_number_position = create_spiral(rows, cols) #spiral_matrix is our returned "matrix"
    print("\nCreated Spiral Matrix:")
    print_matrix(spiral_matrix)
    if largest_number_position is not None:
        largest_number, direction = spiral_matrix[largest_number_position[0]][largest_number_position[1]]
        print(f"\n\nlargest Number in the matrix: {largest_number} ({direction})")
    else:
        print("\n\n matrix is empty.")
#run
main()

