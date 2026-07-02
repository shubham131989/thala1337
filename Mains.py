from ruamel.yaml import YAML

INPUT_FILE = "projects.yaml"
OUTPUT_FILE = "projects_updated.yaml"

TARGET_PROJECTS = [
    "github.com.anzx.sec-domain-vuln-agg",
    "github.com.anzx.sec-domain-sample-app",
    # add more project names here
]

NEW_TAGS = {
    "apmNumber": "apm_new_value",
    "costCentre": "12345678",
    "asset": "new-asset-name",
}

yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 4096

with open(INPUT_FILE, encoding="utf-8-sig") as f:
    data = yaml.load(f)

count = 0
for project in data["projects"]:
    if isinstance(project, dict) and project.get("name") in TARGET_PROJECTS:
        if "tags" not in project:
            project["tags"] = {}
        for key, val in NEW_TAGS.items():
            project["tags"][key] = val
        count += 1
        print(f"Updated: {project['name']}")

print(f"\nTotal updated: {count}")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    yaml.dump(data, f)
