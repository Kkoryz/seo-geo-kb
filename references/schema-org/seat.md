---
title: "Seat"
source_url: https://schema.org/Seat
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2017-03-06
---

# Seat

# Seat

A Schema.org Type

- Canonical URL: https://schema.org/Seat
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Seat)

Used to describe a seat, such as a reserved seat in an event reservation.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[seatNumber](/seatNumber)

[Text](/Text)```
```[seatRow](/seatRow)

[Text](/Text)```
```[seatSection](/seatSection)

[Text](/Text)```
```[seatingType](/seatingType)

[QualitativeValue](/QualitativeValue)or[Text](/Text)[Thing](/Thing)

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

[Seat](/Seat)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Ticket](/Ticket)### Examples

[Example 1](#eg-0180)

Copied

Example notes or example HTML without markup.

Original: Reservation #E123456789 under name: John Smith Foo Fighters Concert 2017-03-06T19:30:00-08:00 AT&T Park 24 Willie Mays Plaza San Francisco, CA 94107 Ticket #abc123 Section: 101 Row: A Seat: 12

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "EventReservation", "reservationId": "E123456789", "reservationStatus": "https://schema.org/ReservationConfirmed", "underName": { "@type": "Person", "name": "John Smith" }, "reservationFor": { "@type": "Event", "name": "Foo Fighters Concert", "startDate": "2017-03-06T19:30:00-08:00", "location": { "@type": "Place", "name": "AT&T Park", "address": { "@type": "PostalAddress", "streetAddress": "24 Willie Mays Plaza", "addressLocality": "San Francisco", "addressRegion": "CA", "postalCode": "94107", "addressCountry": "US" } } }, "reservedTicket": { "@type": "Ticket", "ticketNumber": "abc123", "ticketToken": "qrCode:AB34", "ticketedSeat": { "@type": "Seat", "seatRow": "A", "seatNumber": "12", "seatSection": "101" } } } </script>

Structured representation of the JSON-LD example.
