---
title: "archiveHeld"
source_url: https://schema.org/archiveHeld
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# archiveHeld

# archiveHeld

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/archiveHeld
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+archiveHeld)

Collection,

[fonds](https://en.wikipedia.org/wiki/Fonds), or item held, kept or maintained by an[ArchiveOrganization](/ArchiveOrganization).Inverse-property:
[holdingArchive](/holdingArchive)

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1758](https://github.com/schemaorg/schemaorg/issues/1758)

### Examples

[Example 1](#eg-0254)

Copied

Example notes or example HTML without markup.

<!-- Page Address https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76 --> <div> <h1>V&A Theatre and Performance Collections</h1> <span class="label">Web</span> <span class="val"><a href="http://www.vam.ac.uk/content/articles/t/archives-theatre-performance/">V&A Theatre and Performance Collections</a></span><br/> <span class="label">Address</span> <span class="val">Blythe House23 Blythe Road, London W14 0QX, England</span><br/> <span class="label">Collection</span> <span class="val"><a href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407">Ronnie Barker Collection</a></span> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/ArchiveOrganization"> <h1 itemprop="name">V&A Theatre and Performance Collections</h1> <span class="label">Web</span> <span class="val"><a itemprop="url" href="http://www.vam.ac.uk/content/articles/t/archives-theatre-performance/">V&A Theatre and Performance Collections</a></span><br/> <span class="label">Address</span> <span class="val" itemprop="address">Blythe House23 Blythe Road, London W14 0QX, England</span><br/> <span class="label">Collection</span> <span class="val" itemprop="archiveHeld"><a href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407">Ronnie Barker Collection</a></span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@id": "https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76", "@type": "ArchiveOrganization", "name": "V&A Theatre and Performance Collections", "url": "http://www.vam.ac.uk/content/articles/t/archives-theatre-performance/", "archiveHeld": "https://archiveshub.jisc.ac.uk/data/gb71-thm/407", "address": "Blythe House23 Blythe Road, London W14 0QX, England" } </script>

Structured representation of the JSON-LD example.
