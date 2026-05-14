import os, shutil

releases_dir = r'G:\My Drive\Obsidian\releases\2025\00'
project_dir = r'G:\My Drive\projects\Tree Distance Cophenetic'

# Key files most relevant to the Tree Distance Cophenetic project
relevant_files = [
    '42 Theses on the Nature of a Pattern-Based Reality.md',
    'Grammar of Reality.md',
    'Coherence and Generativity Framework.md',
    'Comparing Fundamental Frameworks.md',
    'Autaxic Trilemma.md',
    '5I.md',
    'Imperfectly Defining Reality.md',
    'Exploring Analogous Foundational Principles and Generative Ontologies.md',
    'Before the Big Bang.md',
    'Beyond the Tyranny of Math.md',
]

for fname in relevant_files:
    src = os.path.join(releases_dir, fname)
    dst = os.path.join(project_dir, f'src_0.2_{fname}')
    if os.path.exists(src):
        shutil.copy2(src, dst)
        sz = os.path.getsize(dst)
        print(f'COPIED: {fname} ({sz} bytes)')
    else:
        print(f'MISSING: {fname}')
