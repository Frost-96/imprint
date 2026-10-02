# Fault Lantern

[English](README.md) | **简体中文**

![品牌视觉](previews/identity.png)

**开发工具 / 像素字形 / 琥珀终端**

虚拟产品，实际完成的 Imprint 品牌案例。产品、用户、活动、陶器、trace、接口示例及 UI 均为创作设定；不表示真实客户、真实运行软件或实体产品上市。

## 简报与定位

产品：本地开发事件捕获、状态检查与异步故障回放工具的品牌概念。面向排查间歇性测试失败或异步状态问题的开发者。

定位：**留下事件顺序，回到故障发生的位置。**

本案以英语名称和传播为假定范围，未完成多语言本地化。以下为策略选择，不是经过受众实验确认的市场事实。

性格与可见决策：可检查 → 编号事件与明确状态；聚焦调查 → 灯笼与选中事件的比喻；直接 → 像素构造与终端信息层级。

应避免：AI 魔法式承诺、游戏化怪物、没有用途的装饰代码。

## 命名探索与取舍

- 留下的顺序：Replay Spool / Event Reel
- 留存的线索：Stackwake / Trace After
- 有方向的调查：Fault Lantern / Error Beacon

| 候选 | 具体优势 | 主要成本 | 决策 |
| --- | --- | --- | --- |
| Fault Lantern | 问题类别清楚，物件意象具体 | Lantern 有相邻软件使用，必须保留完整名称 | 采用为虚拟名称 |
| Replay Spool | 记录与回放易理解 | 软件描述性用语较强，搜索识别成本高 | 退回 |
| Stackwake | 短而具有技术气质 | 已有使用线索，Stack 的语义也偏宽 | 未采用 |

选定书写为 **Fault Lantern**；读音提示：FAULT LAN-tern。Fault 指向问题，Lantern 表达照亮一个具体事件的调查意图；不是自动找到全部根因的能力承诺。

本案没有为了凑齐三名而将冲突或过弱候选包装成最终推荐；表格保留实际筛选过程与退出理由。

初筛结果：Replay Spool 已接近软件中的描述性术语和现有命令，未采用；Stackwake 有音乐及软件线索。Fault Lantern / Faultlantern 搜索未形成直接同名软件结论，但出现 LANtern 网络诊断等相邻线索，因此仍是待验证名称，不简称 Lantern。

检索日期：2026-10-02。实际查询：`"Stackwake"`；`"Replay Spool"`；`"Fault Lantern"`；`"Replay Spool" debugger`；`"Replayspool"`；`"Fault Lantern" debugging software`；`"Faultlantern"`。使用通用搜索与部分 Exa 补查；一些目标页面仅得到搜索摘要，尚未逐页完成复核。域名、社交账号、商标注册与受众听写测试未执行。

- [描述性 replay-spool 命令](https://github.com/TonicAI/distillery)
- [Stackwake 同名曲目](https://music.amazon.com/tracks/B0F9NXC1ND)
- [LANtern 相邻软件线索](https://www.linkedin.com/posts/lanternnetworks_lantern-find-the-fault-know-the-fix-activity-7502455364697747456-FXiy)

## 概念与构造

最终 A 是带单个亮点的像素灯笼；B 是返回事件的回转箭头；C 是框住事件的四角窗口。选择 A：它的物件轮廓更贴合名称，并能成为终端中的状态入口。B 类似普通撤销，C 类似裁切控件。早期磁带方案因像游戏手柄而废弃。

名称从 Replay Spool 改为 Fault Lantern；像素轮廓随之重画为提手、灯室、单点和底座。字标采用自己绘制的 5×7 像素字形，修正缩放时的内部细缝，明确使用硬边像素渲染。常规界面文字另用 JetBrains Mono。

查看 [三个黑白方向](exploration/concepts.png)、[最终黑白结构](exploration/refinement.png)、[实际尺寸图](verification/sizes.png)。开发案例的 retired 文件记录已放弃的名称与图形，不属于最终资产。

## 颜色与排版

炭绿黑承担终端背景；琥珀色突出选中事件与品牌字形；浅米黄显示内容；灰橄榄色用于次要信息。避免把像素视觉发展成游戏吉祥物。

| 角色 | HEX |
| --- | --- |
| 主文字 / 轮廓 | `#22251D` |
| 底色 | `#FCF4CE` |
| 强调 | `#FFC65B` |
| 辅助 | `#87916A` |

Fault Lantern 字标为手绘像素几何；并非现成字体，也不是一个完整的字体文件。 常规信息使用 Manrope；两个开发工具的代码、状态与事件信息使用 JetBrains Mono。全部随附字体依据各自 SIL Open Font License 分发。实例分别改名为 RangeBody、RangeBodyBold、RangeTerminal；原始来源、哈希、轴值见 `fonts/sources.json`，许可正文同目录保存。静态实例来自固定 Google Fonts 提交，修改字体不等于从零设计字体。

## 使用与交付文件

组合标志四周至少保留一个大写字形的高度；16 px 使用给定图标画布，避免任意亚像素缩放。 完整 logo 的最低建议宽度为 **280 px**；图标提供 1024、256、64、32、16 px。尺寸值描述画布，不是可见图形的宽度。小尺寸支持不表示受众一定能记住图标。

- `sources/logo-*.svg`：完整主标志，color / black / white。
- `sources/wordmark-*.svg`：单独字标；音乐、API 案例另有 `wordmark-text.svg`。
- `sources/mark-*.svg` 与 `mark-small.svg`：独立标记及小尺寸版。
- `sources/app-icon*.svg`：完整通用方形图标。32 / 16 px 导出采用 small 文件，不是平台特定上架包。
- `exports/`：1200 px 透明 PNG 标志、最低尺寸完整标志和五档图标。
- `previews/`：品牌总览与一个实际生成的应用示意。
- `verification/`：精确源文件哈希、边界、黑白色值、字体比对与导出对应检查。
- `exploration/`：选择过程、黑白构造及部分修正前版本。

保持比例与内侧留白；不要把字标强缩到 16 px；white 版本放在深色背景；浅辅助色不承担细小正文；不要给核心标志随意加阴影或描边。像素标记使用整像素定位更稳定。

## 实际验证与局限

已渲染全部最终源 SVG，检查核心矢量中没有嵌入位图、透明资产未触边裁切、黑白色值准确、图标尺寸与不透明底色正确。两种字体字标的文字版与转曲版在 2400 px 宽度下比对；另外两种自绘字标不适用字体文字比对。所有正式 PNG 导出已与对应 SVG 同尺寸重新渲染逐字节对比一致。

已目视检查大图、使用场景、黑白/反白及 256、64、32、16 px 图标；1024 px 图标完成尺寸与源对应检查，源标记亦在大图中检查。报告：[结构与渲染](verification/report.json)、[PNG 对应](verification/export-consistency.json)。

像素灯笼也可能被理解成照明或手表形图标；需要产品描述建立开发工具语境。示例 trace 是人工构造的场景，没有运行捕获、回放引擎或性能基准。

外部图形初筛只获得少量类别参考与搜索线索，未形成完整的可视排重证据；不宣称标志绝对原创、名称获准使用或具备真实市场辨识度。这些限制不影响交付文件本身用于展示本次设计流程。

[← 全部案例](../README.zh-CN.md) · [Imprint 主页](../../README.zh-CN.md)
