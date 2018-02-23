#!/usr/bin/env python
import unicornhat


def set_all(color=(255,255,255)):
    """
    Set all LCDs to green.
    :param color: tuple representing color as (R,G,B)
    """
    unicornhat.set_all(color)
    unicornhat.show()


if __name__ == '__main__':
    set_all((0,255,0)) # Initialize to green