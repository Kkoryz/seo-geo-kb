---
title: "holdingArchive"
source_url: https://schema.org/holdingArchive
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# holdingArchive

# holdingArchive

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/holdingArchive
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+holdingArchive)

[ArchiveOrganization](/ArchiveOrganization)that holds, keeps or maintains the

[ArchiveComponent](/ArchiveComponent).

Inverse-property:
[archiveHeld](/archiveHeld)

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1758](https://github.com/schemaorg/schemaorg/issues/1758)

### Examples

[Example 1](#eg-0255)

Copied

Example notes or example HTML without markup.

<div> <h1>Ronnie Barker Collection</h1> <span class="label">Material held at</span> <span class="val"><a href="https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76">V&A Theatre and Performance Collections</a></span><br/> <span class="label">Reference</span> <span class="val">GB 71 THM/407/8<span><br/> <span class="label">Dates of Creation</span> <span class="val">1929-2005</span><br/> <span class="label">Name of Creator</span> <span class="val">Ronnie Barker</span><br/> <span class="label">Language of Material</span> <span class="val">English</span><br/> <span class="label">Direct Link</span> <span class="val"><a href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407">https://archiveshub.jisc.ac.uk/data/gb71-thm/407</a></span><br/> <span class="label">Description</span> <span class="val">The collection consists of memorabilia material collected by Ronnie Barker to document his career. Materials include scrapbooks compiled by Ronnie Barker with press cuttings, reviews, memorabilia and photographs of his theatre, television and film work, photographs, manuscript material, scripts, correspondence, certificates and awards, press and marketing materials, audio recordings, audio visual recordings and material relating to special events and honours in his career.</span><br/> <span class="label">Conditions Governing Access</span> <span class="val">This archive collection is available for consultation in the V&A Blythe House Archive and Library Study Room by appointment only. Full details of access arrangements may be found here: http://www.vam.ac.uk/content/articles/a/archives/. Access to some of the material may be restricted. These are noted in the catalogue where relevant.</span><br/> <span class="label">Contains</span> <span class="val"><a href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8">THM/407/8 - Audio Recordings</a></span><br/> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Collection"> <link itemprop="additionalType" href="https://schema.org/ArchiveComponent"/> <h1 itemprop="name">Ronnie Barker Collection</h1> <span class="label">Material held at</span> <span class="val"><a itemprop="holdingArchive" href="https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76">V&A Theatre and Performance Collections</a></span><br/> <span class="label">Reference</span> <span class="val" itemprop="identifier">GB 71 THM/407/8</span><br/> <span class="label">Dates of Creation</span> <span class="val" itemprop="temporalCoverage">1929-2005</span><br/> <span class="label">Name of Creator</span> <span class="val" itemprop="creator">Ronnie Barker</span><br/> <span class="label">Language of Material</span> <span class="val" itemprop="inLanguage" content="EN">English</span><br/> <span class="label">Direct Link</span> <span class="val"><a itemprop="url" href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407">https://archiveshub.jisc.ac.uk/data/gb71-thm/407</a></span><br/> <span class="label">Description</span> <span class="val" itemprop="description">The collection consists of memorabilia material collected by Ronnie Barker to document his career. Materials include scrapbooks compiled by Ronnie Barker with press cuttings, reviews, memorabilia and photographs of his theatre, television and film work, photographs, manuscript material, scripts, correspondence, certificates and awards, press and marketing materials, audio recordings, audio visual recordings and material relating to special events and honours in his career.</span><br/> <span class="label">Contains</span> <span class="val"><a itemprop="hasPart" href="https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8">THM/407/8 - Audio Recordings</a></span><br/> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<!-- A collection of items held in an archive --> <script type="application/ld+json"> { "@context": "https://schema.org", "@id": "https://archiveshub.jisc.ac.uk/data/gb71-thm/407", "@type": ["Collection","ArchiveComponent"], "identifier": "GB 71 THM/407/8", "name": "Ronnie Barker Collection", "about": ["Comedy","Ronnie Barker"], "creator": { "@type": "Person", "name": "Ronnie Barker", "sameAs": "http://viaf.org/viaf/2676198" }, "description": "The collection consists of memorabilia material collected by Ronnie Barker to document his career. Materials include scrapbooks compiled by Ronnie Barker with press cuttings, reviews, memorabilia and photographs of his theatre, television and film work, photographs, manuscript material, scripts, correspondence, certificates and awards, press and marketing materials, audio recordings, audio visual recordings and material relating to special events and honours in his career.", "inLanguage": "EN", "temporalCoverage": "1929-2005", "itemLocation": "https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76", "holdingArchive": "https://archiveshub.jisc.ac.uk/search/locations/eae30daa-1bf9-33d9-bf1c-7aeb220d2e76", "hasPart": "https://archiveshub.jisc.ac.uk/data/gb71-thm/407/thm/407/8" } </script>

Structured representation of the JSON-LD example.
