# Skills

个人可复用的 Agent Skills，使用 [Skills CLI](https://github.com/vercel-labs/skills) 安装。

## 可用 Skills

| Skill | 用途 |
| --- | --- |
| [commit-msg](skills/commit-msg/SKILL.md) | 根据 Git 暂存区生成中文提交信息 |
| [full-stack](skills/full-stack/SKILL.md) | 全栈项目的技术选型、架构、开发验证与部署 |
| [illustration](skills/illustration/SKILL.md) | 使用 Excalidraw 绘制技术插图，交付展示图与可编辑源文件 |

## 安装

发布到 GitHub 后，将以下 `<owner>/<repo>` 替换为本仓库的实际地址：

```sh
npx skills add <owner>/<repo>
```

选择单个 skill：

```sh
npx skills add <owner>/<repo> --skill illustration
```

默认安装到当前项目；添加 `-g` 可安装到用户级目录，供多个项目使用。

发布前在仓库根目录列出可发现的 skill：

```sh
npx skills add . --list
```

## 目录约定

每个 skill 在 `skills/<name>/` 中独立维护，以包含 `name` 和 `description` 的 `SKILL.md` 为入口。`agents/` 保存 Agent 配置，`references/` 保存按需读取的参考文档。相对路径始终以对应 skill 目录为基准。
