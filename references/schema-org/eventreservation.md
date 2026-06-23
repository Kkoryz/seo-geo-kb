---
title: "EventReservation"
source_url: https://schema.org/EventReservation
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2017-03-06
---

# EventReservation

# EventReservation

A Schema.org Type

- Canonical URL: https://schema.org/EventReservation
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+EventReservation)

A reservation for an event like a concert, sporting event, or lecture.


Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use

Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, use

[Offer](/Offer).| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[Example 1](#eg-0180)

Copied

Example notes or example HTML without markup.

Original: Reservation #E123456789 under name: John Smith Foo Fighters Concert 2017-03-06T19:30:00-08:00 AT&T Park 24 Willie Mays Plaza San Francisco, CA 94107 Ticket #abc123 Section: 101 Row: A Seat: 12

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "EventReservation", "reservationId": "E123456789", "reservationStatus": "https://schema.org/ReservationConfirmed", "underName": { "@type": "Person", "name": "John Smith" }, "reservationFor": { "@type": "Event", "name": "Foo Fighters Concert", "startDate": "2017-03-06T19:30:00-08:00", "location": { "@type": "Place", "name": "AT&T Park", "address": { "@type": "PostalAddress", "streetAddress": "24 Willie Mays Plaza", "addressLocality": "San Francisco", "addressRegion": "CA", "postalCode": "94107", "addressCountry": "US" } } }, "reservedTicket": { "@type": "Ticket", "ticketNumber": "abc123", "ticketToken": "qrCode:AB34", "ticketedSeat": { "@type": "Seat", "seatRow": "A", "seatNumber": "12", "seatSection": "101" } } } </script>

Structured representation of the JSON-LD example.
