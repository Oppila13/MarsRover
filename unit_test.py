import unittest
from lambda_function import MarsRover, simulate_rover

class TestMarsRover(unittest.TestCase):
    def test_turn_left(self):
        rover = MarsRover(0, 0, 'N', 5, 5)
        rover.turn_left()
        self.assertEqual(rover.direction, 'W')

    def test_turn_right(self):
        rover = MarsRover(0, 0, 'N', 5, 5)
        rover.turn_right()
        self.assertEqual(rover.direction, 'E')

    def test_move_forward(self):
        rover = MarsRover(1, 2, 'N', 5, 5)
        rover.move_forward()
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 3)

    def test_simulation(self):
        upper_right = '5 5'
        rover_data = ['1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM', '3 3 E', 'MMRMMRMRRMMMMMMMMMMMMMMMMM']
        rovers = simulate_rover(upper_right, rover_data)

        self.assertEqual(rovers[0].x, 1)
        self.assertEqual(rovers[0].y, 3)
        self.assertEqual(rovers[0].direction, 'N')

        self.assertEqual(rovers[1].x, 5)
        self.assertEqual(rovers[1].y, 1)
        self.assertEqual(rovers[1].direction, 'E')
        
        self.assertEqual(rovers[1].x, 5)
        self.assertEqual(rovers[1].y, 1)
        self.assertEqual(rovers[1].direction, 'E')

if __name__ == "__main__":
    unittest.main()
