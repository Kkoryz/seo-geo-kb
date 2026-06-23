---
title: "AggregateOffer"
source_url: https://schema.org/AggregateOffer
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# AggregateOffer

# AggregateOffer

A Schema.org Type

- Canonical URL: https://schema.org/AggregateOffer
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+AggregateOffer)

When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.


Note: AggregateOffers are normally expected to associate multiple offers that all share the same defined

Note: AggregateOffers are normally expected to associate multiple offers that all share the same defined

[businessFunction](/businessFunction)value, or default to http://purl.org/goodrelations/v1#Sell if businessFunction is not explicitly defined.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[highPrice](/highPrice)

[Number](/Number)or[Text](/Text)Usage guidelines:

- Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

```
```[lowPrice](/lowPrice)

[Number](/Number)or[Text](/Text)Usage guidelines:

- Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

```
```[offerCount](/offerCount)

[Integer](/Integer)```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)[Offer](/Offer)

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

[AggregateOffer](/AggregateOffer)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction), e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.### Examples

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
