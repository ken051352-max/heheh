"""Select which implementation the tests import.

Default: your code in starter/.  Maintainers / CI set NPFS_IMPL=reference to prove the tests are correct.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
IMPL = os.environ.get("NPFS_IMPL", "starter")
if IMPL not in ("starter", "reference"):
    raise SystemExit("NPFS_IMPL must be 'starter' or 'reference'")
sys.path.insert(0, os.path.join(os.path.dirname(HERE), IMPL))
