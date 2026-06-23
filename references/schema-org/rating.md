---
title: "Rating"
source_url: https://schema.org/Rating
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Rating

# Rating

A Schema.org Type

- Canonical URL: https://schema.org/Rating
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Rating)

A rating is an evaluation on a numeric scale, such as 1 to 5 stars.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[author](/author)

[Organization](/Organization)or[Person](/Person)```
```[bestRating](/bestRating)

[Number](/Number)or[Text](/Text)```
```[ratingExplanation](/ratingExplanation)

[Text](/Text)[ClaimReview](/ClaimReview).```
```[ratingValue](/ratingValue)

[Number](/Number)or[Text](/Text)Usage guidelines:

- Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

```
```[reviewAspect](/reviewAspect)

[StructuredValue](/StructuredValue)or[Text](/Text)```
```[worstRating](/worstRating)

[Number](/Number)or[Text](/Text)[Thing](/Thing)

```
```[additionalType](/additionalType)

[Text](/Text)or[URL](/URL)[style guide](https://schema.org/docs/styleguide.html).```
```[alternateName](/alternateName)

[Text](/Text)```
```[description](/description)

[Text](/Text)or[TextObject](/TextObject)```
```[disambiguatingDescription](/disambiguatingDescription)

[Text](/Text)```
```[identifier](/identifier)

[PropertyValue](/PropertyValue)or[Text](/Text)or[URL](/URL)[Thing](/Thing), such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See[background notes](/docs/datamodel.html#identifierBg)for more details.```
```[image](/image)

[ImageObject](/ImageObject)or[URL](/URL)[URL](/URL)or a fully described[ImageObject](/ImageObject).```
```[mainEntityOfPage](/mainEntityOfPage)

[CreativeWork](/CreativeWork)or[URL](/URL)[background notes](/docs/datamodel.html#mainEntityBackground)for details.Inverse property:

[mainEntity](/mainEntity)```
```[name](/name)

[Text](/Text)```
```[owner](/owner)

[Organization](/Organization)or[Person](/Person)Inverse property:

[owns](/owns)```
```[potentialAction](/potentialAction)

[Action](/Action)```
```[sameAs](/sameAs)

[URL](/URL)```
```[subjectOf](/subjectOf)

[CreativeWork](/CreativeWork)or[Event](/Event)Inverse property:

[about](/about)```
```[url](/url)

[URL](/URL)Instances of

[Rating](/Rating)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Certification](/Certification)[gs1:certificationValue](https://www.gs1.org/voc/certificationValue).[contentRating](/contentRating)

[CreativeWork](/CreativeWork)[reviewRating](/reviewRating)

[Review](/Review)`reviewRating`

applies to rating given by the review. The [aggregateRating](/aggregateRating)property applies to the review itself, as a creative work.[starRating](/starRating)

[FoodEstablishment](/FoodEstablishment)or[LodgingBusiness](/LodgingBusiness)#### More specific Types

### Examples

[Example 1](#eg-0010)

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

[Example 2](#eg-0248)

Copied

Example notes or example HTML without markup.

See JSON example.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Review", "reviewBody": "The restaurant has great ambiance.", "itemReviewed": { "@type": "Restaurant", "name": "Fine Dining Establishment" }, "reviewRating": { "@type": "Rating", "ratingValue": 5, "worstRating": 1, "bestRating": 5, "reviewAspect": "Ambiance" } } </script>

Structured representation of the JSON-LD example.
