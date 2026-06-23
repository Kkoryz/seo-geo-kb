---
title: "cssSelector"
source_url: https://schema.org/cssSelector
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# cssSelector

# cssSelector

A Schema.org Property

- Canonical URL: https://schema.org/cssSelector
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+cssSelector)

A CSS selector, e.g. of a

[SpeakableSpecification](/SpeakableSpecification)or[WebPageElement](/WebPageElement). In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1389](https://github.com/schemaorg/schemaorg/issues/1389)

### Examples

[Example 1](#eg-0237)

Copied

Example notes or example HTML without markup.

An example of 'speakable' markup (JSON-LD only, initially).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "WebPage", "name": "Jane Doe's homepage", "speakable": { "@type": "SpeakableSpecification", "cssSelector": ["headline", "summary"] }, "url": "http://www.janedoe.com" }

Structured representation of the JSON-LD example.

[Example 2](#eg-0238)

Copied

Example notes or example HTML without markup.

An example of speakable markup in Microdata in HTML head section.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!DOCTYPE html> <html> <head rel="home" href="/" itemid="" itemscope itemtype="https://schema.org/SpeakableSpecification"> <title>Example showing complex structures in HTML head</title> <meta itemprop="cssSelector" content=".title" /> <meta itemprop="xpath" content="/html/body/h3" /> </head> <body> <h1 class="title">Complex Microdata in HTML head</h1> <p>...</p> </body> </html>
