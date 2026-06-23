---
title: "reviewCount"
source_url: https://schema.org/reviewCount
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# reviewCount

# reviewCount

A Schema.org Property

- Canonical URL: https://schema.org/reviewCount
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+reviewCount)

The count of total number of reviews.

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0004)

Copied

Example notes or example HTML without markup.

GreatFood 4 stars - based on 250 reviews 1901 Lemur Ave Sunnyvale, CA 94086 (408) 714-1489 <a href="http://www.greatfood.com">www.greatfood.com</a> Hours: Mon-Sat 11am - 2:30pm Mon-Thur 5pm - 9:30pm Fri-Sat 5pm - 10pm Categories: Middle Eastern, Mediterranean Price Range: $$ Takes Reservations: Yes

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Restaurant"> <span itemprop="name">GreatFood</span> <div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating"> <span itemprop="ratingValue">4</span> stars - based on <span itemprop="reviewCount">250</span> reviews </div> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">1901 Lemur Ave</span> <span itemprop="addressLocality">Sunnyvale</span>, <span itemprop="addressRegion">CA</span> <span itemprop="postalCode">94086</span> </div> <span itemprop="telephone">(408) 714-1489</span> <a itemprop="url" href="http://www.greatfood.com">www.greatfood.com</a> Hours: <meta itemprop="openingHours" content="Mo-Sa 11:00-14:30">Mon-Sat 11am - 2:30pm <meta itemprop="openingHours" content="Mo-Th 17:00-21:30">Mon-Thu 5pm - 9:30pm <meta itemprop="openingHours" content="Fr-Sa 17:00-22:00">Fri-Sat 5pm - 10:00pm Categories: <span itemprop="servesCuisine"> Middle Eastern </span>, <span itemprop="servesCuisine"> Mediterranean </span> Price Range: <span itemprop="priceRange">$$</span> Takes Reservations: Yes </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Restaurant"> <span property="name">GreatFood</span> <div property="aggregateRating" typeof="AggregateRating"> <span property="ratingValue">4</span> stars - based on <span property="reviewCount">250</span> reviews </div> <div property="address" typeof="PostalAddress"> <span property="streetAddress">1901 Lemur Ave</span> <span property="addressLocality">Sunnyvale</span>, <span property="addressRegion">CA</span> <span property="postalCode">94086</span> </div> <span property="telephone">(408) 714-1489</span> <a property="url" href="http://www.greatfood.com">www.greatfood.com</a> Hours: <meta property="openingHours" content="Mo-Sa 11:00-14:30">Mon-Sat 11am - 2:30pm <meta property="openingHours" content="Mo-Th 17:00-21:30">Mon-Thu 5pm - 9:30pm <meta property="openingHours" content="Fr-Sa 17:00-22:00">Fri-Sat 5pm - 10:00pm Categories: <span property="servesCuisine"> Middle Eastern </span>, <span property="servesCuisine"> Mediterranean </span> Price Range: <span property="priceRange">$$</span> Takes Reservations: Yes </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Restaurant", "address": { "@type": "PostalAddress", "addressLocality": "Sunnyvale", "addressRegion": "CA", "postalCode": "94086", "streetAddress": "1901 Lemur Ave" }, "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4", "reviewCount": "250" }, "name": "GreatFood", "openingHours": [ "Mo-Sa 11:00-14:30", "Mo-Th 17:00-21:30", "Fr-Sa 17:00-22:00" ], "priceRange": "$$", "servesCuisine": [ "Middle Eastern", "Mediterranean" ], "telephone": "(408) 714-1489", "url": "http://www.greatfood.com" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0010)

Copied

Example notes or example HTML without markup.

Kenmore White 17" Microwave <img src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' /> Rated 3.5/5 based on 11 customer reviews $55.00 In stock Product description: 0.7 cubic feet countertop microwave. Has six preset cooking categories and convenience features like Add-A-Minute and Child Lock. Customer reviews: Not a happy camper - by Ellie, April 1, 2011 1/5 stars The lamp burned out and now I have to replace it. Value purchase - by Lucas, March 25, 2011 4/5 stars Great microwave for the price. It is small and fits in my apartment. ...

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Product"> <span itemprop="name">Kenmore White 17" Microwave</span> <img itemprop="image" src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' /> <div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating"> Rated <span itemprop="ratingValue">3.5</span>/5 based on <span itemprop="reviewCount">11</span> customer reviews </div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <!--price is 1000, a number, with locale-specific thousands separator and decimal mark, and the $ character is marked up with the machine-readable code "USD" --> <span itemprop="priceCurrency" content="USD">$</span><span itemprop="price" content="1000.00">1,000.00</span> <link itemprop="availability" href="https://schema.org/InStock" />In stock </div> Product description: <span itemprop="description">0.7 cubic feet countertop microwave. Has six preset cooking categories and convenience features like Add-A-Minute and Child Lock.</span> Customer reviews: <div itemprop="review" itemscope itemtype="https://schema.org/Review"> <span itemprop="name">Not a happy camper</span> - by <span itemprop="author">Ellie</span>, <meta itemprop="datePublished" content="2011-04-01">April 1, 2011 <div itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating"> <meta itemprop="worstRating" content = "1"> <span itemprop="ratingValue">1</span>/ <span itemprop="bestRating">5</span>stars </div> <span itemprop="reviewBody">The lamp burned out and now I have to replace it. </span> </div> <div itemprop="review" itemscope itemtype="https://schema.org/Review"> <span itemprop="name">Value purchase</span> - by <span itemprop="author">Lucas</span>, <meta itemprop="datePublished" content="2011-03-25">March 25, 2011 <div itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating"> <meta itemprop="worstRating" content = "1"/> <span itemprop="ratingValue">4</span>/ <span itemprop="bestRating">5</span>stars </div> <span itemprop="reviewBody">Great microwave for the price. It is small and fits in my apartment.</span> </div> ... </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Product"> <span property="name">Kenmore White 17" Microwave</span> <img property="image" src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' /> <div property="aggregateRating" typeof="AggregateRating"> Rated <span property="ratingValue">3.5</span>/5 based on <span property="reviewCount">11</span> customer reviews </div> <div property="offers" typeof="Offer"> <!--price is 1000, a number, with locale-specific thousands separator and decimal mark, and the $ character is marked up with the machine-readable code "USD" --> <span property="priceCurrency" content="USD">$</span><span property="price" content="1000.00">1,000.00</span> <link property="availability" href="https://schema.org/InStock" />In stock </div> Product description: <span property="description">0.7 cubic feet countertop microwave. Has six preset cooking categories and convenience features like Add-A-Minute and Child Lock.</span> Customer reviews: <div property="review" typeof="Review"> <span property="name">Not a happy camper</span> - by <span property="author">Ellie</span>, <meta property="datePublished" content="2011-04-01">April 1, 2011 <div property="reviewRating" typeof="Rating"> <meta property="worstRating" content = "1"> <span property="ratingValue">1</span>/ <span property="bestRating">5</span>stars </div> <span property="reviewBody">The lamp burned out and now I have to replace it. </span> </div> <div property="review" typeof="Review"> <span property="name">Value purchase</span> - by <span property="author">Lucas</span>, <meta property="datePublished" content="2011-03-25">March 25, 2011 <div property="reviewRating" typeof="Rating"> <meta property="worstRating" content = "1"/> <span property="ratingValue">4</span>/ <span property="bestRating">5</span>stars </div> <span property="reviewBody">Great microwave for the price. It is small and fits in my apartment.</span> </div> ... </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Product", "aggregateRating": { "@type": "AggregateRating", "ratingValue": "3.5", "reviewCount": "11" }, "description": "0.7 cubic feet countertop microwave. Has six preset cooking categories and convenience features like Add-A-Minute and Child Lock.", "name": "Kenmore White 17\" Microwave", "image": "kenmore-microwave-17in.jpg", "offers": { "@type": "Offer", "availability": "https://schema.org/InStock", "price": "55.00", "priceCurrency": "USD" }, "review": [ { "@type": "Review", "author": "Ellie", "datePublished": "2011-04-01", "reviewBody": "The lamp burned out and now I have to replace it.", "name": "Not a happy camper", "reviewRating": { "@type": "Rating", "bestRating": "5", "ratingValue": "1", "worstRating": "1" } }, { "@type": "Review", "author": "Lucas", "datePublished": "2011-03-25", "reviewBody": "Great microwave for the price. It is small and fits in my apartment.", "name": "Value purchase", "reviewRating": { "@type": "Rating", "bestRating": "5", "ratingValue": "4", "worstRating": "1" } } ] } </script>

Structured representation of the JSON-LD example.
