#!/usr/bin/env python3
"""Runs build_ebt.py (build + validation) then ml_ebt.py (baseline). Run: python3 build_all.py"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, os.path.join(HERE, 'build_ebt.py')], cwd=HERE, check=True)
subprocess.run([sys.executable, os.path.join(HERE, 'ml_ebt.py')], cwd=HERE, check=True)
