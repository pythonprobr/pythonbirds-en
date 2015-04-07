# -*- coding: utf-8 -*-
from itertools import chain

from actors import ACTIVE


# Games's Statuses

VICTORY = 'VICTORY'
DEFEAT = 'DEFEAT'
ON_GOING = 'ON_GOING'


class Point():
    def __init__(self, x, y, character):
        self.character = character
        self.x = round(x)
        self.y = round(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.character == other.character

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __repr__(self, *args, **kwargs):
        return "Point(%s,%s,'%s')" % (self.x, self.y, self.character)


class Phase():
    def __init__(self, clash_interval=1):
        """
        Method that initializes a phase.

        :param clash_interval:
        """
        self.clash_interval = clash_interval
        self._birds = []
        self._pigs = []
        self._obstacles = []


    def add_obstacles(self, *obstacles):
        """
        Add obstacles to a phase

        :param obstacles:
        """
        pass

    def add_pigs(self, *pigs):
        """
        Add pigs to a phase

        :param pigs:
        """
        pass

    def add_birds(self, *birds):
        """
        Add birds to a phase

        :param birds:
        """
        pass


    def status(self):
        """
        Method that indicates the game's status:

        ON_GOING if game is still running (there is one bird active at least).

        DEFEAT if game is over with defeat (there is one pig active at least and no bird active)

        VICTORY if game is over with victory (there is no active pig)

        :return:
        """
        return ON_GOING

    def launch(self, angle, time):
        """
        Method that executes launch logic.

        It must pick the first not launched bird from list

        If there is no bird of this kind, nothing must happen

        :param angle: launch angle
        :param time: launch time
        """
        pass


    def calculate_points(self, time):
        """
        Method that convert Actors to Points.

        :param time: game's time
        :return: Point object
        """
        points = []
        return points

    def _to_point(self, actor):
        return Point(actor.x, actor.y, actor.character())

