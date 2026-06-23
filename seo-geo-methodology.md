# SEO/GEO 建站方法论（从本地 KB 提炼）

把 `seo-geo-kb`（6084 篇）+ `klaviyo-marketing` 的 SEO/GEO 内容，提炼成 site-factory
第 3 步可直接执行的清单。**每条带 KB 出处**；执行时用本地 skill（ai-seo /
schema-markup / programmatic-seo / on-page-seo-auditor / internal-linking-optimizer），
事实接地查本库（`search.py`）。本文件是"做成方法论"的产物，不是营销文案。

> 用法：site-factory 跑到第 3 步时读本文件 → 对照页面类型套用 → 不确定的点再
> `search.py` 取最新原文 → 落到 `src/seo.ts` / `seoLandingPages.json` /
> `p1SeoCollections.json` / `public/llms.txt` / `robots.txt` / 各页面组件。

---

## 0. 核心判断：SEO 与 GEO 不是两件事

- 传统排名仍是 AI 引用的基础：在自然结果排前列能提高被 ChatGPT 等引用的概率，
  但"进前三"对 AI 搜索不再像传统那样关键。（来源：Semrush
  https://www.semrush.com/blog/ai-search-seo-traffic-study/）
- GEO ⊃ AEO：AEO 优化"被 AI 答案引用"，GEO 还覆盖整个生成式平台生态。先做扎实的
  技术+内容 SEO，再叠加 AEO 专项。（来源：Ahrefs AEO Course
  https://ahrefs.com/academy/answer-engine-optimization）
- AI 来源访客价值更高：来自 AI 搜索的访客约为传统自然访客的 4.4x。（来源：Semrush
  https://www.semrush.com/blog/lower-funnel-marketing/）

## 1. 技术 AEO（建站硬工件，site-factory 必做）

- **robots.txt 放行 LLM 爬虫**：GPTBot、Google-Extended、ClaudeBot、PerplexityBot、
  CCBot——否则产品页不进 AI 索引。（来源：Ahrefs "Technical SEO for AI: Robots.txt,
  GPTBot & llms.txt" https://ahrefs.com/academy/answer-engine-optimization；
  Klaviyo https://academy.klaviyo.com/.../optimize-your-website-for-agentic-shopping）
- **`public/llms.txt`**：列品牌实体、产品类目、最佳引用页、政策/联系页、简短事实型
  产品描述，供答案引擎读取。（来源：Ahrefs 同上）
- **页面快、可扫读、可爬**：clear/scannable、load fast；结构化数据是 AI 读取产品
  细节的"标签"。（来源：Klaviyo agentic-shopping）
- 站点架构 + canonical + meta robots 控制收录面。（来源：Daydream
  https://www.withdaydream.com/library/insights/search-engines-meta-tags）

## 2. 结构化数据 / Schema（按页面类型，src/seo.ts 落 JSON-LD）

实现 Google 富结果所需类型；AI Overviews 也靠它理解内容。（来源：Semrush
https://www.semrush.com/blog/how-to-rank-in-ai-overviews/ ；Google Search Central
结构化数据文档 developers.google.com/search/docs/appearance/structured-data）

| 页面类型 | JSON-LD | 出处 |
|---|---|---|
| 首页 | Organization, WebSite | Google Search Central |
| 集合/列表 | CollectionPage, ItemList, BreadcrumbList | Daydream / Google |
| PDP | **Product + Offer + AggregateRating + Review** | Klaviyo reviews / Google |
| 内容/指南 | Article, FAQPage, HowTo（仅当真有步骤） | Semrush sitelinks / Google |
| B2B 服务 | Service, Organization, ContactPoint | Google |

产品富数据必须含：name / category / description / **price / reviews / shipping /
return policy**——这正是 AI 购物者决策最看重的信息。（来源：Klaviyo agentic-shopping）

## 3. 内容结构（让 AI 想引用）—— 每页 6 段 answer-ready

- 结构化成清晰 Q&A、简洁摘要、直接给答案，便于片段抽取；别把答案埋起来。（来源：
  Daydream https://www.withdaydream.com/library/insights/b2b-marketing-content ；
  Semrush https://www.semrush.com/blog/brand-visibility/）
- 加**引用、统计数据、专家原话**显著提升被生成式引擎引用的概率（Princeton GEO 实证
  约 +30–40%）。（来源：Princeton GEO 论文 https://arxiv.org/abs/2311.09735）
- 用客户真实语言写"问题→解决方案"，针对**对话式查询**而非关键词堆砌。（来源：
  Klaviyo agentic-shopping）
- **内容新鲜度**：AI 搜索偏好近期内容，常青主题也要定期更新。（来源：Semrush
  https://www.semrush.com/blog/ai-search-optimization/）

每个核心页固定 6 段：What it is / Who it's for / How to choose / How to use /
What to compare / FAQ —— FAQ 段同时输出 FAQPage schema。

## 4. 品牌被引用（off-page，3 层）

LLM 倾向引用它已经信任的站点；让品牌/产品出现在那些站点上是被 AI 提及最有效的方式。
（来源：Semrush https://www.semrush.com/blog/ai-mentions/）
- 与评测站/联盟站合作，进入 AI 常引的 listicle。（来源：Semrush lower-funnel）
- Ahrefs 把"被 AI 引用"拆成 3 层 brand-mention 策略。（来源：Ahrefs AEO Course
  lesson 3-2 https://ahrefs.com/academy/answer-engine-optimization）
- 站内能做的：可被引用的事实型内容 + 数据 + 清晰实体；站外是持续工程，列入运营。

## 5. 评价 / UGC → rich snippets（SEO+GEO 双吃，建到 PDP）

- 评价提供 keyword-rich 内容、内链网络、内容新鲜度、信誉信号；负评不伤 SEO。（来源：
  Klaviyo https://help.klaviyo.com/.../how-to-improve-seo-with-klaviyo-reviews）
- **AggregateRating/Review rich snippets** → SERP 星级 + AI 引用；独立 `/all-reviews`
  聚合页供爬取。（来源：Klaviyo rich-snippets / reviews-SEO）
- AI 购物系统大量分析评价 + 详细描述 + 类目标签来做推荐。（来源：Klaviyo
  agentic-shopping）

## 6. 度量（映射到你的后端：Umami + Metabase + GA4 思路）

- 追踪 AI 来源流量（GA4 / Web Analytics 里识别 ChatGPT 等 referrer）。（来源：Ahrefs
  "How to Track AI Traffic in GA4" lesson 4-1）→ 你的实现：Umami 自定义事件 + Metabase
  仪表盘按 referrer 分流。
- 月度自测可见性：incognito 在 ChatGPT/Gemini/Claude 用买家口吻提问，记录品牌是否出现、
  AI 答错/缺失什么，反向补站内内容。（来源：Klaviyo agentic-shopping）→ 列入第 5 步 QA。

## 7. B2C / B2B 分流（由 siteType 驱动）

- **B2C**：转化向文案 + Product/Offer/AggregateRating + 评价/UGC + 弃购/复购钩子。
- **B2B**：Service/ContactPoint schema、买家 persona、MOQ/交期/样品/合规、lead form；
  内容偏"用 Q&A + schema + 简洁摘要做 AI 可发现的解决方案页"。（来源：Daydream
  https://www.withdaydream.com/library/insights/b2b-marketing-content）

## 8. site-factory 第 3 步落地映射

| 方法论 | 落到文件/组件 | 执行 skill |
|---|---|---|
| §1 技术 AEO | `public/robots.txt` `public/llms.txt` | ai-seo + 本库 |
| §2 Schema | `src/seo.ts`（JSON-LD by route） | schema-markup + 本库 |
| §3 内容 6 段 | 各页组件 + `seoLandingPages.json` | copywriting + seo-content-writer |
| §3 长尾簇 | `seoLandingPages.json` `p1SeoCollections.json` | programmatic-seo + internal-linking |
| §4 品牌引用 | RUN_REPORT 的 off-page 待办清单 | （运营，非建站期） |
| §5 评价 | PDP 评价模块 + `/all-reviews` + Review JSON-LD | schema-markup + Directus |
| §6 度量 | Umami 事件 + Metabase 仪表盘 | （自有后端） |
