---
title: "EventRescheduled"
source_url: https://schema.org/EventRescheduled
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# EventRescheduled

# EventRescheduled

A Schema.org Enumeration Member

- Canonical URL: https://schema.org/EventRescheduled
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+EventRescheduled)

The event has been rescheduled. The event's previousStartDate should be set to the old date and the startDate should be set to the event's new date. (If the event has been rescheduled multiple times, the previousStartDate property may be repeated.)

A member value for enumeration type:

[EventStatusType](/EventStatusType)

### Examples

[Example 1](#eg-0202)

Copied

Example notes or example HTML without markup.

An example of a more fully specified MusicEvent, including a tour image, full venue address, multiple performers, and multiple ticket classes.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> [{ "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King with Jonathon \"Boogie\" Long", "image" : "http://www.bbking.com/gallery/b-b-king-live.jpg", "url" : "http://www.bbking.com/events/apr12-providence.html", "startDate" : "2014-04-12T19:30", "doorTime" : "18:30:00", "endDate" : "2014-04-12T22:00", "location" : { "@type" : "Place", "name" : "Lupo's Heartbreak Hotel", "sameAs" : "http://lupos.com/", "address" : { "@type" : "PostalAddress", "streetAddress" : "79 Washington St.", "addressLocality" : "Providence", "addressRegion" : "RI", "postalCode" : "02903", "addressCountry" : "US" } }, "offers" : [ { "@type" : "Offer", "name" : "General Admission", "priceCurrency": "USD", "price" : "63.25", "availability" : "SoldOut", "url" : "http://www.ticketmaster.com/event/17004C29" },{ "@type" : "Offer", "name" : "VIP Experience", "url" : "http://www.example.com/Abcde12345", "priceCurrency": "USD", "price" : "299.00", "validFrom" : "2014-02-05T10:00", "validThrough" : "2014-03-19T23:59" } ], "performer" : [ { "@type" : "MusicGroup", "name" : "B.B. King", "sameAs" : "http://en.wikipedia.org/wiki/B.B._King" },{ "@type" : "MusicGroup", "name" : "Jonathon \"Boogie\" Long", "sameAs" : "http://jonathonboogielong.com/" } ], "eventStatus" : "EventRescheduled", "previousStartDate" : "2013-09-30T19:30", "typicalAgeRange" : "18+" }] </script>

Structured representation of the JSON-LD example.
