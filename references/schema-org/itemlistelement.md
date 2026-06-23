---
title: "itemListElement"
source_url: https://schema.org/itemListElement
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# itemListElement

# itemListElement

A Schema.org Property

- Canonical URL: https://schema.org/itemListElement
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+itemListElement)

For itemListElement values, you can use simple strings (e.g. "Peter", "Paul", "Mary"), existing entities, or use ListItem.


Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.


Note: The order of elements in your mark-up is not sufficient for indicating the order or elements. Use ListItem with a 'position' property in such cases.

Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.

Note: The order of elements in your mark-up is not sufficient for indicating the order or elements. Use ListItem with a 'position' property in such cases.

### Used on these types


### Examples

[Example 1](#eg-0377)

Copied

Example notes or example HTML without markup.

<ol> <li> <a href="https://example.com/dresses">Dresses</a> </li> <li> <a href="https://example.com/dresses/real">Real Dresses</a> </li> </ol>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<ol itemscope itemtype="https://schema.org/BreadcrumbList"> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"> <a itemprop="item" href="https://example.com/dresses"> <span itemprop="name">Dresses</span></a> <meta itemprop="position" content="1" /> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"> <a itemprop="item" href="https://example.com/dresses/real"> <span itemprop="name">Real Dresses</span></a> <meta itemprop="position" content="2" /> </li> </ol>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<ol vocab="https://schema.org/" typeof="BreadcrumbList"> <li property="itemListElement" typeof="ListItem"> <a property="item" typeof="WebPage" href="https://example.com/dresses"> <span property="name">Dresses</span></a> <meta property="position" content="1"> </li> <li property="itemListElement" typeof="ListItem"> <a property="item" typeof="WebPage" href="https://example.com/dresses/real"> <span property="name">Real Dresses</span></a> <meta property="position" content="2"> </li> </ol>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [ { "@type": "ListItem", "position": 1, "item": { "@id": "https://example.com/dresses", "name": "Dresses" } }, { "@type": "ListItem", "position": 2, "item": { "@id": "https://example.com/dresses/real", "name": "Real Dresses" } } ] } </script>

Structured representation of the JSON-LD example.
