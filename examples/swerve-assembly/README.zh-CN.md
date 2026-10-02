# Swerve Assembly

[English](README.md) | **简体中文**

![品牌视觉](previews/identity.png)

**地下电子音乐 / 倾斜宽字 / 酸性色彩**

虚拟产品，实际完成的 Imprint 品牌案例。产品、用户、活动、陶器、trace、接口示例及 UI 均为创作设定；不表示真实客户、真实运行软件或实体产品上市。

## 简报与定位

产品：地下电子音乐聆听活动与独立发行品牌。面向成年听众、小型独立音乐制作人。

定位：**给节奏里的转弯，留一个聚在一起的地方。**

本案以英语名称和传播为假定范围，未完成多语言本地化。以下为策略选择，不是经过受众实验确认的市场事实。

性格与可见决策：不安分 → 倾斜宽字；集体感 → 保留完整 Assembly 名称；大胆 → 大幅裁切与对比配色。

应避免：通用闪电图形、金属质感游戏标志、企业工业权威感。

## 命名探索与取舍

- 不循常拍：Offmeter / Side Pulse
- 集体的意外：Jolt Choir / Swerve Assembly
- 解开时间：Ravel Hour / Loose Measure

| 候选 | 具体优势 | 主要成本 | 决策 |
| --- | --- | --- | --- |
| Swerve Assembly | 动词感强，集体意味明确 | Swerve 有拼写学习成本，Assembly 较长 | 采用为虚拟名称 |
| Jolt Choir | 短促而出人意料 | 容易被理解为合唱组织，已有相关使用结果 | 保留比较，未采用 |
| Ravel Hour | 有时间与解开缠绕的意象 | Ravel 的作曲家联想会影响定位 | 保留比较，未采用 |

选定书写为 **Swerve Assembly**；读音提示：SWURV uh-SEM-blee。Swerve 表达偏离既定路线的动势，Assembly 表达聚集；这是本次品牌意图，不主张独有词源。

本案没有为了凑齐三名而将冲突或过弱候选包装成最终推荐；表格保留实际筛选过程与退出理由。

初筛结果：Offmeter 有音乐相关使用；Swerve Assembly 的精确及品类搜索主要出现机器人装配语义。Jolt Choir 有合唱团相关结果，Ravel Hour 容易进入作曲家语境。未据此宣称选定名称可独占。

检索日期：2026-10-02。实际查询：`"Offmeter"`；`"Jolt Choir"`；`"Swerve Assembly"`；`"Ravel Hour" music`；`"Swerve Assembly" music label events`。使用通用搜索与部分 Exa 补查；一些目标页面仅得到搜索摘要，尚未逐页完成复核。域名、社交账号、商标注册与受众听写测试未执行。

- [Offmeter 音乐使用线索](https://soundcloud.com/deqwan-offmeter-chapman)
- [Swerve assembly 机器人装配用语](https://docs.wcproducts.com/welcome/gearboxes/wcp-swerve-x/misc/changelog)

## 概念与构造

A 是带偏移短节的 S 形转弯；B 是错位节拍条；C 是普通的双行集合字标。选择 A：轮廓比节拍条更紧凑，能延伸成海报中的转弯线条。代价是单独 S 图形容易与其他字母标记接近，需要完整名称建立识别。

保留不等长端点和分离短节；字标以 Manrope 750 为基础，调整字符间距、横向比例与倾斜角。黑白结构无需颜色也能成立。最小完整字标宽度提高到 320 px，以保留 ASSEMBLY 的可读性。

查看 [三个黑白方向](exploration/concepts.png)、[最终黑白结构](exploration/refinement.png)、[实际尺寸图](verification/sizes.png)。开发案例的 retired 文件记录已放弃的名称与图形，不属于最终资产。

## 颜色与排版

蓝紫用于大背景和图形；酸性黄绿承担主体与反差；浅紫用于斜带和流动线条；深墨色与淡底色用于普通信息。高饱和处理服务音乐传播，不沿用工业品牌的黑橙秩序。

| 角色 | HEX |
| --- | --- |
| 主文字 / 轮廓 | `#191440` |
| 底色 | `#EDEEFF` |
| 强调 | `#C6FF36` |
| 辅助 | `#E69CF6` |
| 音乐主场色 | `#3336E8` |

字标基于 Manrope 的静态实例，并提供文字可编辑源与转曲版。 常规信息使用 Manrope；两个开发工具的代码、状态与事件信息使用 JetBrains Mono。全部随附字体依据各自 SIL Open Font License 分发。实例分别改名为 RangeBody、RangeBodyBold、RangeTerminal；原始来源、哈希、轴值见 `fonts/sources.json`，许可正文同目录保存。静态实例来自固定 Google Fonts 提交，修改字体不等于从零设计字体。

## 使用与交付文件

完整字标外部净空至少为其画布高度的 1/4；单独标记四周至少 32/256 个画布宽度。 完整 logo 的最低建议宽度为 **320 px**；图标提供 1024、256、64、32、16 px。尺寸值描述画布，不是可见图形的宽度。小尺寸支持不表示受众一定能记住图标。

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

孤立的 S 并不能保证独特性；本次没有完成全面图形排重。16 px 仍能分开主要轮廓和短节，但细节比 32 px 弱。

外部图形初筛只获得少量类别参考与搜索线索，未形成完整的可视排重证据；不宣称标志绝对原创、名称获准使用或具备真实市场辨识度。这些限制不影响交付文件本身用于展示本次设计流程。

[← 全部案例](../README.zh-CN.md) · [Imprint 主页](../../README.zh-CN.md)
