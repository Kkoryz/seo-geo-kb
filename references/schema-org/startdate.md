---
title: "startDate"
source_url: https://schema.org/startDate
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# startDate

# startDate

A Schema.org Property

- Canonical URL: https://schema.org/startDate
- Equivalent Property: cmns-dt:hasStartDate
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+startDate)

The start date and time of the item (in

[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2486](https://github.com/schemaorg/schemaorg/issues/2486)

### Examples

[Example 1](#eg-0461)

Copied

Example notes or example HTML without markup.

<a href="nba-miami-philidelphia-game3.html"> NBA Eastern Conference First Round Playoff Tickets: Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1) </a> Thu, 04/21/16 8:00 p.m. <a href="wells-fargo-center.html"> Wells Fargo Center </a> Philadelphia, PA Priced from: $35 1938 tickets left

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Event"> <a itemprop="url" href="nba-miami-philidelphia-game3.html"> NBA Eastern Conference First Round Playoff Tickets: <span itemprop="name"> Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1) </span> </a> <meta itemprop="startDate" content="2016-04-21T20:00"> Thu, 04/21/16 8:00 p.m. <div itemprop="location" itemscope itemtype="https://schema.org/Place"> <a itemprop="url" href="wells-fargo-center.html"> Wells Fargo Center </a> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="addressLocality">Philadelphia</span>, <span itemprop="addressRegion">PA</span> </div> </div> <div itemprop="offers" itemscope itemtype="https://schema.org/AggregateOffer"> <meta itemprop="priceCurrency" content="USD" /> Priced from: <span itemprop="lowPrice" content="35">$35</span> <span itemprop="offerCount">1938</span> tickets left </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Event"> <a property="url" href="nba-miami-philidelphia-game3.html"> NBA Eastern Conference First Round Playoff Tickets: <span property="name"> Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1) </span> </a> <meta property="startDate" content="2016-04-21T20:00"> Thu, 04/21/16 8:00 p.m. <div property="location" typeof="Place"> <a property="url" href="wells-fargo-center.html"> Wells Fargo Center </a> <div property="address" typeof="PostalAddress"> <span property="addressLocality">Philadelphia</span>, <span property="addressRegion">PA</span> </div> </div> <div property="offers" typeof="AggregateOffer"> <meta property="priceCurrency" content="USD" /> Priced from: <span property="lowPrice" content="35">$35</span> <span property="offerCount">1938</span> tickets left </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "name": "Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1)", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Philadelphia", "addressRegion": "PA" }, "url": "wells-fargo-center.html" }, "offers": { "@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "35", "offerCount": "1938" }, "startDate": "2016-04-21T20:00", "url": "nba-miami-philidelphia-game3.html" } </script>

Structured representation of the JSON-LD example.
