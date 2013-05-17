#!/usr/bin/python

"""
BookSearch
Module: timer
Author: Rahul.A.R
"""

import time

class Timer:
  """Time class used to profile different parts of code"""
  def __enter__(self):
    self.start = time.clock()
    return self

  def __exit__(self, *args):
    self.end = time.clock()
    self.interval = self.end - self.start
