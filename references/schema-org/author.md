---
title: "author"
source_url: https://schema.org/author
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# author

# author

A Schema.org Property

- Canonical URL: https://schema.org/author
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+author)

The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0330)

Copied

Example notes or example HTML without markup.

Book series example with nested author(JSON-LD only).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "BookSeries", "name": "The Hitchhiker's Guide to the Galaxy", "genre": "comedy science fiction", "startDate": "1979-10-12", "endDate": "1992-10-12", "abstract": "Earthman Arthur Dent is saved by his friend, Ford Prefect—an alien researcher for the titular Hitchhiker's Guide to the Galaxy, which provides info on every planet in the galaxy—from the Earth just before it is destroyed by the alien Vogons.", "author": { "@type": "Person", "givenName": "Douglas", "familyName": "Adams", "additionalName": "Noel", "birthDate": "1952-03-11", "birthPlace": { "@type": "Place", "address": "Cambridge, Cambridgeshire, England" }, "deathDate": "2001-05-11", "deathPlace": { "@type": "Place", "address": "Santa Barbara, California, United States" } } } </script>

Structured representation of the JSON-LD example.
