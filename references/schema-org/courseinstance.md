---
title: "CourseInstance"
source_url: https://schema.org/CourseInstance
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# CourseInstance

# CourseInstance

A Schema.org Type

- Canonical URL: https://schema.org/CourseInstance
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+CourseInstance)

An instance of a

[Course](/Course)which is distinct from other instances because it is offered at a different time or location or through different media or modes of study or to a specific section of students.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[courseMode](/courseMode)

[Text](/Text)or[URL](/URL)```
```[courseSchedule](/courseSchedule)

[Schedule](/Schedule)[Schedule](/Schedule).```
```[courseWorkload](/courseWorkload)

[Text](/Text)```
```[instructor](/instructor)

[Person](/Person)[CourseInstance](/CourseInstance).[Event](/Event)

```
```[about](/about)

[Thing](/Thing)Inverse property:

[subjectOf](/subjectOf)```
```[actor](/actor)

[PerformingGroup](/PerformingGroup)or[Person](/Person)[actors](/actors).```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[attendee](/attendee)

[Organization](/Organization)or[Person](/Person)[attendees](/attendees).```
```[audience](/audience)

[Audience](/Audience)[serviceAudience](/serviceAudience).```
```[composer](/composer)

[Organization](/Organization)or[Person](/Person)```
```[contributor](/contributor)

[Organization](/Organization)or[Person](/Person)```
```[director](/director)

[Person](/Person)[directors](/directors).```
```[doorTime](/doorTime)

[DateTime](/DateTime)or[Time](/Time)```
```[duration](/duration)

[Duration](/Duration)or[QuantitativeValue](/QuantitativeValue)[ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).```
```[endDate](/endDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).```
```[eventAttendanceMode](/eventAttendanceMode)

[EventAttendanceModeEnumeration](/EventAttendanceModeEnumeration)```
```[eventSchedule](/eventSchedule)

[Schedule](/Schedule)[Event](/Event)with a[Schedule](/Schedule). There are circumstances where it is preferable to share a schedule for a series of repeating events rather than data on the individual events themselves. For example, a website or application might prefer to publish a schedule for a weekly gym class rather than provide data on every event. A schedule could be processed by applications to add forthcoming events to a calendar. An[Event](/Event)that is associated with a[Schedule](/Schedule)using this property should not have[startDate](/startDate)or[endDate](/endDate)properties. These are instead defined within the associated[Schedule](/Schedule), this avoids any ambiguity for clients using the data. The property might have repeated values to specify different schedules, e.g. for different months or seasons.```
```[eventStatus](/eventStatus)

[EventStatusType](/EventStatusType)```
```[funder](/funder)

[Organization](/Organization)or[Person](/Person)```
```[funding](/funding)

[Grant](/Grant)[Grant](/Grant)that directly or indirectly provide funding or sponsorship for this item. See also[ownershipFundingInfo](/ownershipFundingInfo).Inverse property:

[fundedItem](/fundedItem)```
```[hasParticipationOffer](/hasParticipationOffer)

[Offer](/Offer)```
```[hasSponsorshipOffer](/hasSponsorshipOffer)

[Offer](/Offer)```
```[inLanguage](/inLanguage)

[Language](/Language)or[Text](/Text)[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also[availableLanguage](/availableLanguage). Supersedes[language](/language).```
```[isAccessibleForFree](/isAccessibleForFree)

[Boolean](/Boolean)[free](/free).```
```[keywords](/keywords)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[location](/location)

[Place](/Place)or[PostalAddress](/PostalAddress)or[Text](/Text)or[VirtualLocation](/VirtualLocation)```
```[maximumAttendeeCapacity](/maximumAttendeeCapacity)

[Integer](/Integer)```
```[maximumPhysicalAttendeeCapacity](/maximumPhysicalAttendeeCapacity)

[Integer](/Integer)[Event](/Event)whose[eventAttendanceMode](/eventAttendanceMode)is[OfflineEventAttendanceMode](/OfflineEventAttendanceMode)(or the offline aspects, in the case of a[MixedEventAttendanceMode](/MixedEventAttendanceMode)).```
```[maximumVirtualAttendeeCapacity](/maximumVirtualAttendeeCapacity)

[Integer](/Integer)[Event](/Event)whose[eventAttendanceMode](/eventAttendanceMode)is[OnlineEventAttendanceMode](/OnlineEventAttendanceMode)(or the online aspects, in the case of a[MixedEventAttendanceMode](/MixedEventAttendanceMode)).```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[organizer](/organizer)

[Organization](/Organization)or[Person](/Person)```
```[performer](/performer)

[Organization](/Organization)or[Person](/Person)[performers](/performers).```
```[previousStartDate](/previousStartDate)

[Date](/Date)or[DateTime](/DateTime)```
```[recordedIn](/recordedIn)

[CreativeWork](/CreativeWork)Inverse property:

[recordedAt](/recordedAt)```
```[remainingAttendeeCapacity](/remainingAttendeeCapacity)

[Integer](/Integer)```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[sponsor](/sponsor)

[Organization](/Organization)or[Person](/Person)```
```[startDate](/startDate)

[Date](/Date)or[DateTime](/DateTime)[ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).```
```[subEvent](/subEvent)

[Event](/Event)[subEvents](/subEvents).Inverse property:

[superEvent](/superEvent)```
```[superEvent](/superEvent)

[Event](/Event)Inverse property:

[subEvent](/subEvent)```
```[translator](/translator)

[Organization](/Organization)or[Person](/Person)```
```[typicalAgeRange](/typicalAgeRange)

[Text](/Text)```
```[workFeatured](/workFeatured)

[CreativeWork](/CreativeWork)```
```[workPerformed](/workPerformed)

[CreativeWork](/CreativeWork)[Thing](/Thing)

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

[CourseInstance](/CourseInstance)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Course](/Course)### Examples

[Example 1](#eg-0332)

Copied

Example notes or example HTML without markup.

<body vocab="https://schema.org/"> <!-- A MOOC / free online course. As a simple one-off course --> <!-- Based on https://www.coursera.org/course/datascitoolbox --> <main> <h1>The Data Scientist's Toolbox</h1> <h2>About this Course</h2> <p>In this course you will get an introduction to the main tools and ideas in the data scientist's toolbox...</p> <div> <h2>Session dates</h2> <span>February 15</span> - <span>March 21</span> </div> </main> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/"> <!-- A MOOC / free online course. As a simple one-off course --> <!-- Based on https://www.coursera.org/course/datascitoolbox --> <main typeof="Course"> <h1 property="name">The Data Scientist's Toolbox</h1> <h2>About this Course</h2> <p property="description"> In this course you will get an introduction to the main tools and ideas in the data scientist's toolbox...</p> <div rel="hasCourseInstance" typeof="CourseInstance"> <meta property="courseMode" content="MOOC" /> <meta property="courseMode" content="online" /> <h2>Session dates</h2> <span property="startDate" content="2019-02-15">February 15</span> - <span property="endDate" content="2019-03-21">March 21</span> </div> </main> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Course", "description": "In this course you will get an introduction to the main tools and ideas in the data scientist's toolbox...", "hasCourseInstance": { "@type": "CourseInstance", "courseMode": ["MOOC","online"], "endDate": "2019-03-21", "startDate": "2019-02-15" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0333)

Copied

Example notes or example HTML without markup.

<body vocab="https://schema.org/" typeof="Course"> <!-- A college course offered at several locations --> <!-- based on http://www.fife.ac.uk/student/courses/course/HCACC --> <h1>Course Details</h1> <h2>HNC Accounting</h2> <p>This course is designed for those wishing to take up a career in Accounting and Financial Administration within a range of organisations....</p> <h2>This course is currently offered on the date(s) and venue(s) listed below.</h2> <table > <tbody> <tr > <th scope="col" >Method of Study</th> <th scope="col" >Starts</th> <th scope="col" >Ends</th> <th scope="col" >Based at</th> </tr> <tr> <td>Full-time</td> <td>29 Aug 2016</td> <td>23 Jun 2017</td> <td>St Brycedale Campus Kirkcaldy</td> </tr> <tr> <td>Full-time</td> <td>29 Aug 2016</td> <td>23 Jun 2017</td> <td>Halbeath Campus Dunfermline</td> </tr> <tr> <td>Evenings only and weekends</td> <td>31 Aug 2016</td> <td>21 Jun 2017</td> <td>St Brycedale Campus Kirkcaldy</td> </tr> </tbody> </table> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/" typeof="Course"> <!-- A college course offered at several locations --> <!-- based on http://www.fife.ac.uk/student/courses/course/HCACC --> <h1>Course Details</h1> <h2 property="name">HNC Accounting</h2> <p property="description">This course is designed for those wishing to take up a career in Accounting and Financial Administration within a range of organisations....</p> <h2>This course is currently offered on the date(s) and venue(s) listed below.</h2> <table > <tbody> <tr > <th scope="col" >Method of Study</th> <th scope="col" >Starts</th> <th scope="col" >Ends</th> <th scope="col" >Based at</th> </tr> <tr rel="hasCourseInstance" typeof="CourseInstance"> <td property="courseMode">full-time</td> <td property="startDate" content="2016-08-29" datatype="schema:date">29 Aug 2016</td> <td property="endDate" content="2017-06-23" datatype="schema:date">23 Jun 2017</td> <td property="location">St Brycedale Campus Kirkcaldy</td> </tr> <tr rel="hasCourseInstance" typeof="CourseInstance"> <td property="courseMode">full-time</td> <td property="startDate" content="2016-08-29" datatype="schema:date">29 Aug 2016</td> <td property="endDate" content="2017-06-23" datatype="schema:date">23 Jun 2017</td> <td property="location">Halbeath Campus Dunfermline</td> </tr> <tr rel="hasCourseInstance" typeof="CourseInstance"> <td><meta property="courseMode" content="part-time"> Evenings only and weekends</td> <td property="startDate" content="2016-08-31" datatype="schema:date">31 Aug 2016</td> <td property="endDate" content="2017-06-21" datatype="schema:date">21 Jun 2017</td> <td property="location">St Brycedale Campus Kirkcaldy</td> </tr> </tbody> </table> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@id": "./", "@type": "Course", "name": "HNC Accounting", "description": "This course is designed for those wishing to take up \r\n a career in Accounting and Financial Administration within a range of \r\n organisations....", "hasCourseInstance": [ { "@type": "CourseInstance", "courseMode": "part-time", "endDate": "2017-06-21", "location": "St Brycedale Campus Kirkcaldy", "startDate": "2016-08-31" }, { "@type": "CourseInstance", "courseMode": "full-time", "endDate": "2017-06-23", "location": "Halbeath Campus Dunfermline", "startDate": "2016-08-29" }, { "courseMode": "full-time", "endDate": "2017-06-23", "location": "St Brycedale Campus Kirkcaldy", "startDate": "2016-08-29" } ] } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0334)

Copied

Example notes or example HTML without markup.

<body> <!--A self-paced distance learning course (no events)--> <!--Based on http://www.train4publishing.co.uk/courses/distance-learning/basic-proofreading --> <div> <h1>Basic Proofreading</h1> <p>The distance learning training course that takes you from complete beginner to PQB qualified proofreader in one step.</p> <div> Online, cost: £395 </div> <div> Posted, cost:£440 </div> </div> </body>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<body vocab="https://schema.org/"> <!--A self-paced distance learning course (no events)--> <!--Based on http://www.train4publishing.co.uk/courses/distance-learning/basic-proofreading --> <div typeof="Course"> <h1 property="name">Basic Proofreading</h1> <p property="description">The distance learning training course that takes you from complete beginner to PQB qualified proofreader in one step.</p> <div rel="hasCourseInstance" typeof="CourseInstance"> <meta property="courseMode" content="distance learning" /> <span property="courseMode">Online</span>, <div rel="offers" typeof="Offer"> cost:<meta property="priceCurrency" content="GBP" /> £<span property="price">395</span> </div> </div> <div rel="hasCourseInstance" typeof="CourseInstance"> <meta property="courseMode" content="distance learning" /> <span property="courseMode">Posted</span>, <div rel="offers" typeof="Offer"> cost:<meta property="priceCurrency" content="GBP" /> £<span property="price">440</span> </div> </div> </div> </body>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Course", "name": "Basic Proofreading", "description": "The distance learning training course that takes you \r\n from complete beginner to PQB qualified proofreader in one step.", "hasCourseInstance": [ { "@type": "CourseInstance", "courseMode": [ "distance learning", "Online" ], "offers": { "@type": "Offer", "price": "395", "priceCurrency": "GBP" } }, { "@type": "CourseInstance", "courseMode": [ "Posted", "distance learning" ], "offers": { "@type": "Offer", "price": "440", "priceCurrency": "GBP" } } ] } </script>

Structured representation of the JSON-LD example.
