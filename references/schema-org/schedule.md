---
title: "Schedule"
source_url: https://schema.org/Schedule
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Schedule

# Schedule

A Schema.org Type

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/Schedule
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Schedule)

A schedule defines a repeating time period used to describe a regularly occurring

[Event](/Event). At a minimum a schedule will specify[repeatFrequency](/repeatFrequency)which describes the interval between occurrences of the event. Additional information can be provided to specify the schedule more precisely. This includes identifying the day(s) of the week or month when the recurring event will take place, in addition to its start and end time. Schedules may also have start and end dates to indicate when they are active, e.g. to define a limited calendar of events.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[byDay](/byDay)

[DayOfWeek](/DayOfWeek)or[Text](/Text)[Event](/Event)takes place. May be specified using either[DayOfWeek](/DayOfWeek), or alternatively[Text](/Text)conforming to iCal's syntax for byDay recurrence rules.```
```[byMonth](/byMonth)

[Integer](/Integer)[Event](/Event)takes place. Specified as an[Integer](/Integer)between 1-12. January is 1.```
```[byMonthDay](/byMonthDay)

[Integer](/Integer)[Event](/Event)takes place. Specified as an[Integer](/Integer)between 1-31.```
```[byMonthWeek](/byMonthWeek)

[Integer](/Integer)```
```[duration](/duration)

[Duration](/Duration)or[QuantitativeValue](/QuantitativeValue)[ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).```
```[endDate](/endDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).```
```[endTime](/endTime)

[DateTime](/DateTime)or[Time](/Time)*December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

```
```[exceptDate](/exceptDate)

[Date](/Date)or[DateTime](/DateTime)[Date](/Date)or[DateTime](/DateTime)during which a scheduled[Event](/Event)will not take place. The property allows exceptions to a[Schedule](/Schedule)to be specified. If an exception is specified as a[DateTime](/DateTime)then only the event that would have started at that specific date and time should be excluded from the schedule. If an exception is specified as a[Date](/Date)then any event that is scheduled for that 24 hour period should be excluded from the schedule. This allows a whole day to be excluded from the schedule without having to itemise every scheduled event.```
```[repeatCount](/repeatCount)

[Integer](/Integer)[Event](/Event)will take place.```
```[repeatFrequency](/repeatFrequency)

[Duration](/Duration)or[Text](/Text)[Event](/Event)s will occur according to a schedule[Schedule](/Schedule). The intervals between events should be defined as a[Duration](/Duration)of time.```
```[scheduleTimezone](/scheduleTimezone)

[Text](/Text)[Schedule](/Schedule)are given. The value provided should be among those listed in the IANA Time Zone Database.```
```[startDate](/startDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).```
```[startTime](/startTime)

[DateTime](/DateTime)or[Time](/Time)*January*to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

[Thing](/Thing)

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

[Schedule](/Schedule)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[CourseInstance](/CourseInstance)[Schedule](/Schedule).[eventSchedule](/eventSchedule)

[Event](/Event)[Event](/Event)with a[Schedule](/Schedule). There are circumstances where it is preferable to share a schedule for a series of repeating events rather than data on the individual events themselves. For example, a website or application might prefer to publish a schedule for a weekly gym class rather than provide data on every event. A schedule could be processed by applications to add forthcoming events to a calendar. An[Event](/Event)that is associated with a[Schedule](/Schedule)using this property should not have[startDate](/startDate)or[endDate](/endDate)properties. These are instead defined within the associated[Schedule](/Schedule), this avoids any ambiguity for clients using the data. The property might have repeated values to specify different schedules, e.g. for different months or seasons.#### Source

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

[Example 6](#eg-0303)

Copied

Example notes or example HTML without markup.

A reading series occuring the first and third Wednesdays of the month.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "LiteraryEvent", "name": "Local Bookseller Author Night", "description": "Join us the first and third Wednesdays of each month for readings by local authors.", "eventSchedule": { "@type": "Schedule", "byDay": "https://schema.org/Wednesday", "byMonthWeek": [1, 3], "startTime": "20:00:00", "endTime": "22:00:00" } } </script>

Structured representation of the JSON-LD example.
