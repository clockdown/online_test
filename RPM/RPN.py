#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.command()
@click.argument('formula')
def cmd(formula):
    if not formula :
        error(1)
    click.echo(formula)

def error(num):
    print(num)


def main():
	cmd()

if __name__ == '__main__':
    main()