#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from pathlib import Path

from procrust import __description__


def edit():
    print('edit')


def start():
    pass


def stop():
    pass


def main():
    parser = argparse.ArgumentParser(description=__description__)
    subparsers = parser.add_subparsers()
    subparsers.add_parser('edit', description='Edit the list of blocked sites.').set_defaults(func=edit)
    subparsers.add_parser('start', description='Start procrastinating.').set_defaults(func=start)
    subparsers.add_parser('stop', description='Stop procrastinating.').set_defaults(func=stop)
    args = parser.parse_args()
    if getattr(args, 'func', None):
        args.func()


if __name__ == '__main__':
    main()