---
title: "disambiguatingDescription"
source_url: https://schema.org/disambiguatingDescription
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# disambiguatingDescription

# disambiguatingDescription

A Schema.org Property

- Canonical URL: https://schema.org/disambiguatingDescription
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+disambiguatingDescription)

A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0212)

Copied

Example notes or example HTML without markup.

George Bush, the 41st President of the United States is the father of George W. Bush, the 43rd President of the United States.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Person"> <span itemprop="name">George Bush</span>, the <span itemprop="disambiguatingDescription">41st President of the United States</span> is the father of <div itemprop="children" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">George W. Bush</span>, the <span itemprop="disambiguatingDescription">43rd President of the United States</span>. </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Person"> <span property="name">George Bush</span>, the <span property="disambiguatingDescription">41st President of the United States</span> is the father of <div property="children" typeof="Person"> <span property="name">George W. Bush</span>, the <span property="disambiguatingDescription">43rd President of the United States</span>. </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Person", "name": "George Bush", "disambiguatingDescription": "41st President of the United States", "children": { "@type": "Person", "name": "George W. Bush", "disambiguatingDescription": "43rd President of the United States" } } </script>

Structured representation of the JSON-LD example.
