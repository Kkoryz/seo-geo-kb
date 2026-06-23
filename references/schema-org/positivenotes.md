---
title: "positiveNotes"
source_url: https://schema.org/positiveNotes
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# positiveNotes

# positiveNotes

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/positiveNotes
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+positiveNotes)

Provides positive considerations regarding something, for example product highlights or (alongside


In the case of a


The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).

[negativeNotes](/negativeNotes)) pro/con lists for reviews.In the case of a

[Review](/Review), the property describes the[itemReviewed](/itemReviewed)from the perspective of the review; in the case of a[Product](/Product), the product itself is being described.The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).

### Values expected to be one of these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2832](https://github.com/schemaorg/schemaorg/issues/2832)

### Examples

[Example 1](#eg-0468)

Copied

Example notes or example HTML without markup.

See JSON-LD example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Review", "name": "Megaphone 11 review", "description": "Megaphone 11 is the strongest phone in the line...", "positiveNotes": { "@type": "ItemList", "itemListElement": [ { "@type": "ListItem", "position": 1, "name": "Tougher and water resistant design." }, { "@type": "ListItem", "position": 2, "name": "Cheery bright colours and solid feel." }, { "@type": "ListItem", "position": 3, "name": "Excellent amplification." } ] }, "negativeNotes": { "@type": "ItemList", "itemListElement": [ { "@type": "ListItem", "position": 1, "name": "More expensive than its predecessor." }, { "@type": "ListItem", "position": 2, "name": "Quite heavy material." } ] } } </script>

Structured representation of the JSON-LD example.
