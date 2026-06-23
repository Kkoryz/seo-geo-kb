---
title: "hasMap"
source_url: https://schema.org/hasMap
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# hasMap

# hasMap

A Schema.org Property

- Canonical URL: https://schema.org/hasMap
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+hasMap)

A URL to a map of the place.

### Used on these types


| Supersedes |
|---|
```
``` |

### Examples

[Example 1](#eg-0362)

Copied

Example notes or example HTML without markup.

<h1>ACME Hotel Innsbruck</h1> <span>A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> <a href="https://www.google.com/maps?ie=UTF8&hq&ll=47.1234,11.1234&z=13">Click here for a map.</a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> <a itemprop="hasMap" href="https://www.google.com/maps?ie=UTF8&hq&ll=47.1234,11.1234&z=13">Click here for a map.</a> </div>
