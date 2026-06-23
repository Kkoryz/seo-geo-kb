---
title: "isBasedOn"
source_url: https://schema.org/isBasedOn
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# isBasedOn

# isBasedOn

A Schema.org Property

- Canonical URL: https://schema.org/isBasedOn
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+isBasedOn)

A resource from which this work is derived or from which it is a modification or adaptation.

### Values expected to be one of these types


### Used on these types


| Supersedes |
|---|
```
``` |

### Examples

[Example 1](#eg-0381)

Copied

Example notes or example HTML without markup.

<dl> <dt>Derivative work</dt> <dd><p>In copyright law, a derivative work is an expressive creation that includes major elements of a previously created original work. An example of a derivative work is L.H.O.O.Q, or Mona Lisa With a Moustache, by Marcel Duchamp.</p> <p>Note: this definition is based on the wikipedia article on Derivative Work</p> </dd> </dl>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<dl itemscope itemtype="https://schema.org/CreativeWork"> <dt itemprop="name">Derivative work</dt> <dd><p itemprop="text">In copyright law, a derivative work is an expressive creation that includes major elements of a previously created original work. An example of a derivative work is L.H.O.O.Q, or Mona Lisa With a Moustache, by Marcel Duchamp.</p> <p itemprop="isBasedOn" itemscope itemtype="https://schema.org/CreativeWork"> Note: this definition is based on the <span itemprop="publisher">wikipedia</span> article on <span itemprop="name">Derivative Work</span> <link itemprop="url" href="https://en.wikipedia.org/wiki/Derivative_work" /> </p> </dd> </dl>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<dl vocab="https://schema.org/" typeof="CreativeWork"> <dt property="name">Derivative work</dt> <dd><p property="text">In copyright law, a derivative work is an expressive creation that includes major elements of a previously created original work. An example of a derivative work is L.H.O.O.Q, or Mona Lisa With a Moustache, by Marcel Duchamp.</p> <p property="isBasedOn" typeof="CreativeWork"> Note: this definition is based on the <span property="publisher">wikipedia</span> article on <span property="name">Derivative Work</span> <link property="url" href="https://en.wikipedia.org/wiki/Derivative_work" /> </p> </dd> </dl>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "CreativeWork", "name": "Derivative Work", "text": "In copyright law, a derivative work is an expressive creation that includes major elements of a previously created original work. An example of a derivative work is L.H.O.O.Q, or Mona Lisa With a Moustache, by Marcel Duchamp.", "isBasedOn": { "@type": "CreativeWork", "name": "Derivative Work", "publisher": "wikipedia", "url": "https://en.wikipedia.org/wiki/Derivative_work" } } </script>

Structured representation of the JSON-LD example.
