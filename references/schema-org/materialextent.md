---
title: "materialExtent"
source_url: https://schema.org/materialExtent
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# materialExtent

# materialExtent

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/materialExtent
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+materialExtent)

The quantity of the materials being described or an expression of the physical space they occupy.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1759](https://github.com/schemaorg/schemaorg/issues/1759)

### Examples

[Example 1](#eg-0257)

Copied

Example notes or example HTML without markup.

<div> Name: Assorted collection of items<br/> Extent: 285 A boxes, 8 OS boxes (plus 45 T boxes, 50 A boxes, 13 OS boxes / items uncatalogued)<br/> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CreativeWork"> <link itemprop="additionalType" href="https://schema.org/ArchiveComponent"/> Name: <span itemprop="name">Assorted collection of items</span><br/> Extent: <span itemprop="materialExtent">285 A boxes, 8 OS boxes (plus 45 T boxes, 50 A boxes, 13 OS boxes / items uncatalogued)</span><br/> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": ["CreativeWork","ArchiveComponent"], "name": "Assorted collection of items", "materialExtent": "285 A boxes, 8 OS boxes (plus 45 T boxes, 50 A boxes, 13 OS boxes / items uncatalogued)" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0258)

Copied

Example notes or example HTML without markup.

<div> Name: Assorted collection of items<br/> Extent: 1 folder containing 5 design drawings<br/> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CreativeWork"> <link itemprop="additionalType" href="https://schema.org/ArchiveComponent"/> Name: <span itemprop="name">Assorted collection of items</span><br/> Extent: <div> <div itemprop="materialExtent" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="value">1</span> <span itemprop="unitText">folder</span> </div> containing <div itemprop="materialExtent" itemscope itemtype="https://schema.org/QuantitativeValue"> <span itemprop="value">5</span> <span itemprop="unitText">design drawings</span> </div> </div><br/> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": ["CreativeWork","ArchiveComponent"], "materialExtent": [ { "@type": "QuantitativeValue", "unitText": "folder", "value": "1" }, { "@type": "QuantitativeValue", "unitText": "design drawings", "value": "5" } ] } </script>

Structured representation of the JSON-LD example.
