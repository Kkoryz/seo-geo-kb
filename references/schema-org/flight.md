---
title: "Flight"
source_url: https://schema.org/Flight
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2017-03-04
---

# Flight

# Flight

A Schema.org Type

- Canonical URL: https://schema.org/Flight
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Flight)

An airline flight.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[aircraft](/aircraft)

[Text](/Text)or[Vehicle](/Vehicle)```
```[arrivalAirport](/arrivalAirport)

[Airport](/Airport)```
```[arrivalGate](/arrivalGate)

[Text](/Text)```
```[arrivalTerminal](/arrivalTerminal)

[Text](/Text)```
```[boardingPolicy](/boardingPolicy)

[BoardingPolicyType](/BoardingPolicyType)```
```[departureAirport](/departureAirport)

[Airport](/Airport)```
```[departureGate](/departureGate)

[Text](/Text)```
```[departureTerminal](/departureTerminal)

[Text](/Text)```
```[estimatedFlightDuration](/estimatedFlightDuration)

[Duration](/Duration)or[Text](/Text)```
```[flightDistance](/flightDistance)

[Distance](/Distance)or[Text](/Text)```
```[flightNumber](/flightNumber)

[Text](/Text)```
```[mealService](/mealService)

[Text](/Text)```
```[seller](/seller)

[Organization](/Organization)or[Person](/Person)[vendor](/vendor),[merchant](/merchant).```
```[webCheckinTime](/webCheckinTime)

[DateTime](/DateTime)[Trip](/Trip)

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

[Example 1](#eg-0181)

Copied

Example notes or example HTML without markup.

Reservation #RXJ34P Passenger: Eva Green Flight: United Airlines Flight 110 Operated By: Continental Airlines Departing: San Francisco Airport (SFO) 2017-03-04T20:15:00-08:00 Arriving: John F. Kennedy International Airport (JFK) 2017-03-05T06:30:00-05:00 Passenger Sequence Number: ABC123 Boarding priority: FastTrack Boarding policy: zone-based Security screening: TSA PreCheck

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "FlightReservation", "reservationId": "RXJ34P", "reservationStatus": "https://schema.org/ReservationConfirmed", "passengerPriorityStatus": "Fast Track", "passengerSequenceNumber": "ABC123", "securityScreening": "TSA PreCheck", "underName": { "@type": "Person", "name": "Eva Green" }, "reservationFor": { "@type": "Flight", "flightNumber": "UA110", "provider": { "@type": "Airline", "name": "Continental", "iataCode": "CO", "boardingPolicy": "https://schema.org/ZoneBoardingPolicy" }, "seller": { "@type": "Airline", "name": "United", "iataCode": "UA" }, "departureAirport": { "@type": "Airport", "name": "San Francisco Airport", "iataCode": "SFO" }, "departureTime": "2017-03-04T20:15:00-08:00", "arrivalAirport": { "@type": "Airport", "name": "John F. Kennedy International Airport", "iataCode": "JFK" }, "arrivalTime": "2017-03-05T06:30:00-05:00" } } </script>

Structured representation of the JSON-LD example.
