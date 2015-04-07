# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import math

DESTROYED = 'Destroyed'
ACTIVE = 'Active'
GRAVITY = 10  # m/s^2


class Actor():
    """
    Class representing an actor. It represents a point on screen.
    """
    _active_char = 'A'
    _destroyed_char = ' '

    def __init__(self, x=0, y=0):
        """
        Method used to initialize class. It must initialize x, y and status attributes

        :param x: Initial actor's horizontal position
        :param y: Initial actor's vertical position
        """
        self.y = y
        self.x = x
        self.status = ACTIVE

    def character(self):
        return self._active_char

    def calculate_position(self, time):
        """
        Method to calculate position in a given time.
        Time starts in 0 s and advances in 0,01 s

        :param time: game's time
        :return: actor's position x, y
        """
        return 1, 1

    def clash(self, another_actor, interval=1):
        """
        Method tha execute clash logic for two actors.
        Clash must happen only if both actor's status are ACTIVE.
        For clash the actor must be considered as a square surrounding the point with "interval" been its side.
        If squares touch themselves, the clash occur and both actor's statuses must be changed do DESTROYED

        :param another_actor: Actor to be considered on clash
        :param interval: clash interval
        :return:
        """
        pass


class Obstacle(Actor):
    pass


class Pig(Actor):
    pass


class Bird(Actor):
    velocity = 1

    def __init__(self, x=0, y=0):
        """
        Method to initialize bird.

        It must initialize Actor. Besides that, it must store initial bird position (x_initial and y initial)
        launch_time and angle_time

        :param x:
        :param y:
        """
        super().__init__(x, y)
        self._x_initial = x
        self._y_initial = y
        self._launch_time = None
        self._launch_angle = None  # radians

    def launched(self):
        """
        Must return true if bird is already launched and false other else

        :return: boolean
        """
        pass

    def ground_clash(self):
        """
        Execute ground clash logic. Every time y is less or equals than0,
        Bird's status must be changed to destroyed

        """
        pass

    def _calculate_horizontal_position(self, delta_t):
        pass

    def _calculate_vertical_position(self, delta_t):
        pass

    def _calculate_position(self, time):
        pass

    def calculate_position(self, time):
        """
        Method that calculates bird position in a given time.

        Before launch, it must return bird initial position

        After launch it must calculate bird's position according to its initial position, velocity, launch_angle,
        GRAVITY, and time of the game.

        After clash, it must retorn the clash position.

        :param time: game's time
        :return: position (tuple) x, y
        """
        return 1, 1

    def launch(self, angle, launch_time):
        """
        Bird launch logic. Must store angle and launch time for position calculations.
        Angle is given in degree and must be converted to radians.

        :param angle:
        :param launch_time:
        :return:
        """
        pass



class YellowBird(Bird):
    pass


class RedBird(Bird):
    pass