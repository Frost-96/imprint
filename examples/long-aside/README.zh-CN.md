# Long Aside — 虚拟案例 / 实际执行

[English](README.md) | **简体中文**

![品牌视觉](previews/identity.png)

文学 / 字标主导 / 编辑留白。本案例于 2026-10-02 使用 Imprint 实际完成；产品、人物、记录、文章均为虚构，不代表真实客户或上线产品。

## 简报与策略

产品：独立作者长文与短篇的数字出版、阅读和版本注记空间。面向小型文学刊物、独立作者与愿意慢读的读者。

问题：文章被信息流切碎，刊物很难保留自己的编辑节奏与持续可读的篇目。

定位：**为独立文章保留一个值得停留的阅读空间。**

价值范围：以期刊和篇目组织阅读，保留作者注记与版本关系；不代替编辑判断或承诺流量收益。

关键性格：有余韵、独立、从容。使用场景：刊物封面、文章阅读页、移动阅读入口。

## 命名过程

先提出三个命名方向、六个候选，再筛选三个短名单：Long Aside / Afterleaf / Paper Interval。

- 值得停留的旁白：Long Aside / Minor Hours
- 读完后还留着的一页：Afterleaf / Second Paper
- 文章之间留出的呼吸：Paper Interval / Dear Interval

选择：Long Aside / long uh-SIDE。以“较长的旁白”关联编辑立场与慢阅读。完整名称有语义，但自然短语的搜索独占性较弱。

公开初筛：Afterleaf 已有软件使用，退出候选。Long Aside 检索命中文学语境中的普通短语；另有 Aside 语音笔记应用，所以保留完整 Long Aside，不简称 Aside。Paper Interval 的语义较抽象，未继续发展。尚未完成域名、各地区商标或应用商店全面核查。

以上是有限公开检索。部分证据仅来自搜索返回内容，未全部完成页面复核；没有做商标可用性结论。图形检索尝试未形成足够可视证据，外部图形相似性审核仍不完整。

- [Afterleaf 现有应用](https://www.afterleaf.app/)
- [出版商使用 long aside 短语](https://www.lianalevi.fr/foreign-rights/disoriental/)
- [Aside 应用](https://apps.apple.com/ph/app/aside-voice-notes-ai/id6758001568)

## 黑白方向与修正

A：斜体与正体错行；B：单行编辑式字标；C：括号与间隔。选择 A，以行间停顿和错位表达旁白。B 过于常规；C 的标点语汇过于通用。

扩大上下行间隔，第二行向右移动。Bodoni Moda 从较细的展示设置调整为 wght 550、opsz 24，改善细笔画。紧凑图标采用更重的斜体 a 与旁注竖线（wght 700、opsz 12）；16 px 再加粗竖线。阅读页导航采用紧凑标记与普通产品名称，不把大字标强缩进窄导航。

查看 [三个黑白方向](exploration/concepts.png) 与 [最终黑白适配](exploration/refinement.png)。初始概念和最终源文件有意保留差异，以展示真实取舍。

## 颜色与字体

深葡萄色承担主文字；纸白提供阅读背景；冷蓝用于篇目插画与标记；铜棕仅作少量辅助。

| 角色 | 色值 |
| --- | --- |
| 主体 | `#382437` |
| 底色 | `#F4EFE6` |
| 强调 | `#AFC5DA` |
| 辅助 | `#A6775B` |

字标基于 **Bodoni Moda**，信息字体为 Manrope；使用现有字体的字形与定制间距，不宣称从零设计字体。字体来源锁定到 Google Fonts 仓库提交 `9710da1eacb3be272583c3224dcb70f9da6eadbb`。`fonts/sources.json` 记录源 URL、原文件 SHA-256、实例轴值和修改后名称。静态实例重命名为 Range 系列，随包附原始 SIL Open Font License；字体授权以随附 OFL 为准。

## 使用与交付

完整错行字标建议至少 320 px 宽；紧凑标记建议至少 32 px，16 px 用专用 small 版本。完整字标外部净空至少为总高度的 1/8；紧凑标记为画布宽度的 1/8。 这些最小值是本次渲染与目视检查的建议，并未经过受众实验。

- `sources/logo-*.svg`：主标志；color、black、white 三种。white 文件需要深色背景。
- `sources/wordmark-*.svg`：转曲字标；`wordmark-text.svg` 保留可编辑文字并嵌入字体，修改文字后仍需重新检查字距。
- `sources/mark-*.svg`：独立识别元素；`mark-small.svg` 是小尺寸适配。
- `sources/app-icon*.svg`：无预切圆角的通用方形图标，不是某个平台完整上架包。
- `exports/`：透明 PNG 标志，以及 1024、256、64、32、16 px 图标。
- `previews/`：视觉总览与一个真实生成的应用示意；界面不可操作。
- `verification/`：尺寸检查、源文件哈希、文字与转曲比对、导出一致性报告。
- `exploration/`：三个概念和黑白修正板。亲子案例另含图像生成原图与完整提示词。

不要拉伸、描边或给 logo 添加投影；不要把整体完整字标强缩到 16 px；避免将低对比的辅助色用于细小正文。SVG 中有基础图形和字形路径，核心标志未用嵌入位图冒充矢量。

## 验证结论与剩余问题

已检查 SVG 结构、实际渲染边界、黑白色值、透明背景、图标尺寸，以及文字版与转曲版的渲染对应；所有交付 PNG 均与对应 SVG 在相同尺寸重新渲染的结果逐字节一致。详见 [检查报告](verification/report.json)、[导出对应检查](verification/export-consistency.json)、[尺寸实图](verification/sizes.png)。

衬线编辑风格的类别相似性较强。图标也可能被读成 al，独立识别力弱于完整名称，需要与名称共同建立认知。

本次可以用来展示 skill 的流程和交付能力；不能把它表述为客户验证、商标批准或所有 agent 均已实测兼容。

[← 全部案例](../README.zh-CN.md) · [Imprint 主页](../../README.zh-CN.md)
