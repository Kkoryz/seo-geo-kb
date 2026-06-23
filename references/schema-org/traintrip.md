---
title: "TrainTrip"
source_url: https://schema.org/TrainTrip
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2017-01-04
---

# TrainTrip

# TrainTrip

A Schema.org Type

- Canonical URL: https://schema.org/TrainTrip
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+TrainTrip)

A trip on a commercial train line.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[arrivalPlatform](/arrivalPlatform)

[Text](/Text)```
```[arrivalStation](/arrivalStation)

[TrainStation](/TrainStation)```
```[departurePlatform](/departurePlatform)

[Text](/Text)```
```[departureStation](/departureStation)

[TrainStation](/TrainStation)```
```[trainName](/trainName)

[Text](/Text)```
```[trainNumber](/trainNumber)

[Text](/Text)[Trip](/Trip)

```
```[arrivalTime](/arrivalTime)

[DateTime](/DateTime)or[Time](/Time)```
```[departureTime](/departureTime)

[DateTime](/DateTime)or[Time](/Time)```
```[itinerary](/itinerary)

[ItemList](/ItemList)or[Place](/Place)[Place](/Place)) that make up a trip. For a trip where destination order is important use[ItemList](/ItemList)to specify that order (see examples).```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[partOfTrip](/partOfTrip)

[Trip](/Trip)[Trip](/Trip)is a subTrip of another Trip. For example Day 1, Day 2, etc. of a multi-day trip.Inverse property:

[subTrip](/subTrip)```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[subTrip](/subTrip)

[Trip](/Trip)[Trip](/Trip)that is a subTrip of this Trip. For example Day 1, Day 2, etc. of a multi-day trip.Inverse property:

[partOfTrip](/partOfTrip)```
```[tripOrigin](/tripOrigin)

[Place](/Place)[Thing](/Thing)

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

[Example 1](#eg-0178)

Copied

Example notes or example HTML without markup.

Original: Train Reservation #AB3XY2 Departing: Munich Central 2017-01-04T10:30:00+01:00 Arriving: Paris Gare De Lyon 2017-01-04T03:10:00+01:00 Passenger: Eva Green Seat: 27B Seating: 1st Class Ticket: 123XYZ Ticket Token: aztecCode:AB34 We recommend that you arrive at the station at least 30 minutes prior to your scheduled departure. Allow additional time if you need help with baggage or tickets."

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "TrainReservation", "reservationId": "AB3XY2", "reservationStatus": "https://schema.org/ReservationConfirmed", "reservationFor": { "@type": "TrainTrip", "departureStation": { "@type": "TrainStation", "name": "Munich Central" }, "departureTime": "2017-01-04T10:30:00+01:00", "arrivalStation": { "@type": "TrainStation", "name": "Paris Gare De Lyon" }, "arrivalTime": "2017-01-04T03:10:00+01:00" }, "reservedTicket": { "@type": "Ticket", "underName": "Eva Green", "ticketedSeat": { "@type": "Seat", "seatNumber": "27B", "seatingType": "1st Class" }, "ticketNumber": "123XYZ", "ticketToken": "aztecCode:AB34", "description": "We recommend that you arrive at the station at least 30 minutes prior to your scheduled departure. Allow additional time if you need help with baggage or tickets." } } </script>

Structured representation of the JSON-LD example.
