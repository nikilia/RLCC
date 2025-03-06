import os
import re
from datetime import datetime

# Get all meetup files
meetup_files = []
for file in os.listdir('meetups'):
    if file.endswith('.md') and re.match(r'\d{4}-\d{2}-\d{2}\.md', file):
        meetup_date = file.split('.')[0]
        meetup_files.append((meetup_date, file))

# Sort meetups by date (newest first)
meetup_files.sort(reverse=True)

# Generate meetup list in markdown
meetup_list = ""
for date, filename in meetup_files:
    # Try to extract title from file
    title = f"meetup {date}"
    try:
        with open(f'meetups/{filename}', 'r') as f:
            content = f.read()
            title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            if title_match:
                title = title_match.group(1)
    except:
        pass
    
    # Add to list
    meetup_list += f"- [{title}](meetups/{filename})\n"

# Update index.md
header = """# Rotterdam Live Coding Community

Welcome to our meetup notes repository!

## Meetups
"""

footer = """
## How to Contribute

See our [readme](README.md) for information on how to add your notes.
"""

with open('index.md', 'w') as f:
    f.write(header + "\n" + meetup_list + footer)