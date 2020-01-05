import numpy as np
from imported_solver import solve


class SudokuMatrix(object):
    """
    Class like representation of a classical Sudoku field, given as a 9x9 matrix with numbers ranging from 1 to 9.
    Please note that the actual solving algorithm was developed by Peter Norvig and can be found here:
    https://norvig.com/sudoku.html

    """

    def __init__(self, data: list):
        """
        Standard constructor of the class. It requires the given numbers to be provided. Empty fields are representing
        as zeros.

        Args:
            data(list): A list of lists, containing integers from 0 to 9, with 0 representing an empty field.
        """

        self.inner_matrix = np.array(data)
        self.grid = ''.join([str(i) for j in range(9) for i in data[j]])

    def __repr__(self):
        return str(self)

    def __str__(self):
        height = self.inner_matrix.shape[0]
        width = self.inner_matrix.shape[1]
        row_string = ''
        for i in range(height):
            for j in range(width):
                row_string += str(self.inner_matrix[i, j]).replace('0', '.') + ' '
                if str(j) in '25':
                    row_string += '|'
            row_string += '\n'
            if str(i) in '25':
                row_string += '------+------+------\n'

        return row_string

    @staticmethod
    def is_int_convertible(check_string: str) -> bool:
        """
        Checks if a given string is numerical and can be converted to a string.

        Args:
            check_string: The respective string to check.

        Returns:
            bool: Is True if the input can be converted to an int type, False otherwise.
        """

        try:
            int(check_string)
            return True
        except ValueError:
            return False

    @classmethod
    def validate_row(cls, row_list: list) -> bool:

        """
        Checks if the provided row, given as a string represents a valid Sudoku field row.

        Args:
            row_list(list: The row given as a string

        Returns:
            bool: Returns true if the row is valid, otherwise False

        """

        if not len(row_list) == 9:
            print("Your answer isn't correct. Try again!")
            return False
        else:
            validate_list = [cls.is_int_convertible(i) for i in row_list]
            # validate_list = [is_int_convertible(row_list[i]) for i in range(9)]
            if all(validate_list):
                row_list_int = [int(i) for i in row_list]
                row_list_without_zero = [i for i in row_list_int if i > 0]
                if len(row_list_without_zero) == len(list(set(row_list_without_zero))):
                    return True
                else:
                    print("The row isn't correct. At least one number without zero is multiple present!")
                    return False
            else:
                print("Your answer isn't correct. Try again!")
                print("The machine expects nine numbers from 0 to 9 comma separated. The blank cells are"
                      " represented as a 0:")
                print("For example one row looks like 4,2,0,0,8,0,0,0,0")
                return False

    @classmethod
    def from_input(cls):
        """
        Alternative class constructor, allowing to create a SudokuMatrix by entering the matrix rows in the interface.

        Returns:
            SudokuMatrix: The matrix built by the entered rows.

        """

        print("This is a Sudoku solver.")
        print("Please enter your Sudoku line by line. The machine expects a 9x9 board.")
        # Todo, also explain how a sudoku works?
        print("The machine expects nine numbers from 0 to 9 comma separated. The blank cells will represented as a 0:")
        print("For example one row looks like: 4,2,0,0,8,0,0,0,0")
        sudoku_list = []
        for looping_var in range(1, 10):
            print(f"Please enter row number {looping_var}: ")
            row_string = input()
            row_list = row_string.replace(' ', '').split(',')
            while not cls.validate_row(row_list):
                print(f"Please enter row number {looping_var}: ")
                row_string = input()
                row_list = row_string.replace(' ', '').split(',')

            row_list_int = [int(i) for i in row_list]
            sudoku_list.append(row_list_int)
            print(row_list_int)

        sudoku_matrix = cls(data=sudoku_list)
        return sudoku_matrix

    def solve(self) -> None:
        """
        Solves the current Sudoku matrix by using Peter Norvig's algorithm.

        """

        solved_sudoku = solve(self.grid)
        rows = 'ABCDEFGHI'
        cols = '123456789'
        for square, value in solved_sudoku.items():
            row = rows.find(square[0])
            col = cols.find(square[1])
            self.inner_matrix[row, col] = int(value)


if __name__ == '__main__':
    # Activate the below commented code to run a sample Sudoku matrix: #
    sample_matrix = SudokuMatrix(data=[['0', '0', '3', '0', '2', '0', '6', '0', '0'],
                                       ['9', '0', '0', '3', '0', '5', '0', '0', '1'],
                                       ['0', '0', '1', '8', '0', '6', '4', '0', '0'],
                                       ['0', '0', '8', '1', '0', '2', '9', '0', '0'],
                                       ['7', '0', '0', '0', '0', '0', '0', '0', '8'],
                                       ['0', '0', '6', '7', '0', '8', '2', '0', '0'],
                                       ['0', '0', '2', '6', '0', '9', '5', '0', '0'],
                                       ['8', '0', '0', '2', '0', '3', '0', '0', '9'],
                                       ['0', '0', '5', '0', '1', '0', '3', '0', '0']])
    sample_matrix.solve()
    print(sample_matrix)

    # Activate the below commented code to manually enter a Sudoku matrix: #
    # input_matrix = SudokuMatrix.from_input()
    # input_matrix.solve()
    # print(input_matrix)
