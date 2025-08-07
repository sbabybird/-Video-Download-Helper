# 项目名称：视频下载助手浏览器插件

## 1. 项目目标

开发一个浏览器插件（兼容 Chrome、Edge），用于检测主流视频网站（如 YouTube, Twitter, Pornhub 等）的视频内容。插件会在视频播放器附近显示一个下载图标，用户点击该图标后，插件将调用本地安装的 `yt-dlp` 命令行工具来下载当前视频。

## 2. 核心功能

- **视频检测**: 自动在页面上识别 `<video>` 元素或特定网站的视频播放器。
- **UI注入**: 在检测到的视频元素上层浮动一个清晰、易于点击的下载按钮。
- **调用本地应用**: 通过 Native Messaging 技术，将视频页面的URL发送给一个本地辅助应用。
- **执行下载**: 本地辅助应用接收到URL后，调用 `yt-dlp` 执行视频下载任务。
- **用户反馈**: （可选）向用户显示下载已开始或下载失败的通知。

## 3. 技术架构

本项目分为两大部分：浏览器插件本身和与操作系统交互的本地应用。

### 3.1. 浏览器插件 (Browser Extension)

- **清单 (Manifest V3)**: 使用 `manifest.json` 定义插件的权限、脚本和元数据。
  - `permissions`: 需要 `nativeMessaging` (与本地应用通信), `activeTab` 或 `scripting` (在页面注入脚本和样式)。
  - `content_scripts`: 注入到网页中，负责检测视频和创建下载按钮。
  - `background` (Service Worker): 作为后台服务，负责监听来自 `content_script` 的消息，并与 Native Host 通信。
- **内容脚本 (`content_script.js`)**:
  - 职责：DOM 扫描，查找视频播放器。
  - 交互：创建下载按钮并附加到页面，监听按钮点击事件，并将视频URL发送给 `background` 脚本。
- **背景脚本 (`background.js`)**:
  - 职责：接收 `content_script` 的消息，并通过 `chrome.runtime.sendNativeMessage` 将数据（视频URL）发送到 Native Host。

### 3.2. 本地通信应用 (Native Messaging Host)

由于浏览器插件出于安全原因无法直接执行本地程序（如 `yt-dlp.exe`），我们需要一个中间层。

- **通信脚本 (`native_host.py`)**:
  - 语言：使用 Python 编写，因为它能很好地处理JSON输入输出和调用子进程。
  - 职责：
    1.  从标准输入 (stdin) 读取浏览器插件发来的JSON消息（包含视频URL）。
    2.  解析消息，构建 `yt-dlp` 下载命令 (例如: `yt-dlp.exe [URL] --output "C:/Users/admin/Downloads/%(title)s.%(ext)s"`).
    3.  使用 `subprocess` 模块在后台执行该命令。
- **主机清单 (`manifest.json`)**:
  - 这是一个JSON文件，但它属于本地应用，不是插件的一部分。
  - 职责：告诉浏览器本地通信脚本 (`native_host.py`) 的位置，以及允许哪些插件ID与之通信。
- **安装脚本 (`install.bat`)**:
  - 职责：在Windows上，此脚本负责创建必要的注册表项，将 Native Host 的清单文件路径告知浏览器。这是 Native Messaging 能够工作的关键步骤。

## 4. 开发步骤规划

1.  **环境准备**: 确认 `yt-dlp.exe` 已下载并能从命令行运行。
2.  **插件基础**: 创建 `manifest.json` 和空的 `content_script.js`、`background.js` 文件。
3.  **内容脚本开发**: 编写逻辑以检测通用 `<video>` 标签，并成功注入一个测试按钮。
4.  **消息传递**: 实现从 `content_script` 到 `background` 的消息发送（当按钮被点击时）。
5.  **Native Host 脚本**: 编写 `native_host.py`，使其能够接收固定的URL并成功调用 `yt-dlp`。先在命令行独立测试此脚本。
6.  **集成与安装**: 创建 Native Host 的 `manifest.json` 和 `install.bat` 脚本，并运行它以完成注册。
7.  **端到端测试**: 在浏览器中加载插件，点击注入的按钮，验证 `yt-dlp` 是否被成功调用并开始下载。
8.  **功能完善**:
    - 针对 YouTube 等特殊网站进行适配。
    - 优化下载按钮的样式和位置。
    - 添加错误处理和用户通知。

## 5. 关键挑战

- **网站适配性**: 不同网站的视频播放器实现方式各异，可能需要为特定网站编写定制的检测逻辑。
- **Native Messaging 配置**: `install.bat` 的注册表操作必须准确无误，否则浏览器将无法找到本地应用。
- **`yt-dlp` 路径**: Native Host 脚本需要能找到 `yt-dlp.exe`。初期可以假定它与脚本在同一目录，后期可以考虑让用户配置路径或从系统PATH搜索。
