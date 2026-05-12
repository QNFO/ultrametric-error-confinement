# LEARNINGS

### L1: Computational validation is legitimate evidence
- **Category:** METHODOLOGY
- **Issue:** No lab access, no empirical evidence.
- **Solution:** Python simulation produces reproducible, sharable data.
- **Result:** Tree LER=0 at depth 3+ is strong signal.

### L2: Bruhat-Tits trees are efficiently implementable
- **Category:** PYTHON
- **Issue:** Concern about computational intractability.
- **Solution:** Tree scales as O(p^d). For p=2, d=5 = 63 nodes. Trivial.

### L3: Nested directory bug fixed
- **Category:** PYTHON
- **Issue:** Relative path created nested simulations/simulations/plots/.
- **Solution:** Fixed to simulations/plots/ directly.
