# LEARNINGS — Error Confinement Live Demo

Project-specific lessons from development and deployment.

## L1: Single-File HTML is the fastest path to interactive evidence
- **Category:** METHODOLOGY
- **Issue:** Multi-file web apps with build steps add deployment complexity.
- **Solution:** Single HTML file with inline CSS/JS. No build, no dependencies, instant Pages deploy.
- **Prevention:** Start with single-file. Only split into multi-file when complexity demands it.
- **Cross-Project:** YES — all 5 QWAV demo artifacts follow this pattern.

## L2: Canvas non-zero-pixel check is the minimum viable functional test
- **Category:** TESTING
- **Issue:** HTML page can load without errors but canvas may be blank.
- **Solution:** After deploy, check canvas.getImageData() for non-zero pixels.
- **Prevention:** Add to deploy checklist: verify canvas content renders.
- **Cross-Project:** YES — applies to all canvas-based demos.

## L3: GitHub Pages has a 1-2 minute rebuild delay
- **Category:** DEPLOYMENT
- **Issue:** Pushing fixes doesn't make them immediately visible.
- **Solution:** Wait 30-90 seconds after push before verifying. Use cache-busting query parameters.
- **Prevention:** Always verify after a short delay. Don't assume instant deploy.
- **Cross-Project:** YES.

## L4: Interactive verification catches JS bugs that syntax checks miss
- **Category:** TESTING
- **Issue:** Code with no syntax errors can still fail at runtime (e.g., IIFE semicolon bug).
- **Solution:** After every JS change, test actual user interaction (move slider, click button).
- **Prevention:** Include interaction test in the Definition of Done.
- **Cross-Project:** YES.

---

*Learned during ultrametric-error-confinement-demo development. Cross-project candidates added to CROSS-PROJECT-LEARNINGS.md.*
