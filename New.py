TARGET_PROJECTS = [
    "cti-forwarder-stub",
    "integration-stub",
    # add more project names here
]

NEW_TAGS = {
    "apmNumber": "APM_NEW_VALUE",
    "criticality": "C1",
    "internetFacing": "No",
    "techArea": "New Tech Area [TA]",
    "techDomain": "New Domain [TD]",
    "techOrg": "New Org [TO]",
}

FILE = "projects.yaml"

with open(FILE, "r", encoding="utf-8-sig") as f:
    lines = f.readlines()

in_target = False
in_tags = False
tag_indent = ""
count = 0

for i, line in enumerate(lines):
    stripped = line.strip()

    # Detect project name (e.g., "- name: cti-forwarder-stub")
    if stripped.startswith("- name:"):
        name = stripped.split("- name:", 1)[1].strip()
        in_target = name in TARGET_PROJECTS
        in_tags = False
        if in_target:
            count += 1
            print(f"Found: {name}")
        continue

    # Detect tags: block
    if in_target and stripped == "tags:":
        in_tags = True
        continue

    # Replace tag values
    if in_target and in_tags:
        for key, val in NEW_TAGS.items():
            if stripped.startswith(key + ":"):
                # Preserve the original indentation exactly
                indent = line[:len(line) - len(line.lstrip())]
                lines[i] = f'{indent}{key}: "{val}"\n'
                break
        else:
            # If line doesn't match any tag key, we've exited the tags block
            if stripped and not stripped.startswith("#"):
                in_tags = False
                in_target = False

with open(FILE, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"\nTotal updated: {count}")
