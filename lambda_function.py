import json

class MarsRover:
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def turn_left(self):
        current_idx = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_idx + 3) % 4]

    def turn_right(self):
        current_idx = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_idx + 1) % 4]

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1


def simulate_rover(upperRight_values, rover_data):
    plateau_x, plateau_y = map(int, upperRight_values.split())
    rovers = []

    for i in range(0, len(rover_data), 2):
        x, y, direction = rover_data[i].split()
        instructions = rover_data[i + 1]

        rover = MarsRover(int(x), int(y), direction)
        for instruction in instructions:
            if instruction == 'L':
                rover.turn_left()
            elif instruction == 'R':
                rover.turn_right()
            elif instruction == 'M':
                rover.move_forward()

        rovers.append(rover)

    return rovers


def lambda_handler(event, context):
    try:
        upperRight_values = event['upperRight']
        rover_data = event['roverData']

        rovers = simulate_rover(upperRight_values, rover_data)

        response = {
            "statusCode": 200,
            "body": json.dumps([{"x": rover.x, "y": rover.y, "direction": rover.direction} for rover in rovers])
        }
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
    
    return response
