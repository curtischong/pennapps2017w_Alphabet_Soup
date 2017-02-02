#!/usr/bin/env python3

from app import app
from flask import Flask

if __name__ == '__main__': # If it is being run directly, otherwise __name__ would be the name of the module
  app.run(host='0.0.0.0', port=80, debug=True) 