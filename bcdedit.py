#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 Loic Jaquemet loic.jaquemet+python@gmail.com
#

__author__ = "Loic Jaquemet loic.jaquemet+python@gmail.com"

import argparse
import ctypes
import logging
import sys

def show(opts):
  f = opts.bcdfile
  print "%s: %d bytes"%(f.name, 1)
  print f.__dict__
  
def edit(opts):
  f = opts.bcdfile

def argparser():
  rootparser = argparse.ArgumentParser(prog='bcdedit', 
    description='Edit Windows BCD - Boot Configuration Data file.')

  rootparser.add_argument('--debug', action='store_true', help='Debug mode on.')
  rootparser.add_argument('bcdfile', type=argparse.FileType('rb'), action='store', help='BCD file.')

  subparsers = rootparser.add_subparsers(help='sub-command help')

  showp = subparsers.add_parser('show', help='show things.')
  showp.set_defaults(func=show)  

  editp = subparsers.add_parser('edit', help='edit things.')
  editp.set_defaults(func=edit)  

  showp.add_argument('item', type=str, choices=['all','device'], action='store', default=None, 
        help='What to show.')
  
  return rootparser

def main(argv):

  parser = argparser()
  opts = parser.parse_args(argv)

  level=logging.INFO
  if opts.debug :
    level=logging.DEBUG
  else:
    pass

  opts.func(opts)
  
  


if __name__ == "__main__":
  main(sys.argv[1:])

