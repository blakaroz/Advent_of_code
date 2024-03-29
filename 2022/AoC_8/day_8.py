with open("input_ex.txt") as file:
    grid = file.read().split("\n")

# print(trees)

grid = [list(map(int,line)) for line in grid]
# print(grid)

# counter = 0
# for row in range(len(grid)):
#     for column in range(len(grid[row])):
#         # print(column)
#         current = grid[row][column]
#         #  if all po lewej czyli from 0 to index of current collor(without it) or all po praeej czyli from current ocllumn +1 to len of current row in grid or up or down
#         if all(grid[row][x] < current for x in range(column)) or all(grid[row][x] < current for x in range(column+1, len(grid[row]))) or all(grid[x][column] < current for x in range (row)) or all(grid[x][column] < current for x in range(row+1, len(grid))):
#             counter +=1
# print(counter)

# # part 2 
tree_max = 0

for row in range(len(grid)):
    for column in range(len(grid[row])):
        current = grid[row][column]
        L = R = U = D = 0
       
        for x in range(column-1, -1, -1):
             L += 1
             if grid[row][x] >= current:
                 break
        for x in range(column+1, len(grid[row])):   
             R += 1
             if grid[row][x] >= current:
                 break  
        for x in range(row-1, -1, -1):
             U += 1
             if grid[x][column] >= current:
                 break
        for x in range(row+1, len(grid)):
             D += 1
             if grid[x][column] >= current:
                 break
        
        tree_result = L * R * U * D

        # if tree_result > max:
        #     max = tree_result
        tree_max = max(tree_max, tree_result)
print(tree_max)