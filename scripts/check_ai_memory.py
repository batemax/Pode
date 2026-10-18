#!/usr/bin/env python3
"""检查 AI 记忆结构；不验证语义、不改写内容。"""
from datetime import date
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "AGENTS.md": ["每次任务开始前", "强制收尾"],
    ".ai/Memory.md": ["更新时间：", "已确认需求"],
    ".ai/Context.md": ["更新时间：", "当前阶段", "下一步"],
    ".ai/tasks/current.md": ["更新时间：", "状态：", "验收记录"],
    ".ai/logs/operations.md": ["操作：", "验证：", "记忆核对：", "遗留项："],
    ".ai/checklists/task-completion.md": ["Memory.md", "Context.md"],
}

def main():
    errors = []
    for name, markers in REQUIRED.items():
        path = ROOT / name
        if not path.is_file():
            errors.append(f"缺少文件：{name}")
            continue
        content = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in content:
                errors.append(f"{name} 缺少字段：{marker}")
        if "更新时间：" in markers:
            match = re.search(r"更新时间：(\d{4}-\d{2}-\d{2})", content)
            try:
                if not match:
                    raise ValueError()
                date.fromisoformat(match.group(1))
            except ValueError:
                errors.append(f"{name} 更新时间格式无效")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("AI 记忆结构检查通过；内容准确性与本次任务同步情况仍需人工或 AI 核对。")
    return 0

if __name__ == "__main__":
    sys.exit(main())
