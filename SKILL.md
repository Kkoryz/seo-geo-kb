---
name: seo-geo-kb
description: >
  SEO/GEO/AEO 知识库 + 执行参考。当用户提到 SEO、技术 SEO、on-page、结构化数据/
  schema/JSON-LD、rich snippets、sitemap/robots、内链、站点架构、关键词、电商商品页
  SEO、GEO(生成式引擎优化)、AEO(答案引擎优化)、LLMO、AI 搜索/AI Overviews、被
  ChatGPT/Gemini/Perplexity/Claude 引用、agentic shopping，或问"怎么让站点在
  搜索/AI 答案里被发现/被引用"时使用。内容抓自 Google Search Central + schema.org
  + Princeton GEO 论文 + Ahrefs/Semrush + Search Engine Journal + Scrunch/Daydream
  等一手源与方法论站点，既可语义检索，也可指导建站期的 SEO/GEO 基础设施落地。
---

# SEO / GEO 知识库

抓自权威一手源 + 头部方法论站点的 SEO/GEO/AEO 实践库。与 `klaviyo-marketing`
同构（同一套 scrape → BGE-M3 索引 → 语义检索管线，**共用 .venv**）。

## 内容来源

| 来源 | 内容 | 许可 |
|---|---|---|
| developers.google.com/search | 官方技术 SEO + 结构化数据文档 | open |
| schema.org/docs | 结构化数据词汇参考 | open |
| arXiv 2311.09735 | Princeton "GEO" 论文（GEO 概念学术起点） | open |
| ahrefs.com/blog · /academy | SEO 方法论 | robots 放行(商业 ToS 灰区) |
| semrush.com/blog | SEO/GEO 方法论 | robots 放行(商业 ToS 灰区) |
| searchenginejournal.com | SEO/GEO 新闻 + 指南 | open |
| scrunch.com/blog · withdaydream.com/library | AEO/GEO playbook | open |

> 仅供个人本地学习检索；保留 `source_url` 出处，限速抓取，不再发布。

### 更新内容（抓取 → 重建索引）
抓取用全局 python（轻依赖 `requests` + `trafilatura`）：
```
python scrape_seo_geo.py --list
python scrape_seo_geo.py --all                       # 全部源
python scrape_seo_geo.py --sources ahrefs-blog semrush-blog   # 单源
```
抓完后**重建语义索引**（复用 klaviyo-marketing 的 `.venv`，BGE-M3 已缓存）：
```bash
~/.codex/skills/klaviyo-marketing/.venv/Scripts/python.exe \
  ~/.codex/skills/seo-geo-kb/index_kb.py
```

## 用法一：知识库检索（首选语义搜索）

```bash
~/.codex/skills/klaviyo-marketing/.venv/Scripts/python.exe \
  ~/.codex/skills/seo-geo-kb/search.py "如何让产品页被 ChatGPT 引用" --json -k 8
```
返回 JSON：每条含 `score / title / category / path / source_url / text`。
1. 语义搜索拿 top 结果（首次约 10-15 秒加载模型）
2. 挑最相关 `path` 用 **Read** 读完整文档
3. 综合作答

**强制出处规则**：回答任何 SEO/GEO 结论时，**必须为每个要点标注来源**——格式 `（来源：<站点名> <source_url>）`，例如 `（来源：Ahrefs https://ahrefs.com/blog/...）`。不得在无出处的情况下断言 SEO/GEO 事实或操作步骤。无法在 references/ 找到依据时，明确说明"知识库未覆盖，以下为通用判断"。

不要凭记忆杜撰 SEO/GEO 操作——以 references/ 实际文档为准。

> 数据质量备注：`ahrefs-academy` 是视频课，正文在视频里，抓到的多为课程目录；做方法论时优先引用文本型源（semrush-blog / ahrefs-blog / daydream / search-engine-journal / google-search-central / geo-paper）。

## 用法二：执行参考（建站期 SEO/GEO 基础设施）

当用户要做 SEO/GEO 落地（meta、JSON-LD、内链簇、长尾页、llms.txt、AEO 答案块），
本库提供一手依据；与本地 SEO/GEO skill（`ai-seo` / `schema-markup` /
`programmatic-seo` / `on-page-seo-auditor` / `geo-content-optimizer` 等）配合：
skill 出方法与执行，本库出权威事实接地（Google 官方文档 / schema.org / GEO 论文）。

### GEO/AEO 速查（建站必做）
- robots.txt 放行 LLM 爬虫：GPTBot / Google-Extended / ClaudeBot / PerplexityBot
- 产品页结构化数据齐全：name/category/description/**price/reviews/shipping/returns**
- 为对话式查询写"问题→解决方案"答案块，用客户真实语言（非堆关键词）
- 评价 → AggregateRating/Review JSON-LD + 独立 /all-reviews 聚合页（rich snippets）
- 页面快、可扫读；高权威站点的外部提及

## 目录结构

```
SKILL.md            本文件
scrape_seo_geo.py   多站抓取(sitemap 递归展开 + trafilatura 抽取)
index_kb.py         建语义索引(BGE-M3 → LanceDB)  ← 用 klaviyo .venv 跑
search.py           语义搜索(向量召回 + reranker)  ← 用 klaviyo .venv 跑
.kb_index/          LanceDB 语义索引(table: seo_geo)
references/         抓取的 Markdown，按来源分类:
  google-search-central schema-org geo-paper
  ahrefs-blog ahrefs-academy semrush-blog
  search-engine-journal scrunch daydream
```
