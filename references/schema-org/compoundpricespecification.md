---
title: "CompoundPriceSpecification"
source_url: https://schema.org/CompoundPriceSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# CompoundPriceSpecification

# CompoundPriceSpecification

A Schema.org Type

- Canonical URL: https://schema.org/CompoundPriceSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+CompoundPriceSpecification)

A compound price specification is one that bundles multiple prices that all apply in combination for different dimensions of consumption. Use the name property of the attached unit price specification for indicating the dimension of a price component (e.g. "electricity" or "final cleaning").

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[priceComponent](/priceComponent)

[PriceSpecification](/PriceSpecification)[UnitPriceSpecification](/UnitPriceSpecification)nodes that apply in parallel for the[CompoundPriceSpecification](/CompoundPriceSpecification)node.```
```[priceType](/priceType)

[PriceTypeEnumeration](/PriceTypeEnumeration)or[Text](/Text)[priceType](/priceType)property can be used to identify the type of each such specified price. The value of priceType can be specified as a value from enumeration PriceTypeEnumeration or, a UN/EDIFACT 5387 code, or as a free form text string for price types that are not already predefined in PriceTypeEnumeration.[PriceSpecification](/PriceSpecification)

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
