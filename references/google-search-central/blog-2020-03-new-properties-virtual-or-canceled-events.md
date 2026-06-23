---
title: "New properties for virtual, postponed, and canceled events | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2020/03/new-properties-virtual-or-canceled-events
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2020-03-17
---

# New properties for virtual, postponed, and canceled events | Google Search Central Blog | Google for Developers

Tuesday, March 17, 2020

In the current environment and status of COVID-19 around the world, many events are being
canceled, postponed, or moved to an online-only format. Google wants to show users the latest,
most accurate information about your events in this fast-changing environment, and so we've
added some new, optional properties to our
[developer documentation](/search/docs/appearance/structured-data/event)
to help. These properties apply to all regions and languages. This is one part of our overall efforts in
[schema updates](https://blog.schema.org/2020/03/schema-for-coronavirus-special) to
support publishers and users. Here are some important tips on keeping Google up to date on your events.

## Update the status of the event

The schema.org `eventStatus`

property sets the status of the event, particularly when the event has been canceled, postponed,
or rescheduled. This information is helpful because it allows Google to show users the current
status of an event, instead of dropping the event from the event search experience altogether.

-
**If the event has been canceled**: Set theproperty to`eventStatus`

and keep the original date in the`EventCancelled`

of the event.`startDate`

-
**If the event has been postponed (but the date isn't known yet)**: Keep the original date in theof the event until you know when the event will take place and update the`startDate`

to`eventStatus`

. The`EventPostponed`

property is required to help identify the unique event, and we need the date original`startDate`

until you know the new date. Once you know the new date information, change the`startDate`

`eventStatus`

toand update the`EventRescheduled`

and`startDate`

with the new date information.`endDate`

-
**If the event has been rescheduled to a later date**: Update theand`startDate`

with the relevant new dates. Optionally, you can also mark the`endDate`

field as`eventStatus`

and add the`EventRescheduled`

.`previousStartDate`

-
**If the event has moved from in-person to online-only**: Optionally update thefield to indicate the change with`eventStatus`

`EventMovedOnline`

.

For more information on how to implement the `eventStatus`

property, refer to the
[developer documentation](/search/docs/appearance/structured-data/event#eventstatus).

## Mark events as online only

More events are shifting to online only, and we're actively working on a way to show this information to people on Google Search. If your event is happening only online, make sure to use the following properties:

-
Set the location to the
type.`VirtualLocation`

-
Set the
property to`eventAttendanceMode`

.`OnlineEventAttendanceMode`


For more information on how to implement the `VirtualLocation`

type,
refer to the [developer documentation](/search/docs/appearance/structured-data/event#virtual-location).

## Update Google when your event changes

After you make changes to your markup, make sure you
[update Google](/search/docs/guides/submit-URLs). We recommend that you
[make your sitemap available automatically
through your server](https://www.youtube.com/watch?v=y0TPINzAVf0). This is the best way to make sure that your new and updated content is
highlighted to search engines as quickly as possible.

If you have any questions, let us know through the
[Webmasters forum](https://support.google.com/webmasters/community) or on
[Twitter](https://twitter.com/googlesearchc).
