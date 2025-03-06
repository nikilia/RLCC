import os
import re
from datetime import datetime

# Get all meeting files
meeting_files = []
for file in os.listdir('meetings'):
    if file.endswith('.md') and re.match(r'\d{4}-\d{2}-\d{2}\.md', file):
        meeting_date = file.split('.')[0]
        meeting_files.append((meeting_date, file))

# Sort meetings by date (newest first)
meeting_files.sort(reverse=True)

# Generate meeting list in markdown
meeting_list = ""
for date, filename in meeting_files:
    # Try to extract title from file
    title = f"Meeting {date}"
    try:
        with open(f'meetings/{filename}', 'r') as f:
            content = f.read()
            title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            if title_match:
                title = title_match.group(1)
    except:
        pass
    
    # Add to list
    meeting_list += f"- [{title}](meetings/{filename})\n"

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
    f.write(header + "\n" + meeting_list + footer)