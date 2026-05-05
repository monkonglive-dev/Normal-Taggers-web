#!/usr/bin/env python3
# Read file
with open('/home/team/shared/index.html', 'r') as f:
    content = f.read()

# Current bad embed URL
old = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m12!1m3!1d3112.522204550186!2d-121.2850!3d38.7495!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x809b1f7d54483e53%3A0x6b87c714c670737c!2s956%20Oak%20Ln%2C%20Roseville%2C%20CA%2095678!5e0!3m2!1sen!2sus!4v1714800000000!5m2!1sen!2sus'

# Correct embed URL using Rio Java's actual place ID
new = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m12!1m3!1d3111.525!2d-121.4440!3d38.6910!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x809b29c3176d9539%3A0xf8efb5d98e7b6ae!2sRio%20Java%20Coffee%20House!5e0!3m2!1sen!2sus!4v1714800000000!5m2!1sen!2sus'

if old in content:
    content = content.replace(old, new)
    with open('/home/team/shared/index.html', 'w') as f:
        f.write(content)
    print('SUCCESS: Map embed URL updated!')
else:
    print('ERROR: Old URL not found exactly')
    # Check what we have
    import re
    match = re.search(r'maps/embed\?pb=[^"]+', content)
    if match:
        print('Found URL:', match.group(0)[:100])
