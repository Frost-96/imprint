# Odd Almanac · 独立科学小刊

[English](README.md) | **简体中文**

> 虚拟品牌，真实产出的设计练习。产品、受众和定位为假设；不是客户项目，也没有经营或用户成效数据。

![成品](previews/identity.png)

## 定位与名字

面向好奇的成年读者，以图解和短文探索不起眼的科学问题；不冒充学术期刊。

认真看看那些不太起眼的问题。

**Odd Almanac**（建议读法：odd AWL-muh-nak）。把不寻常的问题和有秩序的编排放在一起，表达带有好奇心的编辑视角。

品牌性格：好奇：偏心观察点；有编辑性：鲜明字重对比；不装权威：一处刻意不对称。

避免：伪科学符号、新闻实时性承诺、AI 星光图标。

候选命名方向：不寻常的记录：Odd Almanac / Curious Ledger；观察的动作：Look Again Press / Sideways Notes；零散问题：Loose Questions / Small Why。

| 候选 | 选择理由 / 优点 | 代价 / 风险 |
| --- | --- | --- |
| Odd Almanac | 声音和编辑性明确 | almanac 拼写长 |
| Look Again Press | 动作指向清楚 | 较长且像出版集团 |
| Small Why | 简洁 | 英语语序略生硬 |

## 图形选择与精修

![三个实际绘制的黑白方向](exploration/concepts.png)

| 方向 | 关系 | 主要风险 |
| --- | --- | --- |
| A / 偏心的观察者 | 有开口的圆围着偏心点，右侧像书页。 | 也可能读成眼睛或光学器材。 |
| B / 页边的问题 | 两条错位书脊围出问号般的负空间。 | 识别需要较大尺寸。 |
| C / 不寻常的索引 | 一组不等高书签中有一条反向。 | 更像文件管理工具。 |

采用 **A**：偏心观察点与书页边界相接，比普通书签更有编辑视角。

实际精修：将观察点稍向左移，避免和右侧书页挤在一起；保留开口与未闭合关系。

![精修前后](exploration/refinement.png)

选择由用户授权 agent 自行决定；没有声称获得真实客户或受众的选择。图形由 SVG 路径直接构造；字标使用许可字体排字、调整间距后转曲，并非原创字体。

## 使用与文件

- 主图形 / 字色 `#22221F`；浅底 `#EBE7D9`；强调色 `#D94531`；辅助色 `#B6C3C5`。强调色用于色块或装饰，不能代替文字对比度检查。

- 字标字体：Bodoni Moda + Barlow Condensed。字体文件、OFL 和来源见 [fonts](fonts/)。编辑文字版前安装随包字体；一般投放优先使用转曲版。

- 完整 Logo 建议画布宽度至少 **220 px**，图形独用建议 **16 px** 起；32/16 px 使用 `mark-small.svg`。尺寸按画布宽度计算，保持纵横比。

- 高对比 ODD 字样建议用于标题尺度；小标记不能被当作实际出版物认证。

- 保留 SVG 自带留白，外部再留至少图形宽度的 1/8；不要拉伸、增加阴影、描边或把细字压进头像。深底用白色 / 浅色反白版本。

- `sources/`：图文组合、独立字标、独立图形的彩色 / 黑 / 白 SVG，以及文字版字标与小尺寸图形。

- `exports/`：透明背景 PNG。16 px 文件是实际诊断样本，只有达到上面的建议尺寸才作为推荐用法。

- `previews/`：配色与反白展示、头像示意。头像示意不等同于平台上架图标包。

- `verification/`：实际尺寸图、源文件映射、渲染与导出一致性结果。

## 已检查与仍未验证

已检查实际黑白概念、精修、大尺寸结构、256 / 64 / 32 / 16 px 图形、220 px 宽完整 Logo，以及成品的浅底 / 深底效果。字体文字版与转曲版在 2400 px 宽进行比较，轮廓覆盖 IoU 为 1.00000000。

11 份 SVG 均可渲染，无嵌入位图；除指定文字版外没有字体依赖。23 份正式 PNG 与最终 SVG 重新渲染结果逐字节一致。文件检查通过不代表所有测试尺寸都适合使用。

名称初筛（2026-10-02）：检索出现邻近书名 The Odds Almanac，以及历史文本中的 odd almanac。未确认同名现代杂志；邻近出版物名称仍应保留为后续核查线索。

以下是实际搜索 / 复核入口；搜索结果只提供线索，不能证明没有冲突。

- 查询：`"Odd Almanac" magazine`；部分核查。[来源 1](https://www.books-by-isbn.com/0-695/0695814389-The-Odds-Almanac-James-A-Fix-David-Daughton-0-695-81438-9.html) [来源 2](https://newspaperarchive.com/marion-star-and-southern-real-estate-advertiser-apr-20-1870-p-1/) [来源 3](https://newspaperarchive.com/mills-county-tribune-dec-31-1909-p-1/)

未完成：商标、域名和社交账号可用性；完整外部图形相似性核查；真实受众认读、听写与记忆测试；完整品牌系统和平台上架包。

本轮范围为命名与 Logo 案例，完整品牌手册、真实产品应用和平台图标包不在本轮交付范围。

本案例执行当前仓库的 [skills/imprint/SKILL.md](../../skills/imprint/SKILL.md)，SHA-256：`519e787cdf6277b2e9c5caeb64dbf3b3917a53bde0ee0dc433c4a35dd548fad3`。简报、命名、选择依据与检索记录见 [结构化记录](exploration/brief.json)；可编辑矢量见 [sources/](sources/)。

[← 全部案例](../README.zh-CN.md) · [Imprint 主页](../../README.zh-CN.md)
