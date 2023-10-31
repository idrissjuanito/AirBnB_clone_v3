#!/usr/bin/env bash
find . -type f -name "*.py" -exec sed -E -i "" -e 's/env python3/python3/' {} +\
	|| find . -type f -name "*.py" -exec sed -E -i "" -e 's/\/python3/\/env python3/' {} +
