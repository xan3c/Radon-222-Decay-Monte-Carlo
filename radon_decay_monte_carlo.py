#!/usr/bin/env python3

# Title: Monte Carlo Simulation of Radon-222 Decay
# Author: Kenny Moc
# Date created: 11/08/2023
# Python Version: 3.10

# Usage example:
# Simulating 1000 Ra-222 atoms with a time step of 1 second for 100 time steps
# ./radon_decay_monte_carlo.py -c 1000 -dt 1 -l 100

# Begin code

import numpy as np
import random
import argparse

class Radioisotope():
    """Base class for radioisotopes"""
    def __init__(self, half_life) -> None:
        self.half_life = half_life
        return None

    def decay_probability(self, t) -> 'probability':
        """Probability of decay after t seconds"""
        return 1 - (1/2)**(t / self.half_life)

    def decay(self):
        pass

class Ra_222(Radioisotope):
    def __init__(self) -> None:
        super().__init__(330350)

    def decay(self):
        return Po_218()

class Po_218(Radioisotope):
    def __init__(self) -> None:
        super().__init__(186)

    def decay(self):
        if random.uniform(0, 1) > 0.9998:
            return At_218()
        else:
            return Pb_214()

class Pb_214(Radioisotope):
    def __init__(self) -> None:
        super().__init__(1610)

    def decay(self):
        return Bi_214()

class At_218(Radioisotope):
    def __init__(self) -> None:
        super().__init__(1.5)

    def decay(self):
        if random.uniform(0, 1) > 0.999:
            return Rn_218()
        else:
            return Bi_214()

class Rn_218(Radioisotope):
    def __init__(self) -> None:
        super().__init__(0.035)

    def decay(self):
        return Po_214()

class Bi_214(Radioisotope):
    def __init__(self) -> None:
        super().__init__(1194)

    def decay(self):
        rand_num = random.uniform(0, 1)
        if rand_num < 0.003:
            return Pb_210()
        elif rand_num < 0.003 + 0.021:
            return Ti_210()
        else:
            return Po_214()

class Po_214(Radioisotope):
    def __init__(self) -> None:
        super().__init__(1.643e-4)

    def decay(self):
        return Pb_210()

class Ti_210(Radioisotope):
    def __init__(self) -> None:
        super().__init__(78)

    def decay(self):
        if random.uniform(0, 1) < 0.009:
            return Pb_209()
        else:
            return Pb_210()

class Pb_209(Radioisotope):
    def __init__(self) -> None:
        super().__init__(11710)

    def decay(self):
        return Bi_209()

class Bi_209(Radioisotope):
    def __init__(self) -> None:
        super().__init__(5.99e26)

    def decay(self):
        return Ti_205()

class Ti_205(Radioisotope):
    def __init__(self) -> None:
        super().__init__(0)

    def decay_probability(self, t) -> 'probability':
        return 0

    def decay(self):
        pass

class Pb_210(Radioisotope):
    def __init__(self) -> None:
        super().__init__(7.01e8)

    def decay(self):
        if random.uniform(0, 1) < 1.9e-6:
            return Hg_206()
        else:
            return Bi_210()

class Hg_206(Radioisotope):
    def __init__(self) -> None:
        super().__init__(499.2)

    def decay(self):
        return Ti_206()

class Ti_206(Radioisotope):
    def __init__(self) -> None:
        super().__init__(252.12)

    def decay(self):
        return Pb_206()

class Bi_210(Radioisotope):
    def __init__(self) -> None:
        super().__init__(433000)

    def decay(self):
        if random.uniform(0, 1) < 0.000132:
            return Ti_206()
        else:
            return Po_210()

class Po_210(Radioisotope):
    def __init__(self) -> None:
        super().__init__(1.19557e7)

    def decay(self):
        return Pb_206()

class Pb_206(Radioisotope):
    def __init__(self) -> None:
        super().__init__(0)

    def decay_probability(self, t) -> 'probability':
        return 0

    def decay(self):
        pass

def main():
    parser = argparse.ArgumentParser(description="A script to simulate the decay of Ra-222")
    parser.add_argument("-c", "--count", type=int, help="Number of radon atoms", required=True)
    parser.add_argument('-dt', '--time_step', type=float, help='Time step of simulation in seconds', required=True)
    parser.add_argument('-l', '--loops', type=int, help='Number of time steps to perform', required=True)

    args = parser.parse_args()

    if args.loops < 0 or args.time_step < 0 or args.count < 0:
        print('Parameters must be positive')
        return

    
    source = [Ra_222() for _ in range(args.count + 1)]
    time_stamps = {}

    # Simulation

    for x in range(args.loops):
        time_stamps[x] = {}

        for index, element in enumerate(source):
            n = random.uniform(0, 1)
            if n < element.decay_probability(args.time_step): 
                source[index] = element.decay()

        for atom in source:
            class_name = atom.__class__.__name__
            if class_name in time_stamps[x]:
                time_stamps[x][class_name] += 1
            else:
                time_stamps[x][class_name] = 0

    # Print the results

    for step, counts in time_stamps.items():
        print(f"Step {step}:")
        for class_name, count in counts.items():
            print(f"  {class_name}: {count} atoms")

if __name__ == '__main__':
    main()