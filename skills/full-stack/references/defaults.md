# 默认名字与形状

新建项目，或给现有项目补发布流程时阅读。这里只固定要继续沿用的名字和响应形状。依赖版本和命令参数以使用时的官方文档为准，不在这里写死。已有项目沿用自己的名字，不为对齐这份清单改名。

应用边界、事务和迁移规则见 [开发与数据](development.md)。发布步骤见 [部署与恢复](deployment.md)。

## 鉴权

浏览器使用服务端 session，不默认 JWT，也不默认某个鉴权库。Cookie 只带不透明的会话标识；属性与写请求校验见 [开发与数据](development.md)。

机器凭证如何校验也见 [开发与数据](development.md)。已有认证沿用，不并行再加一套。

## 错误体

失败响应使用 HTTP 状态码，正文固定为：

```json
{
  "error": {
    "code": "not_found",
    "message": "给调用方看的说明"
  }
}
```

`code` 用稳定的 snake_case。`message` 只写调用方能看的说明，不放堆栈、SQL 或秘密。输入校验失败时可以增加 `error.details`，每项为 `path` 和 `message`。

## 脚本名

| 用途 | 脚本 |
| --- | --- |
| 从 schema 生成迁移 | `db:generate` |
| 执行迁移 | `db:migrate` |
| 初始化必要数据 | `db:seed` |

这三步和启动如何分开，见 [开发与数据](development.md)。

## 健康检查、镜像与 Compose

- 健康检查路径是 `GET /health`。进程可以接受请求时返回 200，正文为 `{"ok": true}`。
- Compose 服务名为 `caddy`、`web`、`server`。镜像为 `web` 与 `server`。test 与 production 各自一个 Compose 项目，服务名相同。

## 发布 job

一次发布拆成四个 job，构建只发生一次：

| job | 做什么 |
| --- | --- |
| `check` | 检查与测试 |
| `build` | 构建并推送镜像，记录 digest；依赖 `check` |
| `deploy-test` | 把该 digest 部署到 test；依赖 `build` |
| `deploy-production` | test 通过并得到发布授权后，把同一个 digest 晋级到 production，不重新构建 |

发布入口默认手动触发。晋级和回滚的操作步骤见 [部署与恢复](deployment.md)。
