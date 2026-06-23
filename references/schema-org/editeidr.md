---
title: "editEIDR"
source_url: https://schema.org/editEIDR
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# editEIDR

# editEIDR

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/editEIDR
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+editEIDR)

An


For example, the motion picture known as "Ghostbusters" whose


Since schema.org types like

[EIDR](https://eidr.org/)(Entertainment Identifier Registry)[identifier](/identifier)representing a specific edit / edition for a work of film or television.For example, the motion picture known as "Ghostbusters" whose

[titleEIDR](/titleEIDR)is "10.5240/7EC7-228A-510A-053E-CBB8-J" has several edits, e.g. "10.5240/1F2A-E1C5-680A-14C6-E76B-I" and "10.5240/8A35-3BEE-6497-5D12-9E4F-3".Since schema.org types like

[Movie](/Movie)and[TVEpisode](/TVEpisode)can be used for both works and their multiple expressions, it is possible to use[titleEIDR](/titleEIDR)alone (for a general description), or alongside[editEIDR](/editEIDR)for a more edit-specific description.### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2469](https://github.com/schemaorg/schemaorg/issues/2469)

### Examples

[Example 1](#eg-0459)

Copied

Example notes or example HTML without markup.

<!-- Using editEIDR and titleEIDR identifiers for generic titles and specific expressions of a film or TV work -->

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Movie", "name": "The Hitchhiker's Guide to the Galaxy", "disambiguatingDescription": "2005 British-American comic science fiction film directed by Garth Jennings", "sameAs": "https://www.wikidata.org/wiki/Q836821", "titleEIDR": "10.5240/B752-5B47-DBBE-E5D4-5A3F-N", "workExample": [ { "@type": "Movie", "editEIDR": "10.5240/0196-4177-FF62-A346-D0F6-Z", "disambiguatingDescription": "VUDU version" }, { "@type": "Movie", "editEIDR": "10.5240/043D-15C4-838D-80F4-E96A-G", "disambiguatingDescription": "Censored for India" }, { "@type": "Movie", "editEIDR": "10.5240/7BAD-7B81-396E-27EF-360F-N", "disambiguatingDescription": "Theatrical" }, { "@type": "Movie", "editEIDR": "0.5240/1DC4-B3E4-ECEB-7197-BF18-B", "disambiguatingDescription": "Broadcast" } ], "isBasedOn": { "@type": "Book", "name": "The Hitchhiker's Guide to the Galaxy", "isbn": "0-330-25864-8", "sameAs": "https://www.wikidata.org/wiki/Q3107329", "author": { "@type": "Person", "name": "Douglas Adams", "sameAs": "https://www.wikidata.org/wiki/Q42" } } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0460)

Copied

Example notes or example HTML without markup.

<!-- Using editEIDR and titleEIDR identifiers for a specific edition of a movie or TV work. An exampleOfWork described elsewhere -->

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@type": "Movie", "name": "The Hitchhiker's Guide to the Galaxy", "titleEIDR": "10.5240/B752-5B47-DBBE-E5D4-5A3F-N", "editEIDR": "10.5240/0196-4177-FF62-A346-D0F6-Z", "disambiguatingDescription": "VUDU version", "exampleOfWork": { "@type": "Movie", "sameAs": "https://www.wikidata.org/wiki/Q836821" } } </script>

Structured representation of the JSON-LD example.
