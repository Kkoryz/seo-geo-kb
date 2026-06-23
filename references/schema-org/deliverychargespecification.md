---
title: "DeliveryChargeSpecification"
source_url: https://schema.org/DeliveryChargeSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# DeliveryChargeSpecification

# DeliveryChargeSpecification

A Schema.org Type

- Canonical URL: https://schema.org/DeliveryChargeSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+DeliveryChargeSpecification)

The price for the delivery of an offer using a particular delivery method.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[appliesToDeliveryMethod](/appliesToDeliveryMethod)

[DeliveryMethod](/DeliveryMethod)```
```[areaServed](/areaServed)

[AdministrativeArea](/AdministrativeArea)or[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)[serviceArea](/serviceArea).```
```[eligibleRegion](/eligibleRegion)

[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)See also

[ineligibleRegion](/ineligibleRegion).```
```[ineligibleRegion](/ineligibleRegion)

[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)See also

[eligibleRegion](/eligibleRegion).[PriceSpecification](/PriceSpecification)

```
```[eligibleQuantity](/eligibleQuantity)

[QuantitativeValue](/QuantitativeValue)```
```[eligibleTransactionVolume](/eligibleTransactionVolume)

[PriceSpecification](/PriceSpecification)```
```[maxPrice](/maxPrice)

[Number](/Number)```
```[membershipPointsEarned](/membershipPointsEarned)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)```
```[minPrice](/minPrice)

[Number](/Number)```
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
```[validForMemberTier](/validForMemberTier)

[MemberProgramTier](/MemberProgramTier)```
```[validFrom](/validFrom)

[Date](/Date)or[DateTime](/DateTime)```
```[validThrough](/validThrough)

[Date](/Date)or[DateTime](/DateTime)```
```[valueAddedTaxIncluded](/valueAddedTaxIncluded)

[Boolean](/Boolean)[Thing](/Thing)

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

[DeliveryChargeSpecification](/DeliveryChargeSpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ShippingRateSettings](/ShippingRateSettings)[OfferShippingDetails](/OfferShippingDetails)with[shippingSettingsLink](/shippingSettingsLink)matching this[ShippingRateSettings](/ShippingRateSettings).### Examples

[Example 1](#eg-0397)

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
