---
title: "spokenByCharacter"
source_url: https://schema.org/spokenByCharacter
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# spokenByCharacter

# spokenByCharacter

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/spokenByCharacter
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+spokenByCharacter)

The (e.g. fictional) character, Person or Organization to whom the quotation is attributed within the containing CreativeWork.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/271](https://github.com/schemaorg/schemaorg/issues/271)

### Examples

[Example 1](#eg-0304)

Copied

Example notes or example HTML without markup.

Example of a quote from fiction.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Quotation", "spokenByCharacter": { "@type": "Person", "name": "Princess Leia" }, "text": "Help me Obi Wan Kenobi, you're my only hope.", "isPartOf": { "@type": "Movie", "name": "Star Wars Episode IV: A New Hope" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0305)

Copied

Example notes or example HTML without markup.

Example of a quote from a real person.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Quotation", "creator": { "@type": "Person", "name": "Franklin Delano Roosevelt" }, "text": "The only thing we have to fear is fear itself." } </script>

Structured representation of the JSON-LD example.
