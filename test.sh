#!/usr/bin/env bash
set -eux

pycodestyle src
mypy src
python3 -B -m unittest discover -v
