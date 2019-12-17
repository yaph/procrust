#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from procrust import __description__


def main():
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('action', choices=['start', 'stop', 'edit'], metavar='ACTION',
                        help='Either "start" or "stop" procrastinating or "edit" the list of blocked sites.')
    args = parser.parse_args()


if __name__ == '__main__':
    main()