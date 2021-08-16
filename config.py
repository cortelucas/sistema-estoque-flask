import os
import random, string

class Config(object):
  CSRF_ENABLED = True
  SECRET = "61926647da9b58e9f996ba2557da19500aec84cad4bc358e137ee2ffb8ac4d87"
  TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)))
  ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
  APP = None

