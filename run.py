import argparse

import cv2
from time import time
from image_solver.genetic_algorithm import GeneticAlgorithm

GENERATIONS = 20
POPULATION = 200


def parse_arguments():
    """Parses input arguments required to solve the image"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", type=str, default="out.jpg", help="Input image.", required=True)
    parser.add_argument("-o", "--output", required=True, help="output path of the image")
    parser.add_argument("-s", "--size", type=int, help="Single piece size in pixels.", required=True)
    parser.add_argument("-g", "--generations", type=int, default=GENERATIONS)
    parser.add_argument("-p", "--population", type=int, default=POPULATION)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    image = cv2.imread(args.image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    print(f"\n=== Population:  {args.population}")
    print(f"=== Generations: {args.generations}")
    print(f"=== Piece size:  {args.size} px")

    start = time()
    algorithm = GeneticAlgorithm(image, args.size, args.population, args.generations)
    solution = algorithm.start_evolution()
    end = time()

    print(f"\n=== Done in {end - start} s")

    solution_image = solution.to_image()
    solution_image_name = args.output

    cv2.imwrite(solution_image_name, solution_image)
    print(f"=== Result saved as '{solution_image_name}'")
    print("=== Done!")
