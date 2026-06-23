---
title: "locationCreated"
source_url: https://schema.org/locationCreated
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# locationCreated

# locationCreated

A Schema.org Property

- Canonical URL: https://schema.org/locationCreated
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+locationCreated)

The location where the CreativeWork was created, which may not be the same as the location depicted in the CreativeWork.

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0340)

Copied

Example notes or example HTML without markup.

<div> The Church at Auvers by Vincent van Gogh depicts a church in Auvers-sur-Oise, but was created in Saint-Rémy-de-Provence. </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Painting"> <img itemprop="image" src="https://upload.wikimedia.org/wikipedia/commons/a/ad/Vincent_van_Gogh_-_The_Church_in_Auvers-sur-Oise%2C_View_from_the_Chevet_-_Google_Art_Project.jpg" /> <meta itemprop="sameAs" content="https://en.wikipedia.org/wiki/The_Church_at_Auvers" /> <span itemprop="name">The Church at Auvers</span> by <div itemprop="creator" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Vincent van Gogh</span> </div>, depicts a church in <div itemprop="contentLocation" itemscope itemtype="https://schema.org/AdministrativeArea"> <span itemprop="name">Auvers-sur-Oise</span>, </div> but was created in <div itemprop="locationCreated" itemscope itemtype="https://schema.org/AdministrativeArea"> <span itemprop="name">Saint-Rémy-de-Provence</span>. </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Painting"> <img property="image" src="https://upload.wikimedia.org/wikipedia/commons/a/ad/Vincent_van_Gogh_-_The_Church_in_Auvers-sur-Oise%2C_View_from_the_Chevet_-_Google_Art_Project.jpg" /> <meta property="sameAs" content="https://en.wikipedia.org/wiki/The_Church_at_Auvers" /> <span property="name">The Church at Auvers</span> by <div property="creator" typeof="Person"> <span property="name">Vincent van Gogh</span> </div>, depicts a church in <div property="contentLocation" typeof="AdministrativeArea"> <span property="name">Auvers-sur-Oise</span>, </div> but was created in <div property="locationCreated" typeof="AdministrativeArea"> <span property="name">Saint-Rémy-de-Provence</span>. </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Painting", "name": "The Church at Auvers", "image": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Vincent_van_Gogh_-_The_Church_in_Auvers-sur-Oise%2C_View_from_the_Chevet_-_Google_Art_Project.jpg", "sameAs": "https://en.wikipedia.org/wiki/The_Church_at_Auvers", "creator": { "@type": "Person", "name": "Vincent van Gogh" }, "contentLocation": { "@type": "AdministrativeArea", "name": "Auvers-sur-Oise" }, "locationCreated": { "@type": "AdministrativeArea", "name": "Saint-Rémy-de-Provence" } } </script>

Structured representation of the JSON-LD example.
