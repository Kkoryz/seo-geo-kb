---
title: "genre"
source_url: https://schema.org/genre
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# genre

# genre

A Schema.org Property

- Canonical URL: https://schema.org/genre
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+genre)

Genre of the creative work, broadcast channel or group.

### Values expected to be one of these types


### Used on these types


#### Sub-properties

### Examples

[Example 1](#eg-0003)

Copied

Example notes or example HTML without markup.

<h1>The Madonna with the Long Neck</h1> Late Renaissance painting by Parmigianino

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Painting"> <h1><span itemprop="name">The Madonna with the Long Neck</span></h1> <meta itemprop="genre" content="http://vocab.getty.edu/aat/300021143"/>Late Renaissance painting by <span itemprop="creator">Parmigianino</span>. </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Painting"> <h1><span property="name">The Madonna with the Long Neck</span></h1> <span property="genre" content="http://vocab.getty.edu/aat/300021143">Late Renaissance</span> painting by <span property="creator">Parmigianino</span>. </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Painting", "name": "The Madonna with the Long Neck", "genre": "http://vocab.getty.edu/aat/300021143" } </script>

Structured representation of the JSON-LD example.
