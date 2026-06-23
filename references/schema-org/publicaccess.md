---
title: "publicAccess"
source_url: https://schema.org/publicAccess
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# publicAccess

# publicAccess

A Schema.org Property

- Canonical URL: https://schema.org/publicAccess
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+publicAccess)

A flag to signal that the

[Place](/Place)is open to public visitors. If this property is omitted there is no assumed default boolean value.### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0435)

Copied

Example notes or example HTML without markup.

<h1>Leaning Tower of Pisa</h1> <div>It is a twelfth-thirteenth century Romanesque tower started building by Bonanno Pisano.</div> <div>Public access: yes</div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/TouristAttraction"> <h1><span itemprop="name">Leaning Tower of Pisa</span></h1> <div> <span itemprop="description">It is a twelfth-thirteenth century Romanesque tower started building by Bonanno Pisano.</span> </div> <div> <meta itemprop="publicAccess" content="true"/>Public access: yes </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="TouristAttraction"> <h1><span property="name">Leaning Tower of Pisa</span></h1> <div> <span property="description">It is a twelfth-thirteenth century Romanesque tower started building by Bonanno Pisano.</span> </div> <div> <meta property="publicAccess" content="true"/>Public access: yes </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "TouristAttraction", "name": "Leaning Tower of Pisa", "publicAccess": true, "description": "It is a twelfth-thirteenth century Romanesque tower started building by Bonanno Pisano." } </script>

Structured representation of the JSON-LD example.
