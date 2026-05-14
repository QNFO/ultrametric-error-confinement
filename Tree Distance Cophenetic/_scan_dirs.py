import os

releases = r'G:\My Drive\Obsidian\releases'
archive = r'G:\My Drive\Archive'

def scan_dir(path, label, max_files=80):
    results = []
    count = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            if count >= max_files:
                break
            fp = os.path.join(root, f)
            sz = os.path.getsize(fp)
            rel = os.path.relpath(fp, path)
            results.append((sz, rel))
            count += 1
        if count >= max_files:
            break
    print(f'=== {label} ({len(results)} files shown) ===')
    for sz, rel in sorted(results, key=lambda x: x[1]):
        print(f'{sz:>8d}  {rel}')
    print()

scan_dir(releases, 'RELEASES')
scan_dir(archive, 'ARCHIVE')
