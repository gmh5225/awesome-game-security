filename = "../README.md"
insert_line = 3

indent_lookup = {
    '## ': 0,
    '### ': 1, # unused right now
    '#### ': 2, # unused right now
}


found_items = []

f = open(filename, "r")
readme_lines = f.readlines()
f.close()

for line in readme_lines:
    for prefix in indent_lookup:
        if line.startswith(prefix):
            heading = line[len(prefix):].strip()
            heading_ref = heading.replace(' ', '-')
            found_items.append('%s- [%s](#%s)' % ('\t' * indent_lookup[prefix], heading, heading_ref))
    pass

for item in found_items:
    print(item)

readme_lines.insert(insert_line, '## Contents\n')

for i in range(len(found_items)):
    item = found_items[i]
    readme_lines.insert(insert_line + i + 1, item + '\n')
    pass

readme_lines.insert(insert_line + len(found_items) + 1, '\n')

f = open(filename, "w")
f.writelines(readme_lines)
f.close()
