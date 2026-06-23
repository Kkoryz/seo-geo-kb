---
title: "VirtualLocation"
source_url: https://schema.org/VirtualLocation
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# VirtualLocation

# VirtualLocation

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/VirtualLocation
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+VirtualLocation)

An online or virtual location for attending events. For example, one may attend an online seminar or educational event. While a virtual location may be used as the location of an event, virtual locations should not be confused with physical locations in the real world.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[VirtualLocation](/VirtualLocation)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Action](/Action)or[Event](/Event)or[InteractionCounter](/InteractionCounter)or[Organization](/Organization)#### Source

[https://github.com/schemaorg/schemaorg/issues/1842](https://github.com/schemaorg/schemaorg/issues/1842)

### Examples

[Example 1](#eg-0014)

Copied

Example notes or example HTML without markup.

Example of an online event.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ChildrensEvent", "name": "Story Time Reading", "startDate": "2020-07-24T16:00Z", "endDate": "2020-07-24T16:30Z", "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled", "location": { "@type": "VirtualLocation", "url": "https://stream.storytimereadings.com/" }, "image": "https://storytimereadings.com/photos/childrensphoto.jpg", "description": "Story Time readings for children of all ages - July 2020 edition", "offers": { "@type": "Offer", "url": "https://torytimereadings.com/event_offer/2020-07-24-free", "price": "0", "priceCurrency": "USD", "availability": "https://schema.org/InStock", "validFrom": "2020-07-01T12:00" }, "performer": { "@type": "Person", "name": "Darren R Story", "alternateName": "The Virtual Story Master" }, "organizer": { "@type": "Organization", "name": "Story Time Virtual Events", "url": "https://torytimereadings.com.com" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0170)

Copied

Example notes or example HTML without markup.

Example of a mixed online and offline event.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "name": "The Adventures of Kira and Morrison", "startDate": "2025-07-21T19:00-05:00", "endDate": "2025-07-21T23:00-05:00", "eventAttendanceMode": "https://schema.org/MixedEventAttendanceMode", "eventStatus": "https://schema.org/EventScheduled", "location": [{ "@type": "VirtualLocation", "url": "https://operaonline.stream5.com/" }, { "@type": "Place", "name": "Snickerpark Stadium", "address": { "@type": "PostalAddress", "streetAddress": "100 West Snickerpark Dr", "addressLocality": "Snickertown", "postalCode": "19019", "addressRegion": "PA", "addressCountry": "US" } }], "image": [ "https://example.com/photos/1x1/photo.jpg", "https://example.com/photos/4x3/photo.jpg", "https://example.com/photos/16x9/photo.jpg" ], "description": "The Adventures of Kira and Morrison is coming to Snickertown in a can’t miss performance.", "offers": { "@type": "Offer", "url": "https://www.example.com/event_offer/12345_201803180430", "price": "30", "priceCurrency": "USD", "availability": "https://schema.org/InStock", "validFrom": "2024-05-21T12:00" }, "performer": { "@type": "PerformingGroup", "name": "Kira and Morrison" }, "organizer": { "@type": "Organization", "name": "Kira and Morrison Music", "url": "https://kiraandmorrisonmusic.com" } } </script>

Structured representation of the JSON-LD example.
