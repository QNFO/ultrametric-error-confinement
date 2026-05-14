import os, shutil

releases_dir = r'G:\My Drive\Obsidian\releases\2025\00'
project_dir = r'G:\My Drive\projects\Tree Distance Cophenetic'

# Additional critical files
more_files = [
    'Autaxys Defined.md',
    'Autaxys and its Generative Engine.md',
    'Ultimate Reality Framework Examination.md',
    'Illusion of Time.md',
    'Statistics of Possibility.md',
    'Ten-Fingered Trap.md',
]

for fname in more_files:
    src = os.path.join(releases_dir, fname)
    dst = os.path.join(project_dir, f'src_0.2_{fname}')
    if os.path.exists(src):
        shutil.copy2(src, dst)
        sz = os.path.getsize(dst)
        print(f'COPIED: {fname} ({sz} bytes)')
    else:
        print(f'MISSING: {fname}')
