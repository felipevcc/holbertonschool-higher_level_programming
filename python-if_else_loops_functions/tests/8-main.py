#!/usr/bin/env python3
from sys import path

path.append('../')
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")
