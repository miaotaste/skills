import re
import sys
from pathlib import Path

fail = 0
link = re.compile(r"\[[^\]]*\]\(([^)\s]+)")
for skill in sorted(p for p in Path("skills").iterdir() if p.is_dir()):
    text = (skill / "SKILL.md").read_text()
    name = re.search(r"^name:\s*(\S+)\s*$", text, re.M)
    if not name or name.group(1) != skill.name:
        print(f"name 与目录不一致: {skill}")
        fail = 1
    yaml = (skill / "agents" / "openai.yaml").read_text()
    if not re.search(r"^interface:\s*$", yaml, re.M) or not re.search(r"^policy:\s*$", yaml, re.M):
        print(f"openai.yaml 缺少 interface 或 policy: {skill}")
        fail = 1
    for md in skill.rglob("*.md"):
        for target in link.findall(md.read_text()):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path = target.split("#", 1)[0]
            if path and not (md.parent / path).exists():
                print(f"链接不存在: {md} -> {target}")
                fail = 1
sys.exit(fail)
