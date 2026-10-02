# Palm Silt

[English](README.md) | **简体中文**

![品牌视觉](previews/identity.png)

**陶艺工作室 / 手绘字形 / 土色与材质**

虚拟产品，实际完成的 Imprint 品牌案例。产品、用户、活动、陶器、trace、接口示例及 UI 均为创作设定；不表示真实客户、真实运行软件或实体产品上市。

## 简报与定位

产品：手捏陶器与小型工作室课程品牌。面向喜欢制作痕迹的日用品使用者，以及成年手作初学者。

定位：**把手的动作，留在日常器物里。**

本案以英语名称和传播为假定范围，未完成多语言本地化。以下为策略选择，不是经过受众实验确认的市场事实。

性格与可见决策：有触感 → 不规则轮廓与朴素手写字；温暖 → 陶土与燕麦色表面；从容 → 低密度排版与材质静物图。

应避免：奢华衬线印章、可爱吉祥物、虚构的古老工艺传承。

## 命名探索与取舍

- 泥土与手势：Palm Silt / Loamfold
- 柔软与烧制：Tender Kiln / Warm Vessel
- 制作者的痕迹：Thumbwell / Palm Note

| 候选 | 具体优势 | 主要成本 | 决策 |
| --- | --- | --- | --- |
| Palm Silt | 两个短词，手与材料关系明确 | 需要介绍品类，不应解释为真实原料配方 | 采用为虚拟名称 |
| Tender Kiln | 柔软与烧制形成反差 | Tender 已有相邻品类使用线索 | 未采用 |
| Thumbwell | 与指压印痕贴近 | 技术术语联想偏重，读音未经受众测试 | 未采用 |

选定书写为 **Palm Silt**；读音提示：PAHM silt（按目标口音读 palm）。Palm 与 Silt 组合手掌和土质的触觉意象；不表示产品实际配方由粉砂构成。

本案没有为了凑齐三名而将冲突或过弱候选包装成最终推荐；表格保留实际筛选过程与退出理由。

初筛结果：Loamfold 已有服装品牌。Tender Kiln 的检索出现窑炉与玻璃艺术语义，且 Tender 也出现在陶器类别；Thumbwell 是已有技术术语。Palm Silt 与 Palmsilt 的检索多为两词语义匹配，并出现 Palm Élan / Silt Design Studio 的相邻词线索，未完成可用性验证。

检索日期：2026-10-02。实际查询：`"Loamfold"`；`"Palm Silt"`；`"Tender Kiln"`；`"Thumbwell" ceramics`；`"Palmsilt"`；`"Palm Silt" ceramics`；`"Palm Silt" pottery studio`。使用通用搜索与部分 Exa 补查；一些目标页面仅得到搜索摘要，尚未逐页完成复核。域名、社交账号、商标注册与受众听写测试未执行。

- [Loamfold 品牌自述](https://loamfold.com/pages/statement-of-faith)
- [Tender 玻璃作品检索结果](https://www.vitreus-art.co.uk/tender-fused-vitreus-art.html)
- [Thumbwell 术语来源](https://www.globalpointofcare.abbott/content/dam/ardx/globalpointofcare/apoc/support/i-stat-1/technical-bulletins/english/istat-large-thumbwell/738598-00B.pdf)
- [相邻词使用线索](https://www.palmelan.com/)

## 概念与构造

A 是内侧带压痕的不规则开口形；B 是托起器物的双手；C 是仅保留制作者笔迹。选择 A 配合手绘字标：既能保留触觉，也有可独立使用的印记。B 容易被读成爱心，C 缺少紧凑入口。

逐字绘制 palm silt 的圆头单线笔画，保留适度高低差。最初小尺寸版删掉内侧印痕，目视检查发现只剩普通圆环，因此改为更粗、更短的内侧曲线；保留修正前的尺寸板供比较。

查看 [三个黑白方向](exploration/concepts.png)、[最终黑白结构](exploration/refinement.png)、[实际尺寸图](verification/sizes.png)。开发案例的 retired 文件记录已放弃的名称与图形，不属于最终资产。

## 颜色与排版

土棕用于文字与印记；燕麦色作背景；赭陶色用于大面和标签；灰石色只作辅助。材质主要由静物图呈现，不把纹理烘焙进核心 logo。

| 角色 | HEX |
| --- | --- |
| 主文字 / 轮廓 | `#573C30` |
| 底色 | `#F2E6D5` |
| 强调 | `#B76E50` |
| 辅助 | `#B4B1A0` |

Palm Silt 的字标为手绘单线矢量；没有可直接键入的对应字体。 常规信息使用 Manrope；两个开发工具的代码、状态与事件信息使用 JetBrains Mono。全部随附字体依据各自 SIL Open Font License 分发。实例分别改名为 RangeBody、RangeBodyBold、RangeTerminal；原始来源、哈希、轴值见 `fonts/sources.json`，许可正文同目录保存。静态实例来自固定 Google Fonts 提交，修改字体不等于从零设计字体。

## 使用与交付文件

组合标志外部净空至少为整体画布高度的 1/4；独立印记四周至少留出 32/256 个画布宽度。 完整 logo 的最低建议宽度为 **240 px**；图标提供 1024、256、64、32、16 px。尺寸值描述画布，不是可见图形的宽度。小尺寸支持不表示受众一定能记住图标。

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

16 px 仅用于已建立识别后的入口；32 px 以上更容易看清内侧印痕。静物图是生成图像，不是实际制作、烧制或拍摄的产品。

外部图形初筛只获得少量类别参考与搜索线索，未形成完整的可视排重证据；不宣称标志绝对原创、名称获准使用或具备真实市场辨识度。这些限制不影响交付文件本身用于展示本次设计流程。

静物图由内置 imagegen 生成；原图见 `previews/still-life-original.png`，完整实际提示词见 `exploration/imagegen-prompt.txt`。核心 logo 独立构造，未从照片提取商标，也未将照片嵌入核心 logo SVG。

[← 全部案例](../README.zh-CN.md) · [Imprint 主页](../../README.zh-CN.md)
