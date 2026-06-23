---
title: "eventSchedule"
source_url: https://schema.org/eventSchedule
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# eventSchedule

# eventSchedule

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/eventSchedule
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+eventSchedule)

Associates an

[Event](/Event)with a[Schedule](/Schedule). There are circumstances where it is preferable to share a schedule for a series of repeating events rather than data on the individual events themselves. For example, a website or application might prefer to publish a schedule for a weekly gym class rather than provide data on every event. A schedule could be processed by applications to add forthcoming events to a calendar. An[Event](/Event)that is associated with a[Schedule](/Schedule)using this property should not have[startDate](/startDate)or[endDate](/endDate)properties. These are instead defined within the associated[Schedule](/Schedule), this avoids any ambiguity for clients using the data. The property might have repeated values to specify different schedules, e.g. for different months or seasons.### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1457](https://github.com/schemaorg/schemaorg/issues/1457)

### Examples

[Example 1](#eg-0240)

Copied

Example notes or example HTML without markup.

A Tai-Chi class runs throughout 2017. The class occurs weekly, every Wednesday at 7pm.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Event", "url": "http://www.example.org/events/1", "name": "Tai chi Class", "description": "A weekly Tai-Chi class", "duration": "PT60M", "eventSchedule": { "@type": "Schedule", "startDate": "2017-01-01", "endDate": "2017-12-31", "repeatFrequency": "P1W", "byDay": "https://schema.org/Wednesday", "startTime": "19:00:00", "endTime": "20:00:00", "scheduleTimezone": "Europe/London" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0241)

Copied

Example notes or example HTML without markup.

A Meetup takes place on the 1st and 15th of every month between 9-10am

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Event", "name": "Example Meetup", "eventSchedule": { "@type": "Schedule", "repeatFrequency": "P1M", "byMonthDay": [1,15], "startTime": "09:00:00", "endTime": "10:00:00", "scheduleTimezone": "America/Glace_Bay" } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0242)

Copied

Example notes or example HTML without markup.

Starting from 2th December an Event will run daily between 9-10am for 10 occurences.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "name": "Count Example", "eventSchedule": { "@type": "Schedule", "startDate": "2016-12-24", "repeatFrequency": "P1D", "repeatCount": 10, "startTime": "09:00:00", "endTime": "10:00:00", "scheduleTimezone": "Europe/London" } } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0243)

Copied

Example notes or example HTML without markup.

An Event runs twice a day, at 9am-10am and 2pm-3pm but only Monday to Friday

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "name": "Example", "eventSchedule": [ { "@type": "Schedule", "repeatFrequency": "P1D", "byDay": [ "https://schema.org/Monday", "https://schema.org/Tuesday", "https://schema.org/Wednesday", "https://schema.org/Thursday", "https://schema.org/Friday" ], "startTime": "09:00:00", "endTime": "10:00:00", "scheduleTimezone": "America/Glace_Bay" }, { "@type": "Schedule", "repeatFrequency": "P1D", "byDay": [ "https://schema.org/Monday", "https://schema.org/Tuesday", "https://schema.org/Wednesday", "https://schema.org/Thursday", "https://schema.org/Friday" ], "startTime": "14:00:00", "endTime": "15:00:00", "scheduleTimezone": "America/Glace_Bay" } ] } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0244)

Copied

Example notes or example HTML without markup.

An Event runs on the second Monday of every month, from 6pm-7:30pm. Because this kind of recurrence goes beyond that expressible using <a href="https://schema.org/DayOfWeek">https://schema.org/DayOfWeek</a>, it is specified instead using iCal's <a href="https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html">syntax for byDay recurrence rules</a>.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "name": "Example", "eventSchedule": [ { "@type": "Schedule", "repeatFrequency": "P1M", "byDay": "2MO", "startTime": "18:00:00", "endTime": "19:30:00", "scheduleTimezone": "Asia/Shanghai" } ] } </script>

Structured representation of the JSON-LD example.
