---
title: "LodgingReservation"
source_url: https://schema.org/LodgingReservation
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2017-04-11
---

# LodgingReservation

# LodgingReservation

A Schema.org Type

- Canonical URL: https://schema.org/LodgingReservation
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+LodgingReservation)

A reservation for lodging at a hotel, motel, inn, etc.


Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[checkinTime](/checkinTime)

[DateTime](/DateTime)or[Time](/Time)```
```[checkoutTime](/checkoutTime)

[DateTime](/DateTime)or[Time](/Time)```
```[lodgingUnitDescription](/lodgingUnitDescription)

[Text](/Text)```
```[lodgingUnitType](/lodgingUnitType)

[QualitativeValue](/QualitativeValue)or[Text](/Text)```
```[numAdults](/numAdults)

[Integer](/Integer)or[QuantitativeValue](/QuantitativeValue)```
```[numChildren](/numChildren)

[Integer](/Integer)or[QuantitativeValue](/QuantitativeValue)[Reservation](/Reservation)

```
```[bookingTime](/bookingTime)

[DateTime](/DateTime)```
```[broker](/broker)

[Organization](/Organization)or[Person](/Person)[bookingAgent](/bookingAgent).```
```[modifiedTime](/modifiedTime)

[DateTime](/DateTime)```
```[priceCurrency](/priceCurrency)

[Text](/Text)[PriceSpecification](/PriceSpecification)and its subtypes.Use standard formats:

[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR".```
```[programMembershipUsed](/programMembershipUsed)

[ProgramMembership](/ProgramMembership)```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[reservationFor](/reservationFor)

[Thing](/Thing)```
```[reservationId](/reservationId)

[Text](/Text)```
```[reservationStatus](/reservationStatus)

[ReservationStatusType](/ReservationStatusType)```
```[reservedTicket](/reservedTicket)

[Ticket](/Ticket)```
```[totalPrice](/totalPrice)

[Number](/Number)or[PriceSpecification](/PriceSpecification)or[Text](/Text)Usage guidelines:

- Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

```
```[underName](/underName)

[Organization](/Organization)or[Person](/Person)[Thing](/Thing)

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

[URL](/URL)### Examples

[Example 1](#eg-0183)

Copied

Example notes or example HTML without markup.

Original: Hotel Reservation #abc456 under name: John Smith Hilton San Francisco Union Square 333 O'Farrell Street San Francisco, CA 94102 check in: 2017-04-11T16:00:00-08:00 check out: 2017-04-13T11:00:00-08:00

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "LodgingReservation", "reservationId": "abc456", "reservationStatus": "https://schema.org/ReservationConfirmed", "underName": { "@type": "Person", "name": "John Smith" }, "reservationFor": { "@type": "LodgingBusiness", "name": "Hilton San Francisco Union Square", "address": { "@type": "PostalAddress", "streetAddress": "333 O'Farrell St", "addressLocality": "San Francisco", "addressRegion": "CA", "postalCode": "94102", "addressCountry": "US" }, "telephone": "415-771-1400" }, "checkinTime": "2017-04-11T16:00:00-08:00", "checkoutTime": "2017-04-13T11:00:00-08:00" } </script>

Structured representation of the JSON-LD example.
