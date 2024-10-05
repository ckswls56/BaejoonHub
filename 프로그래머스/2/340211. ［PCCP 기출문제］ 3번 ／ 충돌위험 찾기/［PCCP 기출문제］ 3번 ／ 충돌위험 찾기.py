def solution(points, routes):
    total_collisions = 0
    point_map = {}
    robot_routes = []

    # Create a dictionary mapping point numbers to their coordinates
    for index in range(len(points)):
        point_map[index + 1] = points[index]

    # Generate robot movement paths
    for route in routes:
        robot_path = []
        current_position = point_map[route[0]].copy()  # Copy the starting point
        for j in range(1, len(route)):
            destination = point_map[route[j]].copy()  # Get the destination point
            # Move along the x-axis
            while current_position[0] != destination[0]:
                temp_position = current_position.copy()  # Copy current position
                robot_path.append(temp_position)
                if destination[0] > current_position[0]:
                    current_position[0] += 1
                else:
                    current_position[0] -= 1
            # Move along the y-axis
            while current_position[1] != destination[1]:
                temp_position = current_position.copy()
                robot_path.append(temp_position)
                if destination[1] > current_position[1]:
                    current_position[1] += 1
                else:
                    current_position[1] -= 1

        robot_path.append(current_position)
        robot_routes.append(robot_path)  # Store the robot's route

    empty_routes = 0  # Check if all routes are empty
    while empty_routes != len(routes):  # Terminate if all robot routes are empty
        current_positions = []  # Store robot positions at the same time
        collision_points = []  # Store collision coordinates
        empty_routes = 0
        for path in robot_routes:
            if len(path) == 0:  # If the route is empty
                empty_routes += 1
                continue
            position = path.pop(0)
            # Check for collisions
            if position in current_positions and position not in collision_points:  # New collision
                collision_points.append(position)
                total_collisions += 1
            else:
                current_positions.append(position)

    return total_collisions
