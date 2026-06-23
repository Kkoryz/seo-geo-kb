---
title: "offers"
source_url: https://schema.org/offers
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# offers

# offers

A Schema.org Property

- Canonical URL: https://schema.org/offers
- Equivalent Property: fibo-fnd-pas-pas:isProductOf
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+offers)

An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use

[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse-property:
[itemOffered](/itemOffered)

### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2289](https://github.com/schemaorg/schemaorg/issues/2289)

### Examples

[Example 1](#eg-0011)

Copied

Example notes or example HTML without markup.

<img src="dell-30in-lcd.jpg" alt="A Dell UltraSharp monitor" /> Dell UltraSharp 30" LCD Monitor 87 out of 100 based on 24 user ratings $1250 to $1495 from 8 sellers Sellers: <a href="save-a-lot-monitors.com/dell-30.html"> Save A Lot Monitors - $1250</a> <a href="jondoe-gadgets.com/dell-30.html"> Jon Doe's Gadgets - $1350</a> ...

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="dell-30in-lcd.jpg" alt="A Dell UltraSharp monitor"/> <span itemprop="name">Dell UltraSharp 30" LCD Monitor</span> <div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating"> <span itemprop="ratingValue">87</span> out of <span itemprop="bestRating">100</span> based on <span itemprop="ratingCount">24</span> user ratings </div> <div itemprop="offers" itemscope itemtype="https://schema.org/AggregateOffer"> <meta itemprop="priceCurrency" content="USD" /> <span itemprop="lowPrice" content="1250">$1250</span> to <span itemprop="highPrice" content="1495">$1495</span> from <span itemprop="offerCount">8</span> sellers Sellers: <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <a itemprop="url" href="save-a-lot-monitors.com/dell-30.html"> Save A Lot Monitors - $1250</a> </div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <a itemprop="url" href="jondoe-gadgets.com/dell-30.html"> Jon Doe's Gadgets - $1350</a> </div> </div> ... </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Product"> <img property="image" src="dell-30in-lcd.jpg" alt="A Dell UltraSharp monitor"> <span property="name">Dell UltraSharp 30" LCD Monitor</span> <div property="aggregateRating" typeof="AggregateRating"> <span property="ratingValue">87</span> out of <span property="bestRating">100</span> based on <span property="ratingCount">24</span> user ratings </div> <div property="offers" typeof="AggregateOffer"> <meta property="priceCurrency" content="USD" /> <span property="lowPrice" content="1250">$1250</span> to <span property="highPrice" content="1495">$1495</span> from <span property="offerCount">8</span> sellers Sellers: <div property="offers" typeof="Offer"> <a property="url" href="save-a-lot-monitors.com/dell-30.html">Save A Lot Monitors - $1250</a> </div> <div property="offers" typeof="Offer"> <a property="url" href="jondoe-gadgets.com/dell-30.html">Jon Doe's Gadgets - $1350</a> </div> ... </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Product", "aggregateRating": { "@type": "AggregateRating", "bestRating": "100", "ratingCount": "24", "ratingValue": "87" }, "image": "dell-30in-lcd.jpg", "name": "Dell UltraSharp 30\" LCD Monitor", "offers": { "@type": "AggregateOffer", "priceCurrency": "USD", "highPrice": "1495", "lowPrice": "1250", "offerCount": "8", "offers": [ { "@type": "Offer", "url": "save-a-lot-monitors.com/dell-30.html" }, { "@type": "Offer", "url": "jondoe-gadgets.com/dell-30.html" } ] } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0461)

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
