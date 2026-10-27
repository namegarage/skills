"""Verify the public skill artifact and its coordinated release metadata."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
release = json.loads((root / "release.json").read_text())
skill = (root / "skills/catalog/SKILL.md").read_bytes()
assert hashlib.sha256(skill).hexdigest() == release["skill_sha256"], "Skill digest is stale"
for capability in release["capabilities"]:
    assert capability["tool"] in skill.decode(), "Skill capability guidance is stale"
assert f'@namegarage/sdk@{release["components"]["sdk"]}' in skill.decode(), "SDK pin is stale"
readme = (root / "README.md").read_text()
version = release["components"]["skill"]
assert f"tree/v{version}" in readme and f"--version {version}" in readme, "Skill install version is stale"
print(f'Skill release coordination passed: {release["id"]}')
