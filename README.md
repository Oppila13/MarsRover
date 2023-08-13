# MarsRover
Implementing a solution for Mars Rover problem in python

## Code Testing
The code is deployed in AWS APIGateway publicly. Use the endpoint and input details to test the code.
   * API Endpoint: https://22fmtho4zg.execute-api.ap-southeast-2.amazonaws.com/dev/input
   * Method: POST
   * Add the following in header
```sh
Content-Type:application/json
```

   * Sample Input to add in body:
```sh
{
  "upperRight": "5 5",
  "roverData": [
    "1 2 N",
    "LMLMLMLMM",
    "3 3 E",
    "MMRMMRMRRM"
  ]
}
```

   * Input parameters consists of upperRight dimension value. The lower right dimensions are by default consisdered to be (0,0). The next value is roverData, which gets the starting point of a rover and the directions for movement. n number of data can be given here.
   * Once all the data are entered in postman or similar application, click send.
   * Output returns 200 for success, x and y position of the rover and the rover's direction it is currently in.
   * Output returns 500 for error.
   * Sample Output:
```sh
{
    "statusCode": 200,
    "body": "[{\"x\": 1, \"y\": 3, \"direction\": \"N\"}, {\"x\": 5, \"y\": 1, \"direction\": \"E\"}]"
}
```

## Unit test 

  * Under unit_test.py file sample test cases are given as unit tests.
  * Clone the repo in local machine and run ```py unit_test.py``` in the folder.
    
## Deployment Proposal

  * For code deployment use terraform or other TF alternatives such as Plumi/AWS Cloud Formation/etc., to implement Infrastructure as Code (IAC).
  * Deploy the code to AWS via Jenkins or similar platforms for managing the releases and deployments.
  * Ensure zero downtime using Blue/Green deployment approach. 
  * Use Microservies such as Lambda, ECS, etc to run the code. Here the code is written for lamda.
  * AWS APIGateway is used to create and deploy APIs publicly under different stages.
  * For naming conversion, follow {stage}-{Blue/Green Stack}-{Application Name}

## Development techniques

  * The code consists of four parts.
      * Lambda_handler function which reads the input and returns the output
      * Simulate_rover function which calls the required function to move one rover after another based on the directions given.
      * MarsRover class in which the core logic (turn_left, turn_right and move_forward) lies.
      * Unit_test file where sample test cases for above functions are simulated before deployment.
  * MarsRover Class
      * turn_left function: In this method 90 degree turn will result in the following changes, N->W, W->S, S->E, E->N. These rotations forms a circle in the array ['N','E','S','W']. The resulting direction array index can be calculated as (current_idx + 3) % 4 
      * turn_right function: In this method, N->E, E->S, S->W, W->N. These rotations also forms a circle in the array ['N','E','S','W']. The resulting direction array index can be calculated as (current_idx + 1) % 4
      * move_forward function: This method alters the position based on the direction. N->(x,y+1); E->(x+1,y); S->(x,y-1); W->(x-1,y). This function ensures the value does not exceed outside the plateau, if it exceeds the value won't change. 
  * Simulate_rover
      * This function updates the upper right dimensional value.
      * Splits the rover position and directional instructions.
      * Calls the methods from MarsRover class based on the instruction present.
      * Second rover will start move after the first rover movement completes.
  * Unit test file
      * This files contains unit test for four different methods. Run the file during CI/CD pipeline to ensure the code working condition before deployment. Test cases can also be created in Postman and used to test the code before deployment. A link between postman and jenkins can be estalblished.
  * requirement.txt and setup.py are not added in this code because they are not needed for this lambda. It only imports json package.
