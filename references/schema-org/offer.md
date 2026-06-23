---
title: "Offer"
source_url: https://schema.org/Offer
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Offer

# Offer

A Schema.org Type

- Canonical URL: https://schema.org/Offer
-
Equivalent Class: unece:Offer

Equivalent Class: fibo-fnd-pas-pas:Offer [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Offer)

An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.


Note: As the


For

Note: As the

[businessFunction](/businessFunction)property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.For

[GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related fields, see[Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator)and[validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide)from[GS1](http://www.gs1.org/).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[acceptedPaymentMethod](/acceptedPaymentMethod)

[LoanOrCredit](/LoanOrCredit)or[PaymentMethod](/PaymentMethod)or[Text](/Text)```
```[addOn](/addOn)

[Offer](/Offer)```
```[additionalProperty](/additionalProperty)

[PropertyValue](/PropertyValue)Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

```
```[advanceBookingRequirement](/advanceBookingRequirement)

[QuantitativeValue](/QuantitativeValue)```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[areaServed](/areaServed)

[AdministrativeArea](/AdministrativeArea)or[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)[serviceArea](/serviceArea).```
```[asin](/asin)

[Text](/Text)or[URL](/URL)[Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details. ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.

```
```[availability](/availability)

[ItemAvailability](/ItemAvailability)```
```[availabilityEnds](/availabilityEnds)

[Date](/Date)or[DateTime](/DateTime)or[Time](/Time)```
```[availabilityStarts](/availabilityStarts)

[Date](/Date)or[DateTime](/DateTime)or[Time](/Time)```
```[availableAtOrFrom](/availableAtOrFrom)

[Place](/Place)```
```[availableDeliveryMethod](/availableDeliveryMethod)

[DeliveryMethod](/DeliveryMethod)```
```[businessFunction](/businessFunction)

[BusinessFunction](/BusinessFunction)```
```[category](/category)

[CategoryCode](/CategoryCode)or[PhysicalActivityCategory](/PhysicalActivityCategory)or[Text](/Text)or[Thing](/Thing)or[URL](/URL)```
```[checkoutPageURLTemplate](/checkoutPageURLTemplate)

[Text](/Text)```
```[deliveryLeadTime](/deliveryLeadTime)

[QuantitativeValue](/QuantitativeValue)```
```[eligibleCustomerType](/eligibleCustomerType)

[BusinessEntityType](/BusinessEntityType)```
```[eligibleDuration](/eligibleDuration)

[QuantitativeValue](/QuantitativeValue)```
```[eligibleQuantity](/eligibleQuantity)

[QuantitativeValue](/QuantitativeValue)```
```[eligibleRegion](/eligibleRegion)

[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)See also

[ineligibleRegion](/ineligibleRegion).```
```[eligibleTransactionVolume](/eligibleTransactionVolume)

[PriceSpecification](/PriceSpecification)```
```[gtin](/gtin)

[Text](/Text)or[URL](/URL)[GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.A correct

[gtin](/gtin)value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a[valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator)and meet the other rules for valid GTINs. See also[GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)and[Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number)for more details. Left-padding of the gtin values is not required or encouraged. The[gtin](/gtin)property generalizes the earlier[gtin8](/gtin8),[gtin12](/gtin12),[gtin13](/gtin13), and[gtin14](/gtin14)properties.The GS1

[digital link specifications](https://www.gs1.org/standards/Digital-Link/)expresses GTINs as URLs (URIs, IRIs, etc.). Digital Links should be populated into the[hasGS1DigitalLink](/hasGS1DigitalLink)attribute.Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.

```
```[gtin12](/gtin12)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin13](/gtin13)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin14](/gtin14)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin8](/gtin8)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[hasAdultConsideration](/hasAdultConsideration)

[AdultOrientedEnumeration](/AdultOrientedEnumeration)```
```[hasGS1DigitalLink](/hasGS1DigitalLink)

[URL](/URL)[GS1 digital link](https://www.gs1.org/standards/gs1-digital-link)associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a[Product](/Product)or an[Organization](/Organization), and for the correct granularity. In particular, for products:- A Digital Link that contains a serial number (AI
`21`

) should only be present on instances of[IndividualProduct](/IndividualProduct) - A Digital Link that contains a lot number (AI
`10`

) should be annotated as[SomeProducts](/SomeProducts)if only products from that lot are sold, or[IndividualProduct](/IndividualProduct)if there is only a specific product. - A Digital Link that contains a global model number (AI
`8013`

) should be attached to a[Product](/Product)or a[ProductModel](/ProductModel).

```
```[hasMeasurement](/hasMeasurement)

[QuantitativeValue](/QuantitativeValue)```
```[hasMerchantReturnPolicy](/hasMerchantReturnPolicy)

[MerchantReturnPolicy](/MerchantReturnPolicy)[hasProductReturnPolicy](/hasProductReturnPolicy).```
```[includesObject](/includesObject)

[TypeAndQuantityNode](/TypeAndQuantityNode)[Offer](/Offer)or[ProductCollection](/ProductCollection).```
```[ineligibleRegion](/ineligibleRegion)

[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)See also

[eligibleRegion](/eligibleRegion).```
```[inventoryLevel](/inventoryLevel)

[QuantitativeValue](/QuantitativeValue)```
```[isFamilyFriendly](/isFamilyFriendly)

[Boolean](/Boolean)```
```[itemCondition](/itemCondition)

[OfferItemCondition](/OfferItemCondition)```
```[itemOffered](/itemOffered)

[AggregateOffer](/AggregateOffer)or[CreativeWork](/CreativeWork)or[Event](/Event)or[MenuItem](/MenuItem)or[Product](/Product)or[Service](/Service)or[Trip](/Trip)[businessFunction](/businessFunction), e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[offers](/offers)```
```[leaseLength](/leaseLength)

[Duration](/Duration)or[QuantitativeValue](/QuantitativeValue)[Accommodation](/Accommodation), either particular to some[Offer](/Offer)or in some cases intrinsic to the property.```
```[mobileUrl](/mobileUrl)

[Text](/Text)[mobileUrl](/mobileUrl)property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.To discourage over-use, and reflecting intial usecases, the property is expected only on

[Product](/Product)and[Offer](/Offer), rather than[Thing](/Thing). The general trend in web technology is towards[responsive design](https://en.wikipedia.org/wiki/Responsive_web_design)in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established[url](/url)property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all[url](/url)markup to use[mobileUrl](/mobileUrl)for more mobile-oriented pages. The property is intended for the case when items (primarily[Product](/Product)and[Offer](/Offer)) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.```
```[mpn](/mpn)

[Text](/Text)```
```[offeredBy](/offeredBy)

[Organization](/Organization)or[Person](/Person)Inverse property:

[makesOffer](/makesOffer)```
```[price](/price)

[Number](/Number)or[Text](/Text)Usage guidelines:

- Use the
[priceCurrency](/priceCurrency)property (with standard formats:[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR") instead of including[ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign)such as '$' in the value. - Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
- Note that both
[RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute)and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting. - Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.

```
```[priceCurrency](/priceCurrency)

[Text](/Text)[PriceSpecification](/PriceSpecification)and its subtypes.Use standard formats:

[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR".```
```[priceSpecification](/priceSpecification)

[PriceSpecification](/PriceSpecification)```
```[priceValidUntil](/priceValidUntil)

[Date](/Date)```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[seller](/seller)

[Organization](/Organization)or[Person](/Person)[vendor](/vendor),[merchant](/merchant).```
```[serialNumber](/serialNumber)

[Text](/Text)```
```[shippingDetails](/shippingDetails)

[OfferShippingDetails](/OfferShippingDetails)[Offer](/Offer).```
```[sku](/sku)

[Text](/Text)```
```[validForMemberTier](/validForMemberTier)

[MemberProgramTier](/MemberProgramTier)```
```[validFrom](/validFrom)

[Date](/Date)or[DateTime](/DateTime)```
```[validThrough](/validThrough)

[Date](/Date)or[DateTime](/DateTime)```
```[warranty](/warranty)

[WarrantyPromise](/WarrantyPromise)[warrantyPromise](/warrantyPromise).[Thing](/Thing)

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

[Offer](/Offer)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Order](/Order)[addOn](/addOn)

[Offer](/Offer)[expectsAcceptanceOf](/expectsAcceptanceOf)

[ActionAccessSpecification](/ActionAccessSpecification)or[ConsumeAction](/ConsumeAction)or[MediaSubscription](/MediaSubscription)[hasParticipationOffer](/hasParticipationOffer)

[Event](/Event)[hasSponsorshipOffer](/hasSponsorshipOffer)

[Event](/Event)[makesOffer](/makesOffer)

[Organization](/Organization)or[Person](/Person)[offers](/offers)

[AggregateOffer](/AggregateOffer)or[CreativeWork](/CreativeWork)or[EducationalOccupationalProgram](/EducationalOccupationalProgram)or[Event](/Event)or[MenuItem](/MenuItem)or[Product](/Product)or[Service](/Service)or[Trip](/Trip)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.#### More specific Types

### Acknowledgements

GoodRelations Vocabulary Terms

[uses](https://blog.schema.org/2012/11/08/good-relations-and-schema-org/)terminology from the GoodRelations Vocabulary for E-Commerce, created by Martin Hepp. GoodRelations is a data model for sharing e-commerce data on the Web. More information about GoodRelations can be found at

[http://purl.org/goodrelations/](http://purl.org/goodrelations/).

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

[Example 2](#eg-0011)

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

[Example 3](#eg-0012)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Sep 14</div> <div class="event-title">Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">9:30 PM</div> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" itemprop="name"> Typhoon with Radiation City </div> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-09-14T21:30">Sat Sep 14</div> <div class="event-title" property="name">Typhoon with Radiation City</div> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <span property="offers" typeof="Offer"> <div class="event-price"> <meta property="priceCurrency" content="USD" />$ <meta property="price" content="13.00" />13.00 </div> <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "Typhoon with Radiation City", "offers": { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0171)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Sep 14</div> <div class="event-title">Typhoon with Radiation City</div> <div class="event-title">CANCELLED - Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">9:30 PM</div> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" itemprop="name"> CANCELLED - Typhoon with Radiation City </div> <meta itemprop="eventStatus" content="https://schema.org/EventCancelled"> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"> <a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" property="name"> CANCELLED - Typhoon with Radiation City </div> <meta property="eventStatus" content="https://schema.org/EventCancelled"> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div property="offers" typeof="Offer"> $<div class="event-price" property="price">13.00</div> <meta property="priceCurrency" content="USD"><a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "eventStatus": "https://schema.org/EventCancelled", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "CANCELLED - Typhoon with Radiation City", "offers": { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0172)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Oct 12</div> <div><span>(previously scheduled for Sept 14th)</span></div> <div class="event-title">Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">10:00 PM</div> <span> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-10-12T22:00"> Sat Oct 12 </div> <div class="event-title" itemprop="name"> Typhoon with Radiation City </div> <meta itemprop="eventStatus" content="https://schema.org/EventRescheduled"><span itemprop="previousStartDate" content="2013-09-14T21:30">(previously scheduled for Sept 14th)</span> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time"> 10:00 PM </div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-10-12T22:00">Sat Oct 12</div> <div class="event-title" property="name">Typhoon with Radiation City</div> <meta property="eventStatus" content="https://schema.org/EventRescheduled"> <span property="previousStartDate" content="2013-09-14T21:30">(previously scheduled for Sept 14th)</span> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">10:00 PM</div> <span property="offers" typeof="Offer"> <div class="event-price"> <meta property="priceCurrency" content="USD" />$ <meta property="price" content="13.00" />13.00 </div> <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@graph": [ { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" } ] } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-0173)

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

[Example 7](#eg-0174)

Copied

Example notes or example HTML without markup.

JSON-LD description of a scheduled Event with limited ticket availability and performer details indicated using sameAs.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context" : "https://schema.org", "@type" : "Event", "name" : "Typhoon with Radiation City", "startDate" : "2013-09-14T21:30", "location" : { "@type" : "Place", "sameAs" : "http://www.hi-dive.com", "name" : "The Hi-Dive", "address" : { "@type" : "PostalAddress", "streetAddress" : "7 S. Broadway", "addressLocality" : "Denver", "addressRegion" : "CO", "postalCode" : "80209" } }, "performer" : [ { "@type" : "MusicGroup", "name" : "Typhoon", "sameAs" : "http://en.wikipedia.org/wiki/Typhoon_(American_band)" }, { "@type" : "MusicGroup", "name" : "RadiationCity", "sameAs" : "http://en.wikipedia.org/wiki/Radiation_City" }], "offers" : { "@type" : "Offer", "availability" : "https://schema.org/LimitedAvailability", "priceCurrency": "USD", "price" : "13.00", "url" : "http://www.ticketfly.com/purchase/309433" }, "typicalAgeRange" : "18+" } </script>

Structured representation of the JSON-LD example.

[Example 8](#eg-0201)

Copied

Example notes or example HTML without markup.

An example snippet of JSON-LD describing two B.B. King concerts.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> [{ "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King", "startDate" : "2014-04-12T19:30", "location" : { "@type" : "Place", "name" : "Lupo's Heartbreak Hotel", "address" : "79 Washington St., Providence, RI" }, "offers" : { "@type" : "Offer", "url" : "https://www.etix.com/ticket/1771656" } }, { "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King", "startDate" : "2014-04-13T20:00", "location" : { "@type" : "Place", "name" : "Lynn Auditorium", "address" : "Lynn, MA, 01901" }, "offers" : { "@type" : "Offer", "url" : "http://frontgatetickets.com/venue.php?id=11766" } }] </script>

Structured representation of the JSON-LD example.

[Example 9](#eg-0202)

Copied

Example notes or example HTML without markup.

An example of a more fully specified MusicEvent, including a tour image, full venue address, multiple performers, and multiple ticket classes.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> [{ "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King with Jonathon \"Boogie\" Long", "image" : "http://www.bbking.com/gallery/b-b-king-live.jpg", "url" : "http://www.bbking.com/events/apr12-providence.html", "startDate" : "2014-04-12T19:30", "doorTime" : "18:30:00", "endDate" : "2014-04-12T22:00", "location" : { "@type" : "Place", "name" : "Lupo's Heartbreak Hotel", "sameAs" : "http://lupos.com/", "address" : { "@type" : "PostalAddress", "streetAddress" : "79 Washington St.", "addressLocality" : "Providence", "addressRegion" : "RI", "postalCode" : "02903", "addressCountry" : "US" } }, "offers" : [ { "@type" : "Offer", "name" : "General Admission", "priceCurrency": "USD", "price" : "63.25", "availability" : "SoldOut", "url" : "http://www.ticketmaster.com/event/17004C29" },{ "@type" : "Offer", "name" : "VIP Experience", "url" : "http://www.example.com/Abcde12345", "priceCurrency": "USD", "price" : "299.00", "validFrom" : "2014-02-05T10:00", "validThrough" : "2014-03-19T23:59" } ], "performer" : [ { "@type" : "MusicGroup", "name" : "B.B. King", "sameAs" : "http://en.wikipedia.org/wiki/B.B._King" },{ "@type" : "MusicGroup", "name" : "Jonathon \"Boogie\" Long", "sameAs" : "http://jonathonboogielong.com/" } ], "eventStatus" : "EventRescheduled", "previousStartDate" : "2013-09-30T19:30", "typicalAgeRange" : "18+" }] </script>

Structured representation of the JSON-LD example.

[Example 10](#eg-0208)

Copied

Example notes or example HTML without markup.

<div> <!-- http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600 --> <span>315</span> <div> <img alt="Photo of product" src="http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg" /> <a href="http://multivarki.ru/brand_502/"> <span>BRAND 502</span> </a> <div> <span>4399 р.</span> </div>... <div> ... </div> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/ItemList"> <link itemprop="url" href="http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600"><span itemprop="numberOfItems">315</span> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/Product"> <img alt="Photo of product" itemprop="image" src="http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg"> <a itemprop="url" href="http://multivarki.ru/brand_502/"><span itemprop="name">BRAND 502</span></a> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <meta property="priceCurrency" content="RUB"> <span itemprop="price" content="4399.00">4399 р.</span> </div>... </div> <div itemprop="itemListElement" itemtype="https://schema.org/Product"> ... </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="ItemList"> <link property="url" href="http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600"><span property="numberOfItems">315</span> <div property="itemListElement" typeof="Product"> <img property="image" alt="Photo of product" src="http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg"> <a property="url" href="http://multivarki.ru/brand_502/"><span property="name">BRAND 502</span></a> <div property="offers" typeof="Offer"> <meta property="priceCurrency" content="RUB">руб <meta property="price" content="4399.00">4 399,00 <link property="itemCondition" href="https://schema.org/NewCondition"> </div>... </div> <div property="itemListElement" typeof="Product"> ... </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ItemList", "url": "http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600", "numberOfItems": "315", "itemListElement": [ { "@type": "Product", "image": "http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg", "url": "http://multivarki.ru/brand_502/", "name": "Brand 502", "offers": { "@type": "Offer", "priceCurrency": "RUB", "price": "4399.00" } }, { "@type": "Product", "name": "..." } ] } </script>

Structured representation of the JSON-LD example.

[Example 11](#eg-0393)

Copied

Example notes or example HTML without markup.

<!-- Uses both the "Book" and "Product" item types to support Offer relationships --> <div> <h3>Le concerto</h3> <div> Bibliographic Details <table> <tr> <th>Main Author: </th> <td>Ferchault, Guy</td> </tr> </table> </div> </div> <div> Holdings details from Anytown City Library <table> <!-- Example of a copy available for loan --> <tr> <th>Copy </th> <td>Available <div>Barcode: <span>CONC91000937</span></div> <div>Call number: <span>780 R2</span></div> <div>Library: <span>Anytown City Library</span></div> </td> </tr> <table> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Uses both the "Book" and "Product" item types to support Offer relationships --> <div itemscope itemtype="https://schema.org/Book" itemid="#record"> <link itemprop="additionalType" href="https://schema.org/Product"/> <h3 itemprop="name">Le concerto</h3> <div> Bibliographic Details <table> <tr> <th>Main Author: </th> <td itemprop="author">Ferchault, Guy</td> </tr> </table> </div> </div> <div> Holdings details from Anytown City Library <table> <!-- Example of a copy available for loan --> <tr itemscope itemtype="https://schema.org/Offer"> <th>Copy </th> <td>Available <link itemprop="availability" href="https://schema.org/InStock"> <div>Barcode: <span itemprop="serialNumber">CONC91000937</span></div> <div>Call number: <span itemprop="sku">780 R2</span></div> <div>Library: <span itemprop="offeredBy" itemscope itemtype="https://schema.org/Library" itemid="http://library.anytown.gov.uk" >Anytown City Library</span></div> <link itemprop="businessFunction" href="http://purl.org/goodrelations/v1#LeaseOut"> <link itemprop="itemOffered" href="#record"> </td> </tr> </table> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<!-- Uses both the "Book" and "Product" item types to support Offer relationships --> <div vocab="https://schema.org/" resource="#record" typeof="Book Product"> <h3 property="name"> Le concerto </h3> <div> Bibliographic Details <table> <tr> <th> Main Author: </th> <td property="author"> Ferchault, Guy </td> </tr> </table> </div> </div> <div> Holdings details from Anytown City Library <table vocab="https://schema.org/"> <!-- Example of a copy available for loan --> <tr typeof="Offer"> <th> Copy </th> <td> Available <div> Barcode: <span property="serialNumber">CONC91000937</span> </div> <div> Call number: <span property="sku">780 R2</span> </div> <div> Library: <span property="offeredBy" typeof="Library" resource="http://library.anytown.gov.uk">Anytown City Library</span> </div> </td> </tr> </table> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@id": "#record", "@type": "Book", "additionalType": "Product", "name": "Le concerto", "author": "Ferchault, Guy", "offers":{ "@type": "Offer", "availability": "https://schema.org/InStock", "serialNumber": "CONC91000937", "sku": "780 R2", "offeredBy": { "@type": "Library", "@id": "http://library.anytown.gov.uk", "name": "Anytown City Library" }, "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "itemOffered": "#record" } } </script>

Structured representation of the JSON-LD example.

[Example 12](#eg-0394)

Copied

Example notes or example HTML without markup.

<body> <main> <article> <h1> <a href="http://example.com/explosive-tennis-balls">Explosive tennis balls</a> </h1> <img alt="Explosive tennis balls" title src="http://example.com/explosive-tennis-balls.jpg" /> <p > $29.99 - In stock </p> <p > Tickle your friends!<br /> Surprise your opponent! <p> </article> </main> <footer> <p> © <span>2015</span> - <span property="name">Acme Inc</span> </p> <ul> <li><a href="https://twitter.com/AcmeInc">Twitter</a></li> <li><a href="https://www.facebook.com/AcmeInc">Facebook</a></li> <li><a href="https://plus.google.com/u/0/+AcmeInc/">Google+</a></li> </ul> </footer> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/" resource="http://example.com/explosive-tennis-balls" typeof="ItemPage"> <link property="copyrightHolder publisher" href="#Organization" /> <main> <article resource="#Product" property="mainEntity" typeof="Product"> <h1 property="name"> <a property="url" href="http://example.com/explosive-tennis-balls">Explosive tennis balls</a> </h1> <img property="image" alt="Explosive tennis balls" title src="http://example.com/explosive-tennis-balls.jpg" /> <p resource="#Offer" property="offers" typeof="Offer"> <meta property="priceCurrency" content="USD" /> <meta property="price" content="1000.00" /> <link property="availability" href="https://schema.org/InStock" /> <link property="itemOffered" href="#Product" /> <link property="businessFunction" href="http://purl.org/goodrelations/v1#Sell" /> <link rev="makesOffer" href="#Organization" /> $29.99 - In stock </p> <p property="description"> Tickle your friends!<br /> Surprise your opponent! <p> </article> </main> <footer> <p resource="#Organization" typeof="Organization"> © <span resource="#CopyrightYear" typeof="rdfa:Pattern">2015</span> - <span property="name">Acme Inc</span> <link property="logo" href="http://example.com/acme-inc-logo.jpg" /> <link property="url" href="http://example.com" /> <link property="rdfa:copy" href="#SameAsResource"/> </p> <ul resource="#SameAsResource" typeof="rdfa:Pattern"> <li><a property="sameAs" href="https://twitter.com/AcmeInc">Twitter</a></li> <li><a property="sameAs" href="https://www.facebook.com/AcmeInc">Facebook</a></li> <li><a property="sameAs" href="https://plus.google.com/u/0/+AcmeInc/">Google+</a></li> </ul> </footer> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@id":"http://example.com/explosive-tennis-balls", "@type":"ItemPage", "copyrightYear":"2015", "copyrightHolder":{"@id":"#Organization"}, "publisher":{"@id":"#Organization"}, "mainEntity":{ "@id":"#Product", "@type":"Product", "name":"Explosive tennis balls", "description":"Tickle your friends! Surprise your opponent!", "image":"http://example.com/explosive-tennis-balls.jpg", "url":"http://example.com/explosive-tennis-balls", "offers":{ "@id":"#Offer", "@type":"Offer", "priceCurrency":"USD", "price":"1000.00", "availability":"https://schema.org/InStock", "itemOffered":{"@id":"#Product"}, "offeredBy":{ "@id":"#Organization", "@type":"Organization", "name":"Acme Inc", "logo":"http://example.commple.com/acme-inc-logo.jpg", "url":"http://example.com/", "sameAs":["https://twitter.com/AcmeInc","https://www.facebook.com/AcmeInc","https://plus.google.com/u/0/+AcmeInc/"] } } } } </script>

Structured representation of the JSON-LD example.

[Example 13](#eg-0396)

Copied

Example notes or example HTML without markup.

ACME Home Cleaning offers a variety of services in Massachusetts, including: <ul> <li>House cleaning</li> <ul> <li>Apartment light cleaning</li> <li>House light cleaning up to 2 bedrooms</li> <li>House light cleaning 3+ bedrooms</li> </ul> <li>One-time services</li> <ul> <li>Window washing</li> <li>Carpet deep cleaning</li> <li>Move in/out cleaning</li> </ul> </ul>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Service"> <meta itemprop="serviceType" content="Home cleaning" /> <span itemprop="provider" itemscope itemtype="https://schema.org/LocalBusiness"> <span itemprop="name">ACME Home Cleaning</span> </span> offers a variety of services in <span itemprop="areaServed" itemscope itemtype="https://schema.org/State"> <span itemprop="name">Massachusetts</span>, including </span> <ul itemprop="hasOfferCatalog" itemscope itemtype="https://schema.org/OfferCatalog"> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <span itemprop="name">House cleaning</span> <ul itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Apartment light cleaning</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">House light cleaning up to 2 bedrooms</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">House light cleaning 3+ bedrooms</span> </div> </li> </ul> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <span itemprop="name">One-time services</span> <ul itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Window washing</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Carpet deep cleaning</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Move in/out cleaning</span> </div> </li> </ul> </li> </ul> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Service"> <meta property="serviceType" content="Home cleaning" /> <span property="provider" typeof="LocalBusiness"> <span property="name">ACME Home Cleaning</span> </span> offers a variety of services in <span property="areaServed" typeof="State"> <span property="name">Massachusetts</span>, including </span> <ul property="hasOfferCatalog" typeof="OfferCatalog"> <li property="itemListElement" typeof="OfferCatalog"> <span property="name">House cleaning</span> <ul property="itemListElement" typeof="OfferCatalog"> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Apartment light cleaning</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">House light cleaning up to 2 bedrooms</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">House light cleaning 3+ bedrooms</span> </div> </li> </ul> <li property="itemListElement" typeof="OfferCatalog"> <span property="name">One-time services</span> <ul property="itemListElement" typeof="OfferCatalog"> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Window washing</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Carpet deep cleaning</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Move in/out cleaning</span> </div> </li> </ul> </li> </ul> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Service", "serviceType": "Weekly home cleaning", "provider": { "@type": "LocalBusiness", "name": "ACME Home Cleaning" }, "areaServed": { "@type": "State", "name": "Massachusetts" }, "hasOfferCatalog": { "@type": "OfferCatalog", "name": "Cleaning services", "itemListElement": [ { "@type": "OfferCatalog", "name": "House Cleaning", "itemListElement": [ { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Apartment light cleaning" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "House light cleaning up to 2 bedrooms" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "House light cleaning 3+ bedrooms" } } ] }, { "@type": "OfferCatalog", "name": "One-time services", "itemListElement": [ { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Window washing" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Carpet cleaning" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Move in/out cleaning" } } ] } ] } } </script>

Structured representation of the JSON-LD example.

[Example 14](#eg-0397)

Copied

Example notes or example HTML without markup.

Joes' Pizza 123 Main Street Cambridge, MA 02142 delivers within 5 km of its store with a minimum order of $20.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/FoodEstablishment"> <span itemprop="name">Joe's Pizza</span> <div itemprop="location" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">123 Main Street</span> <span itemprop="addressLocality">Cambridge</span> <span itemprop="addressRegion">MA</span> <span itemprop="postalCode">02142</span> </div> delivers within 5 km of its store <div itemprop="makesOffer" itemscope itemtype="https://schema.org/Offer"> <div itemprop="eligibleRegion" itemscope itemtype="https://schema.org/GeoCircle"> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <meta itemprop="streetAddress" content="123 Main Street" /> <meta itemprop="addressLocality" content="Cambridge" /> <meta itemprop="addressRegion" content="MA" /> <meta itemprop="postalCode" content="02142" /> </div> <meta itemprop="geoRadius" content="5000" /> </div> with a minimum order of $20. <div itemprop="priceSpecification" itemscope itemtype="https://schema.org/DeliveryChargeSpecification"> <meta itemprop="appliesToDeliveryMethod" link="http://purl.org/goodrelations/v1#DeliveryModeOwnFleet"> <div itemprop="eligibleTransactionVolume" itemscope itemtype="https://schema.org/PriceSpecification"> <meta itemprop="price" content="20.00" /> <meta itemprop="priceCurrency" content="USD" /> </div> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="FoodEstablishment"> <span property="name">Joe's Pizza</span> <div property="location" typeof="PostalAddress"> <span property="streetAddress">123 Main Street</span> <span property="addressLocality">Cambridge</span> <span property="addressRegion">MA</span> <span property="postalCode">02142</span> </div> delivers within 5 km of its store with a minimum order of $20. <div property="makesOffer" typeof="Offer"> <div property="priceSpecification" typeof="DeliveryChargeSpecification"> <meta property="appliesToDeliveryMethod" link="http://purl.org/goodrelations/v1#DeliveryModeOwnFleet"> <div property="eligibleTransactionVolume" typeof="PriceSpecification"> <meta property="price" content="20.00" /> <meta property="priceCurrency" content="USD" /> </div> <div property="eligibleRegion" typeof="GeoCircle"> <div property="address" typeof="PostalAddress"> <meta property="streetAddress" content="123 Main Street" /> <meta property="addressLocality" content="Cambridge" /> <meta property="addressRegion" content="MA" /> <meta property="postalCode" content="02142" /> </div> <meta property="geoRadius" content="5000" /> </div> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "FoodEstablishment", "name": "Joe's Pizza", "location": { "@type": "PostalAddress", "@id": "http://example.com/address", "streetAddress": "123 Main Street", "addressLocality": "Cambridge", "addressRegion": "MA", "postalCode": "02142" }, "makesOffer": { "@type": "Offer", "priceSpecification": { "@type": "DeliveryChargeSpecification", "appliesToDeliveryMethod": "http://purl.org/goodrelations/v1#DeliveryModeOwnFleet", "eligibleTransactionVolume": { "@type": "PriceSpecification", "price": "20.00", "priceCurrency": "USD" }, "eligibleRegion": { "@type": "GeoCircle", "address": { "@id": "http://www.example.com/address" }, "geoRadius": "5000" } } } } </script>

Structured representation of the JSON-LD example.

[Example 15](#eg-0462)

Copied

Example notes or example HTML without markup.

<a href="category/books.html">Books</a> > <a href="category/books-literature.html">Literature & Fiction</a> > <a href="category/books-classics">Classics</a> <img src="catcher-in-the-rye-book-cover.jpg" alt="cover art: red horse, city in background"/> The Catcher in the Rye - Mass Market Paperback by <a href="/author/jd_salinger.html">J.D. Salinger</a> 4 stars - 3077 reviews Price: $6.99 In Stock Product details 224 pages Publisher: Little, Brown, and Company - May 1, 1991 Language: English ISBN-10: 0316769487 Reviews: 5 stars - <b>"A masterpiece of literature" </b> by John Doe. Written on May 4, 2006 I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood. 4 stars - <b>"love it LOLOL111!" </b> by Bob Smith, Written on June 15, 2006 Catcher in the Rye is a fun book. It's a good book to read.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<body itemscope itemtype="https://schema.org/WebPage"> ... <div itemprop="breadcrumb"> <a href="category/books.html">Books</a> > <a href="category/books-literature.html">Literature & Fiction</a> > <a href="category/books-classics">Classics</a> </div> <div itemprop="mainEntity" itemscope itemtype="https://schema.org/Book"> <img itemprop="image" src="catcher-in-the-rye-book-cover.jpg" alt="cover art: red horse, city in background"/> <span itemprop="name">The Catcher in the Rye</span> - <link itemprop="bookFormat" href="https://schema.org/Paperback">Mass Market Paperback by <a itemprop="author" href="/author/jd_salinger.html">J.D. Salinger</a> <div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating"> <span itemprop="ratingValue">4</span> stars - <span itemprop="reviewCount">3077</span> reviews </div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> Price: $<span itemprop="price">6.99</span> <meta itemprop="priceCurrency" content="USD" /> <link itemprop="availability" href="https://schema.org/InStock">In Stock </div> Product details <span itemprop="numberOfPages">224</span> pages Publisher: <span itemprop="publisher">Little, Brown, and Company</span> - <meta itemprop="datePublished" content="1991-05-01">May 1, 1991 Language: <span itemprop="inLanguage">English</span> ISBN-10: <span itemprop="isbn">0316769487</span> Reviews: <div itemprop="review" itemscope itemtype="https://schema.org/Review"> <span itemprop="reviewRating">5</span> stars - <b>"<span itemprop="name">A masterpiece of literature</span>"</b> by <span itemprop="author">John Doe</span>, Written on <meta itemprop="datePublished" content="2006-05-04">May 4, 2006 <span itemprop="reviewBody">I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.</span> </div> <div itemprop="review" itemscope itemtype="https://schema.org/Review"> <span itemprop="reviewRating">4</span> stars - <b>"<span itemprop="name">A good read.</span>" </b> by <span itemprop="author">Bob Smith</span>, Written on <meta itemprop="datePublished" content="2006-06-15">June 15, 2006 <span itemprop="reviewBody">Catcher in the Rye is a fun book. It's a good book to read.</span> </div> </div> ... </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/" typeof="WebPage"> ... <div property="breadcrumb"> <a href="category/books.html">Books</a> > <a href="category/books-literature.html">Literature & Fiction</a> > <a href="category/books-classics">Classics</a> </div> <div property="mainEntity" typeof="Book"> <img property="image" src="catcher-in-the-rye-book-cover.jpg" alt="cover art: red horse, city in background"/> <span property="name">The Catcher in the Rye</span> - <link property="bookFormat" href="https://schema.org/Paperback">Mass Market Paperback by <a property="author" href="/author/jd_salinger.html">J.D. Salinger</a> <div property="aggregateRating" typeof="AggregateRating"> <span property="ratingValue">4</span> stars - <span property="reviewCount">3077</span> reviews </div> <div property="offers" typeof="Offer"> Price: $<span property="price">6.99</span> <meta property="priceCurrency" content="USD" /> <link property="availability" href="https://schema.org/InStock">In Stock </div> Product details <span property="numberOfPages">224</span> pages Publisher: <span property="publisher">Little, Brown, and Company</span> - <meta property="datePublished" content="1991-05-01">May 1, 1991 Language: <span property="inLanguage">English</span> ISBN-10: <span property="isbn">0316769487</span> Reviews: <div property="review" typeof="Review"> <span property="reviewRating">5</span> stars - <b>"<span property="name">A masterpiece of literature</span>"</b> by <span property="author">John Doe</span>, Written on <meta property="datePublished" content="2006-05-04">May 4, 2006 <span property="reviewBody">I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.</span> </div> <div property="review" typeof="Review"> <span property="reviewRating">4</span> stars - <b>"<span property="name">A good read.</span>" </b> by <span property="author">Bob Smith</span>, Written on <meta property="datePublished" content="2006-06-15">June 15, 2006 <span property="reviewBody">Catcher in the Rye is a fun book. It's a good book to read.</span> </div> </div> ... </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "WebPage", "breadcrumb": "Books > Literature & Fiction > Classics", "mainEntity":{ "@type": "Book", "author": "/author/jd_salinger.html", "bookFormat": "https://schema.org/Paperback", "datePublished": "1991-05-01", "image": "catcher-in-the-rye-book-cover.jpg", "inLanguage": "English", "isbn": "0316769487", "name": "The Catcher in the Rye", "numberOfPages": "224", "offers": { "@type": "Offer", "availability": "https://schema.org/InStock", "price": "6.99", "priceCurrency": "USD" }, "publisher": "Little, Brown, and Company", "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4", "reviewCount": "3077" }, "review": [ { "@type": "Review", "author": "John Doe", "datePublished": "2006-05-04", "name": "A masterpiece of literature", "reviewBody": "I really enjoyed this book. It captures the essential challenge people face as they try make sense of their lives and grow to adulthood.", "reviewRating": { "@type": "Rating", "ratingValue": "5" } }, { "@type": "Review", "author": "Bob Smith", "datePublished": "2006-06-15", "name": "A good read.", "reviewBody": "Catcher in the Rye is a fun book. It's a good book to read.", "reviewRating": "4" } ] } } </script>

Structured representation of the JSON-LD example.

[Example 16](#eg-0475)

Copied

Example notes or example HTML without markup.

An example of an offer with a checkoutPageURLTemplate.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"Product", "sku":"12345", "image":"https://example.com/fnobarizer.jpg", "name":"Advanced Fnobarizer", "brand":{ "@type":"Brand", "name":"Nucleatronics Inc." }, "offers":{ "@type":"Offer", "checkoutPageURLTemplate":"https://www.example.com/checkout?items={VARIANT_ID_1}:{Quantity_1},{VARIANT_ID_2}:{Quantity_2}&discount={DISCOUNT_CODE}&store_id={pickup_store_id}", "priceSpecification":{ "@type":"PriceSpecification", "price":"99.99", "priceCurrency":"USD" }, "acceptedPaymentMethod":"http://purl.org/goodrelations/v1#GoogleCheckout" } } </script>

Structured representation of the JSON-LD example.

[Example 17](#eg-3617a)

Copied

Example notes or example HTML without markup.

Offer with free shipping in the US and Canada (in the V2 Shipping format).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Product", "name": "JSON Example", "offers": { "@type": "Offer", "shippingDetails": { "@type": "OfferShippingDetails", "height": "12 in", "width": "45 cm", "depth": "0.3 m", "weight": "1.2 kg", "hasShippingService": { "@type": "ShippingService", "shippingConditions": { "@type": "ShippingConditions", "shippingDestination": [ { "@type": "DefinedRegion", "addressCountry": "US" }, { "@type": "DefinedRegion", "addressCountry": "CA" } ], "shippingRate": "0" } } } } } </script>

Structured representation of the JSON-LD example.

[Example 18](#eg-3617c)

Copied

Example notes or example HTML without markup.

Offer with shipping costs of $10 + $1/kg for orders $35-$200, to the US and Canada, with a handling time of 3.5 hours on weekdays (in the V2 format).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Product", "name": "JSON Example", "offers": { "@type": "Offer", "shippingDetails": { "@type": "OfferShippingDetails", "height": "12 in", "width": "45 cm", "depth": "300 mm", "weight": "1.2 kg", "hasShippingService": { "@type": "ShippingService", "handlingTime": { "@type": "ServicePeriod", "cutoffTime": "14:30:00-07:00", "duration": { "@type": "QuantitativeValue", "maxValue": "30", "unitCode": "min" } }, "shippingConditions": { "@type": "ShippingConditions", "shippingDestination": [ { "@type": "DefinedRegion", "addressCountry": "US" }, { "@type": "DefinedRegion", "addressCountry": "CA" } ], "orderValue": { "@type": "MonetaryAmount", "minValue": "35", "maxValue": "200" }, "shippingRate": { "@type": "ShippingRateSettings", "shippingRate": { "@type": "MonetaryAmount", "value": "10", "currency": "USD" }, "weightPercentage": "1.0" }, "transitTime": { "@type": "ServicePeriod", "duration": { "maxValue": "3.5", "unitCode": "h" }, "businessDays": [ { "dayOfWeek": "Monday" }, { "dayOfWeek": "Tuesday" }, { "dayOfWeek": "Wednesday" }, { "dayOfWeek": "Thursday" }, { "dayOfWeek": "Friday" } ] } } } } } } </script>

Structured representation of the JSON-LD example.

[Example 19](#eg-4505)

Copied

Example notes or example HTML without markup.

<strong>Château Snotty 2020</strong> The snottiest red wine on the market. <ul> <li>Organic red wine, made in France</li> <li>2020 Vintage, a very interesting year</li> <li>75 cl bottle</li> <li>Cru du Pichet d'Or</li> <li>Best before 2026</li> <li>Contains Sulfite</li> <li>Please recycle the glass bottle</li> </ul>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": { "@vocab": "https://schema.org/", "gs1": "https://ref.gs1.org/voc/", "unece": "https://vocabulary.uncefact.org/" }, "@graph": [ { "@type": [ "https://schema.org/DefinedRegion", "https://schema.org/PostalAddress" ], "@id": "http://example.com/lechateausnottyaddress", "addressCountry": "FR", "addressLocality": "L'Introuvable", "addressRegion": "Charentes" }, { "@type": ["QuantitativeValue", "gs1:QuantitativeValue", "unece:MeasureType"], "@id": "http://example.com/lechateausnottynetmass", "name": "Net mass", "unitCode": "KGM", "unitText": "kg.", "value": 0.75, "gs1:unitCode": "KGM", "gs1:value": 0.75, "unece:MeasureTypeValue": 75, "unece:MeasureTypeCode": "unece:WeightUnitMeasureCode#KGM", "unece:measuredAttributeCode": "unece:MeasuredAttributeCodeList#AAA" }, { "@type": ["QuantitativeValue", "gs1:QuantitativeValue", "unece:MeasureType"], "@id": "http://example.com/lechateausnottygrossmass", "name": "Gross mass", "unitCode": "KGM", "unitText": "kg.", "value": 1, "gs1:unitCode": "KGM", "gs1:value": 1, "unece:MeasureTypeValue": 1, "unece:MeasureTypeCode": "unece:WeightUnitMeasureCode#KGM", "unece:measuredAttributeCode": "unece:MeasuredAttributeCodeList#ACN" }, { "@type": [ "Organization", "gs1:Organization", "unece:TradeParty" ], "@id": "http://example.com/lechateausnotty", "name": "Domaine du Château Snotty", "address": { "@id": "http://example.com/lechateausnottyaddress" }, "unece:allianceName": "Les Châteaux obscurs de Charente" }, { "@type": [ "Organization", "gs1:Organization" ], "@id": "http://example.com/oenologuesatteres", "name": "Association des Œnologues attérés" }, { "@type": [ "Certification", "unece:TradeProductCertification" ], "@id": "http://example.com/certifiedpretentiouswine", "name": "Certified Pretentious Wine", "certificationIdentification": "pichetdor", "issuedBy": { "@id": "http://example.com/oenologuesatteres" }, "certificationRating": { "@type": "Rating", "ratingValue": "Pichet d'Or" } }, { "@type": [ "Product", "unece:TradeProduct", "gs1:Beverage" ], "name": "Château Snotty 2020", "description": [ { "@value": "The snottiest red wine on the market.", "@language": "en" }, { "@value": "Le vin le plus prétentieux du marché.", "@language": "fr" } ], "url": "https://www.example.com/chateau-snotty", "image": "https://www.example.com/chateau-snotty.jpg", "offers": { "@type": "Offer", "availability": "https://schema.org/InStock", "priceValidUntil": "2026-01-01", "price": "999.00", "priceCurrency": "EUR", "seller": { "@id": "http://example.com/lechateausnotty" }, "hasMerchantReturnPolicy": { "@type": "MerchantReturnPolicy", "applicableCountry": "EU", "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted" }, "shippingDetails": { "@type": "OfferShippingDetails", "shippingDestination": { "@type": "DefinedRegion", "name": "Europe", "addressCountry": "EU" }, "shippingRate": { "@type": "MonetaryAmount", "name": "Free", "value": 0, "currency": "EUR" }, "deliveryTime": { "@type": "ShippingDeliveryTime", "handlingTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 2, "unitText": "Days", "unitCode": "DAY" }, "transitTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 5, "unitText": "Days", "unitCode": "DAY" } }, "hasShippingService": { "@type": "ShippingService", "name": "Postal Service", "fulfillmentType": "https://schema.org/FulfillmentTypeDelivery", "shippingConditions": { "@type": "ShippingConditions", "shippingOrigin": { "@id": "http://example.com/lechateausnottyaddress" }, "orderValue": { "@type": "MonetaryAmount", "value": 100.0, "currency": "EUR" } } } } }, "manufacturer": { "@id": "http://example.com/lechateausnotty" }, "weight": [{ "@id": "http://example.com/lechateausnottynetmass" }, { "@id": "http://example.com/lechateausnottygrossmass" }], "productionDate": "2020-10-01", "hasCertification": { "@id": "http://example.com/certifiedpretentiouswine" }, "aggregateRating": { "@type": "AggregateRating", "ratingCount": 33, "ratingValue": 4.7, "bestRating": 5, "worstRating": 1 }, "review": { "@type": "Review", "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1 }, "reviewBody": { "@value": "Oncques n'a jamais vu de vin plus prétentieux", "@language": "fr" }, "author": { "@type": "Person", "name": "Jean d'Eau" } }, "gs1:bestBeforeDate": "2027-01-01", "gs1:AdditiveDetails": { "@type": "gs1:AdditiveDetails", "gs1:additiveName": "Sulfite", "gs1:additiveLevelOfContainment": "gs1:LevelOfContainmentCode-CONTAINS" }, "gs1:netWeight": { "@id": "http://example.com/lechateausnottynetmass" }, "gs1:beverageVintage": "2020", "gs1:gpcCategoryCode": "10000276", "gs1:percentageOfAlcoholByVolume": 4.0, "gs1:vintner": "Domaine du Château Snotty", "gs1:alcoholicBeverageSubregion": "FR-16", "gs1:sweetnessLevelOfAlcoholicBeverage": "gs1:SweetnessLevelOfAlcoholicBeverageCode-DRY", "gs1:growingMethod": "gs1:GrowingMethodCode-ORGANIC", "gs1:packagingMarkedLabelAccreditation": "gs1:PackagingMarkedLabelAccreditationCode-EU_ECO_LABEL", "gs1:consumerSalesCondition": "gs1:ConsumerSalesConditionsCode-RESTRICTED_TO_SELL_16", "gs1:seller": { "@id": "http://example.com/lechateausnotty" }, "unece:specifiedMarking": { "@type": "unece:Marking", "unece:packagingMarkingTypeCode": [ "unece:PackagingMarkingCodeList#32", "unece:PackagingMarkingCodeList#9" ] }, "unece:fromDeliveryLifeSpanMeasure": { "@type": "unece:SupplyChainPackaging", "unece:DurationUnitMeasureCode": "unece:DurationUnitMeasureCode#MON", "unece:DurationUnitMeasureTypeValue": 6 }, "unece:recyclableIndicator": true, "unece:applicableTradeProductCertification": { "@id": "http://example.com/certifiedpretentiouswine" }, "unece:manufacturerParty": { "@id": "http://example.com/lechateausnotty" }, "unece:netWeightMeasure": { "@id": "http://example.com/lechateausnottynetmass" }, "unece:grossWeightMeasure": { "@id": "http://example.com/lechateausnottygrossmass" } } ] } </script>

Structured representation of the JSON-LD example.
