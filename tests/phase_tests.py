# -*- coding: utf-8 -*-

import os
from os import path
from unittest.case import TestCase
import math
import sys

project_dir = path.dirname(__file__)
project_dir = path.join('..')
sys.path.append(project_dir)
from graphics_tk import run_phase

project_dir = os.path.join(os.path.dirname(__file__), '..')
project_dir = os.path.normpath(project_dir)
sys.path.append(project_dir)

from actors import Obstacle, Pig, RedBird, YellowBird, DESTROYED
from phase import Phase, Point, ON_GOING, VICTORY, DEFEAT


class PhaseTestes(TestCase):
    def test_add_obstacles(self):
        phase = Phase()
        self.assertListEqual([], phase._obstacles)
        obstacle = Obstacle()
        phase.add_obstacles(obstacle)
        self.assertListEqual([obstacle], phase._obstacles)

        obstacle1, obstacle2 = Obstacle(), Obstacle()
        phase.add_obstacles(obstacle1, obstacle2)
        self.assertListEqual([obstacle, obstacle1, obstacle2], phase._obstacles)

    def test_add_pig(self):
        phase = Phase()
        self.assertListEqual([], phase._pigs)
        pig = Pig()
        phase.add_pigs(pig)
        self.assertListEqual([pig], phase._pigs)

        pig1, pig2 = Pig(), Pig()
        phase.add_pigs(pig1, pig2)
        self.assertListEqual([pig, pig1, pig2], phase._pigs)

    def test_add_bird(self):
        phase = Phase()
        self.assertListEqual([], phase._birds)
        bird = RedBird()
        phase.add_birds(bird)
        self.assertListEqual([bird], phase._birds)

        bird1, bird2 = RedBird(), YellowBird()
        phase.add_birds(bird1, bird2)
        self.assertListEqual([bird, bird1, bird2], phase._birds)


    def test_game_over_without_pigs(self):
        phase = Phase()
        self.assertEqual(VICTORY, phase.status())

    def test_game_over_with_pigs_and_birds(self):
        phase = Phase()
        pigs = [Pig(1, 1) for i in range(2)]  # creating 2 pigs
        birds = [YellowBird(1, 1) for i in range(2)]  # criating 2 birds
        phase.add_pigs(*pigs)
        phase.add_birds(*birds)

        self.assertEqual(ON_GOING, phase.status())

        # clashing bird against pig on time 3
        for bird, pig in zip(birds, pigs):
            bird.clash(pig, 3)

        self.assertEqual(VICTORY, phase.status())

        phase.add_obstacles(Obstacle())
        self.assertEqual(VICTORY, phase.status(), 'Obstacle must not interfere on game result')

        phase.add_pigs(Pig())
        self.assertEqual(DEFEAT, phase.status(), 'With no active birds and one Pig active, player should lose')

        phase.add_birds(YellowBird())
        self.assertEqual(ON_GOING, phase.status(),
                         'With one pig and bird both active, game should still going on')

    def test_status(self):
        phase = Phase()
        pigs = [Pig(1, 1) for i in range(2)]
        birds = [YellowBird(1, 1) for i in range(2)]
        phase.add_pigs(*pigs)
        phase.add_birds(*birds)
        self.assertEqual(ON_GOING, phase.status())

        for bird, pig in zip(birds, pigs):
            bird.clash(pig, 3)

        self.assertEqual(VICTORY, phase.status(),
                         'Without active pigs game should end with victory')

        phase.add_obstacles(Obstacle())
        self.assertEqual(VICTORY, phase.status(),
                          'Obstacle must not interfere on game result')

        pig = Pig()
        phase.add_pigs(pig)
        self.assertEqual(DEFEAT, phase.status(),
                         'With Active Pig and with no Active bird, game should end with defeat')

        phase.add_birds(YellowBird())
        self.assertEqual(ON_GOING, phase.status(),
                         'With active pig and birds, game should not end')

        pig.clash(pig, 3)
        self.assertEqual(VICTORY, phase.status(),
                         'Without active pigs game should end with victory')

    def test_launch_without_error_when_there_is_no_bird_to_be_launch(self):
        red_bird, yellow_bird = RedBird(1, 1), YellowBird(1, 1)
        phase = Phase()
        phase.add_birds(red_bird, yellow_bird)
        self.assertFalse(red_bird.launched())
        self.assertFalse(yellow_bird.launched())
        phase.launch(90, 1)
        phase.launch(45, 3)
        phase.launch(31, 5)  # There is no bird to launch here

        self.assertTrue(red_bird.launched())
        self.assertEqual(math.radians(90), red_bird._launch_angle)
        self.assertEqual(1, red_bird._launch_time)

        self.assertTrue(yellow_bird.launched())
        self.assertEqual(math.radians(45), yellow_bird._launch_angle)
        self.assertEqual(3, yellow_bird._launch_time)

    def test_default_clash_interval(self):

        phase = Phase()
        bird = YellowBird(1, 1)
        phase.add_birds(bird)
        porco = Pig(2, 2)
        phase.add_pigs(porco)
        phase.calculate_points(0)
        self.assertEqual(DESTROYED, bird.status)
        self.assertEqual(DESTROYED, porco.status)

    def test_non_default_clash_interval(self):
        phase = Phase(30)
        bird = YellowBird(1, 1)
        phase.add_birds(bird)
        pig = Pig(31, 31)
        phase.add_pigs(pig)
        phase.calculate_points(0)
        self.assertEqual(DESTROYED, bird.status)
        self.assertEqual(DESTROYED, pig.status)

    def test_calculate_points(self):
        phase = create_phase()
        expected = set([Point(3, 3, 'Y'), Point(3, 3, 'Y'), Point(31, 10, 'O'), Point(78, 1, '@'),
                        Point(70, 1, '@'), Point(3, 3, 'R')])
        self.assertSetEqual(expected, set(phase.calculate_points(0)))

        phase.launch(45, 1)

        # i going from 1 to 2.9
        for i in range(100, 300, 1):
            phase.calculate_points(i / 100)

        phase.launch(63, 3)

        # i going from 3 to 3.9
        for i in range(300, 400, 1):
            phase.calculate_points(i / 100)

        phase.launch(23, 4)

        expected = set([Point(32, 11, 'r'), Point(17, 25, 'Y'), Point(3, 3, 'Y'), Point(31, 10, ' '), Point(78, 1, '@'),
                        Point(70, 1, '@')])

        self.assertSetEqual(expected, set(phase.calculate_points(4)))

        # i going from 4 to 6.9
        for i in range(400, 700, 1):
            phase.calculate_points(i / 100)

        expected = set(
            [Point(32, 11, 'r'), Point(57, 30, 'Y'), Point(70, 2, 'y'), Point(31, 10, ' '), Point(78, 1, '@'),
             Point(70, 1, '+')])

        self.assertSetEqual(expected, set(phase.calculate_points(7)))

        # i going from 7 to 8.49
        for i in range(700, 849, 1):
            phase.calculate_points(i / 100)
        print(phase.calculate_points(8.5))

        expected = set([Point(32, 11, 'r'), Point(77, 0, 'y'), Point(70, 2, 'y'), Point(31, 10, ' '), Point(78, 1, '+'),
                        Point(70, 1, '+')])

        self.assertSetEqual(expected, set(phase.calculate_points(8.5)))

        self.assertEqual(VICTORY, phase.status())


def create_phase(multplier=1):
    example_phase = Phase(1 if multplier == 1 else 32)
    birds = [RedBird(3 * multplier, 3 * multplier),
                YellowBird(3 * multplier, 3 * multplier),
                YellowBird(3 * multplier, 3 * multplier)]
    pigs = [Pig(78 * multplier, multplier), Pig(70 * multplier, multplier)]
    obstacles = [Obstacle(31 * multplier, 10 * multplier)]

    example_phase.add_birds(*birds)
    example_phase.add_pigs(*pigs)
    example_phase.add_obstacles(*obstacles)

    return example_phase


if __name__ == '__main__':
    run_phase(create_phase(10))
