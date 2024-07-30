#         *
#        * *
#       *   *
#      *     *
#     *       *
#    *         *
#   *           *
#  ***************

row = 8

for i in range(row):
    for j in range(row - i):
        # prints left space in the same row
        print(' ', end='')

    for j in range(2 * i + 1):

        # printing the left boundary of triangle
        if j == 0 or j == 2 * i or i == row - 1:
            print('*', end='')

        # printing spaces in the middle of the triangle
        else:
            print(' ', end='')

    print()  # printing new line