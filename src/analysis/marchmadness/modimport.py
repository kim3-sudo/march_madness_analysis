# -*- coding: utf-8 -*-
"""
March Madness Analysis
Steven Lucas & Sejin Kim
STAT 306 S21 @ Kenyon College

Module import script. Requires following dependencies.
"""

# Import all the things
import pyreadr
from random import randint
import os
from os import path
import sklearn
from __future__ import division
import pandas as pd
import numpy as np
import collections
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn import tree
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Convolution1D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD
from sklearn.cross_validation import cross_val_score
from keras.utils import np_utils
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
import sys
from sklearn.ensemble import GradientBoostingRegressor
import math
import csv
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import classification_report
import urllib
from sklearn.svm import LinearSVC
from utils import *