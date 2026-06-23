---
title: "contentRating"
source_url: https://schema.org/contentRating
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# contentRating

# contentRating

A Schema.org Property

- Canonical URL: https://schema.org/contentRating
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+contentRating)

Official rating of a piece of content—for example, 'MPAA PG-13'.

### Used on these types


### Examples

[Example 1](#eg-0020)

Copied

Example notes or example HTML without markup.

<div> Resistance 3: Fall of Man by Sony Platform: Playstation 3 Rated: Mature <img alt="Fall of Man cover art" src="videogame.jpg" /> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CreativeWork"> <img itemprop="image" alt="Fall of Man cover art" src="videogame.jpg" /> <span itemprop="name">Resistance 3: Fall of Man</span> by <span itemprop="author">Sony</span>, Platform: Playstation 3 Rated:<span itemprop="contentRating">Mature</span> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="CreativeWork"> <img property="image" alt="Fall of Man cover art" src="videogame.jpg" /> <span property="name">Resistance 3: Fall of Man</span> by <span property="author">Sony</span>, Platform: Playstation 3 Rated:<span property="contentRating">Mature</span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "CreativeWork", "author": "Sony", "contentRating": "Mature", "image": "videogame.jpg", "name": "Resistance 3: Fall of Man" } </script>

Structured representation of the JSON-LD example.
