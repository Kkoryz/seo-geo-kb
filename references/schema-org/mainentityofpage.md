---
title: "mainEntityOfPage"
source_url: https://schema.org/mainEntityOfPage
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# mainEntityOfPage

# mainEntityOfPage

A Schema.org Property

- Canonical URL: https://schema.org/mainEntityOfPage
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+mainEntityOfPage)

Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See

[background notes](/docs/datamodel.html#mainEntityBackground)for details.Inverse-property:
[mainEntity](/mainEntity)

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0383)

Copied

Example notes or example HTML without markup.

<div> <h1>Cath's Cafe</h1> <p>Open: Daily from 11:00am till 8pm</p> <p>Phone: 555-0100-3344</p> <p>View <a href="/menu">our menu</a>.</p> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Restaurant" itemid="#thecafe"> <a itemprop="mainEntityOfPage" href="http://cathscafe.example.com/"><h1 itemprop="name">Cath's Cafe</h1></a> <p>Open: <span itemprop="openingHours" content="Mo,Tu,We,Th,Fr,Sa,Su 11:00-20:00">Daily from 11:00am till 8pm</span></p> <p>Phone: <span itemprop="telephone" content="+155501003344">555-0100-3344</span></p> <p>View <a itemprop="hasMenu" href="/menu">our menu</a>.</p> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Restaurant" resource="#thecafe"> <a property="mainEntityOfPage" href="http://cathscafe.example.com/"><h1 property="name">Cath's Cafe</h1></a> <p>Open: <span property="openingHours" content="Mo,Tu,We,Th,Fr,Sa,Su 11:00-20:00">Daily from 11:00am till 8pm</span></p> <p>Phone: <span property="telephone" content="+155501003344">555-0100-3344</span></p> <p>View <a property="hasMenu" href="/menu">our menu</a>.</p> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Restaurant", "mainEntityOfPage": "http://cathscafe.example.com/", "name": "Cath's Cafe", "openingHours": "Mo,Tu,We,Th,Fr,Sa,Su 11:00-20:00", "telephone": "+155501003344", "hasMenu": "/menu" } </script>

Structured representation of the JSON-LD example.
