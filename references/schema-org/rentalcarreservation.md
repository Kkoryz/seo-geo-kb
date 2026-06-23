---
title: "RentalCarReservation"
source_url: https://schema.org/RentalCarReservation
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2017-08-05
---

# RentalCarReservation

# RentalCarReservation

A Schema.org Type

- Canonical URL: https://schema.org/RentalCarReservation
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+RentalCarReservation)

A reservation for a rental car.


Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[dropoffLocation](/dropoffLocation)

[Place](/Place)```
```[dropoffTime](/dropoffTime)

[DateTime](/DateTime)```
```[pickupLocation](/pickupLocation)

[Place](/Place)```
```[pickupTime](/pickupTime)

[DateTime](/DateTime)[Reservation](/Reservation)

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

[Example 1](#eg-0184)

Copied

Example notes or example HTML without markup.

Car rental reservation #546323 Customer: John Smith Car: Honda Civic (Economy Class) Rental company: Hertz Pick up location: Hertz San Diego Airport 1500 Orange Avenue San Diego, CA 94043 Pickup time: 2017-08-05T16:00:00-07:00 Drop off location: Hertz LAX 1234 First Street Los Angeles, CA 94043 Drop off time: 2017-08-06T20:00:00-07:00

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "RentalCarReservation", "reservationId": "546323", "reservationStatus": "https://schema.org/ReservationConfirmed", "underName": { "@type": "Person", "name": "John Smith" }, "reservationFor": { "@type": "Car", "name": "Economy Class Car", "model": "Civic", "brand": { "@type": "Brand", "name": "Honda" } }, "provider": { "@type": "Organization", "name": "Hertz" }, "pickupLocation": { "@type": "Place", "name": "Hertz San Diego Airport", "address": { "@type": "PostalAddress", "streetAddress": "1500 Orange Avenue", "addressLocality": "San Diego", "addressRegion": "CA", "postalCode": "94043", "addressCountry": "US" } }, "pickupTime": "2017-08-05T16:00:00-07:00", "dropoffLocation": { "@type": "Place", "name": "Hertz LAX", "address": { "@type": "PostalAddress", "streetAddress": "1234 First Street", "addressLocality": "Los Angeles", "addressRegion": "CA", "postalCode": "94043", "addressCountry": "US" } }, "dropoffTime": "2017-08-06T20:00:00-07:00" } </script>

Structured representation of the JSON-LD example.
