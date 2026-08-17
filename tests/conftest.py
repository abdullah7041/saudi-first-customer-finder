"""Put the generator's directory on sys.path.

The script lives inside the skill payload rather than an installable package,
so tests import it by path rather than by module name.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "saudi-first-customer-finder" / "scripts"
sys.path.insert(0, str(SCRIPTS))
