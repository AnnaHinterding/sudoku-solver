## Sudoku Class

This package implements the solving algorithm by Peter Norvig by wrapping a general Sudoku class for a more convient 
object-oriented usage.

The actual solving algorithm can be found here: https://norvig.com/sudoku.html

You can create a Sudoku class either by directly providing the already given numbers by using SudokuMatrix(data=) or you
 can manually enter the data in the input screen via SudokuMatrix.from_input() where all values would also get validated if they are actually valid 
 in the sense of Sudoku rules.