#lint.py 
import sys
from pylint import lint
THRESHOLD =9
run=lint.Run(["factorial1.py"],exit=False)
score=run.linter.stats.global_note
if score<THRESHOLD:
    print("Linter failed: score<threshold value to change")
    sys.exit(1)
sys.exit(0)