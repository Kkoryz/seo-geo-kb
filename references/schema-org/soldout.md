---
title: "SoldOut"
source_url: https://schema.org/SoldOut
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# SoldOut

# SoldOut

A Schema.org Enumeration Member

- Canonical URL: https://schema.org/SoldOut
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+SoldOut)

Indicates that the item has sold out.

A member value for enumeration type:

[ItemAvailability](/ItemAvailability)

### Examples

[Example 1](#eg-0173)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Sep 14</div> <div class="event-title">SOLD OUT! Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">10:00 PM</div> <span> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" itemprop="name"> SOLD OUT! Typhoon with Radiation City </div> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <meta itemprop="availability" content="https://schema.org/SoldOut"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-09-14T21:30">Sat Sep 14</div> <div class="event-title" property="name">SOLD OUT! Typhoon with Radiation City</div> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <span property="offers" typeof="Offer"> <meta property="availability" content="https://schema.org/SoldOut"> <div class="event-price"> <meta property="priceCurrency" content="USD" />$ <meta property="price" content="13.00" />13.00 </div> <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "SOLD OUT! Typhoon with Radiation City", "offers": { "@type": "Offer", "availability": "https://schema.org/SoldOut", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" } </script>

Structured representation of the JSON-LD example.
