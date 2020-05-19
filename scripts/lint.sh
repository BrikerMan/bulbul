#!/usr/bin/env bash

set -e
set -x

mypy bulbul --config-file=.config.ini
flake8 bulbul --config=.config.ini
