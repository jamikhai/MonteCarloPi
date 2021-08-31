import math
import random
import matplotlib.pyplot as plt

def compute_pi():
    num_iterations = int(input("How many iterations? "))
    circle_points = 0
    square_points = 0
    iteration = 0
    point_list = []
    while iteration < num_iterations:
        x = random.random()
        y = random.random()
        point_list.append((x, y))
        d = x*x + y*y
        if d <= 1:
            circle_points += 1
        square_points += 1
        iteration += 1
    pi_estimate = 4.0 * circle_points / square_points
    print(f"Estimate: {pi_estimate}")
    return pi_estimate, point_list, num_iterations


def draw_plot(estimate, points, iterations):
    circle1 = plt.Circle((0.5,0.5), 0.5, fill=False)
    fig, ax = plt.subplots()
    ax.add_patch(circle1)
    ax.set_aspect('equal', adjustable='box')
    x, y = zip(*points)
    plt.scatter(x, y, s=1)
    plt.title(f"Estimate for pi: {estimate} from {iterations} iterations")
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    plt.show()
    return


if __name__ == "__main__":
    estimation, point_list, iterations = compute_pi()
    draw_plot(estimation, point_list, iterations)