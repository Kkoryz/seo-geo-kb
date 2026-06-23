---
title: "sameAs"
source_url: https://schema.org/sameAs
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# sameAs

# sameAs

A Schema.org Property

- Canonical URL: https://schema.org/sameAs
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+sameAs)

URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0458)

Copied

Example notes or example HTML without markup.

<!-- Utilising Wikidata as a source of URIs for entities in a sameAs relationship -->

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Movie", "name": "The Hitchhiker's Guide to the Galaxy", "disambiguatingDescription": "2005 British-American comic science fiction film directed by Garth Jennings", "sameAs": "https://www.wikidata.org/wiki/Q836821", "titleEIDR": "10.5240/B752-5B47-DBBE-E5D4-5A3F-N", "isBasedOn": { "@type": "Book", "name": "The Hitchhiker's Guide to the Galaxy", "isbn": "0-330-25864-8", "sameAs": "https://www.wikidata.org/wiki/Q3107329", "author": { "@type": "Person", "name": "Douglas Adams", "sameAs": "https://www.wikidata.org/wiki/Q42" } } } </script>

Structured representation of the JSON-LD example.
