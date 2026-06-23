---
title: "OpeningHoursSpecification"
source_url: https://schema.org/OpeningHoursSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# OpeningHoursSpecification

# OpeningHoursSpecification

A Schema.org Type

- Canonical URL: https://schema.org/OpeningHoursSpecification
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+OpeningHoursSpecification)

A structured value providing information about the opening hours of a place or a certain service inside a place.


The place is


If the value for the

The place is

**open**if the[opens](/opens)property is specified, and**closed**otherwise.If the value for the

[closes](/closes)property is less than the value for the[opens](/opens)property then the hour range is assumed to span over the next day.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[closes](/closes)

[Time](/Time)```
```[dayOfWeek](/dayOfWeek)

[DayOfWeek](/DayOfWeek)```
```[opens](/opens)

[Time](/Time)```
```[validFrom](/validFrom)

[Date](/Date)or[DateTime](/DateTime)```
```[validThrough](/validThrough)

[Date](/Date)or[DateTime](/DateTime)[Thing](/Thing)

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

[OpeningHoursSpecification](/OpeningHoursSpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ServicePeriod](/ServicePeriod)or[ShippingDeliveryTime](/ShippingDeliveryTime)[hoursAvailable](/hoursAvailable)

[ContactPoint](/ContactPoint)or[LocationFeatureSpecification](/LocationFeatureSpecification)or[Service](/Service)[openingHoursSpecification](/openingHoursSpecification)

[Place](/Place)[seasonalOverride](/seasonalOverride)

[ShippingConditions](/ShippingConditions)[specialOpeningHoursSpecification](/specialOpeningHoursSpecification)

[Place](/Place)Use this to explicitly override general opening hours brought in scope by

[openingHoursSpecification](/openingHoursSpecification)or[openingHours](/openingHours).### Examples

[Example 1](#eg-0193)

Copied

Example notes or example HTML without markup.

<div> <h1>Middle of Nowhere Foods</h1> <h2>Opening hours</h2> <p>Normally open daily <time datetime="09:00:00">9am</time>-<time datetime="14:00:00">2pm</time> except on:</p> <ul> <li> <time datetime="2013-12-24">24 December 2013</time> and <time datetime="2013-12-25">25 December 2013</time>: <time datetime="09:00:00">9am</time>-<time datetime="11:00:00">11am</time> </li> <li> <time datetime="2014-01-01">1st January 2014</time>: <time datetime="12:00:00">Noon</time>-<time datetime="14:00:00">2pm</time> </li> </ul> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Store"> <h1 itemprop="name">Middle of Nowhere Foods</h1> <h2>Opening hours</h2> <meta itemprop="openingHours" content="Mo,Tu,We,Th,Fr,Sa,Su 09:00-14:00"> <p>Normally open daily <time datetime="09:00:00">9am</time>-<time datetime="14:00:00">2pm</time> except on:</p> <ul> <li itemprop="openingHoursSpecification" itemscope itemtype="https://schema.org/OpeningHoursSpecification"> <time itemprop="validFrom" datetime="2013-12-24">24 December 2013</time> and <time itemprop="validThrough" datetime="2013-12-25">25 December 2013</time>: <time itemprop="opens" datetime="09:00:00">9am</time>-<time itemprop="closes" datetime="11:00:00">11am</time> </li> <li itemprop="openingHoursSpecification" itemscope itemtype="https://schema.org/OpeningHoursSpecification"> <time itemprop="validFrom validThrough" datetime="2014-01-01">1st January 2014</time>: <time itemprop="opens" datetime="12:00:00">Noon</time>-<time itemprop="closes" datetime="14:00:00">2pm</time> </li> </ul> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Store"> <h1 property="name">Middle of Nowhere Foods</h1> <h2>Opening hours</h2> <meta property="openingHours" content="Mo,Tu,We,Th,Fr,Sa,Su 09:00-14:00"> <p>Normally open daily <time datetime="09:00:00">9am</time>-<time datetime="14:00:00">2pm</time> except on:</p> <ul> <li property="openingHoursSpecification" typeof="OpeningHoursSpecification"> <time property="validFrom" datetime="2013-12-24">24 December 2013</time> and <time property="validThrough" datetime="2013-12-25">25 December 2013</time>: <time property="opens" datetime="09:00:00">9am</time>-<time property="closes" datetime="11:00:00">11am</time> </li> <li property="openingHoursSpecification" typeof="OpeningHoursSpecification"> <time property="validFrom validThrough" datetime="2014-01-01">1st January 2014</time>: <time property="opens" datetime="12:00:00">Noon</time>-<time property="closes" datetime="14:00:00">2pm</time> </li> </ul> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Store", "name": "Middle of Nowhere Foods", "openingHours": "Mo,Tu,We,Th,Fr,Sa,Su 09:00-14:00", "openingHoursSpecification": [ { "@type": "OpeningHoursSpecification", "validFrom": "2013-12-24", "validThrough": "2013-12-25", "opens": "09:00:00", "closes": "11:00:00" }, { "@type": "OpeningHoursSpecification", "validFrom": "2014-01-01", "validThrough": "2014-01-01", "opens": "12:00:00", "closes": "14:00:00" } ] } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0378)

Copied

Example notes or example HTML without markup.

<div> <h1>Music Resource Centre</h1> <h2>Opening hours</h2> <div>Monday: <time> 9:00 AM</time> - <time> 5:00 PM</time></div> <div>Tuesday: <time> 9:00 AM</time> - <time> 5:00 PM</time></div> <div>Wednesday: <time> 9:00 AM</time> - <time> 5:00 PM</time></div> <div>Thursday: <time> 9:00 AM</time> - <time> 5:00 PM</time></div> <div>Friday: <time> 9:00 AM</time> - <time> 5:00 PM</time></div> <div>Saturday: <time> 9:00 AM</time> - <time> 5:00 PM</time></div> <div>Sunday: <time> 9:00 AM</time> - <time> 5:00 PM</time></div> <h2 >Contact information</h2> <div>Email address: <a href="mailto:dscott@laurentian.ca">dscott@laurentian.ca</a></div> <div> <div> <h3>Mailing address</h3> School of Education - Music Resource Centre<br />Laurentian University<br /> Sudbury<br /> ON<br /> Canada<br /> P3E 2C6<br /> </div> </div> <h2>Branch relationship</h2> <div>Parent library: <a href="/eg/opac/library/LUSYS">Laurentian University</a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Library"> <h1 itemprop="name"> Music Resource Centre </h1> <h2> Opening hours </h2> <div itemprop="openingHoursSpecification" itemscope itemtype="https://schema.org/OpeningHoursSpecification"> <link itemprop="dayOfWeek" href="https://schema.org/Monday">Monday: <time itemprop="opens" content="09:00:00">9:00 AM</time> - <time itemprop="closes" content="17:00:00">5:00 PM</time> </div> <div itemprop="openingHoursSpecification" itemscope itemtype="https://schema.org/OpeningHoursSpecification"> <link itemprop="dayOfWeek" href="https://schema.org/Tuesday">Tuesday: <time itemprop="opens" content="09:00:00">9:00 AM</time> - <time itemprop="closes" content="17:00:00">5:00 PM</time> </div> <div itemprop="openingHoursSpecification" itemscope itemtype="https://schema.org/OpeningHoursSpecification"> <link itemprop="dayOfWeek" href="https://schema.org/Wednesday">Wednesday: <time itemprop="opens" content="09:00:00">9:00 AM</time> - <time itemprop="closes" content="17:00:00">5:00 PM</time> </div> <div itemprop="openingHoursSpecification" itemscope itemtype="https://schema.org/OpeningHoursSpecification"> <link itemprop="dayOfWeek" href="https://schema.org/Thursday">Thursday: <time itemprop="opens" content="09:00:00">9:00 AM</time> - <time itemprop="closes" content="17:00:00">5:00 PM</time> </div> <div itemprop="openingHoursSpecification" itemscope itemtype="https://schema.org/OpeningHoursSpecification"> <link itemprop="dayOfWeek" href="https://schema.org/Friday">Friday: <time itemprop="opens" content="09:00:00">9:00 AM</time> - <time itemprop="closes" content="17:00:00">5:00 PM</time> </div> <div itemprop="openingHoursSpecification" itemscope itemtype="https://schema.org/OpeningHoursSpecification"> <link itemprop="dayOfWeek" href="https://schema.org/Saturday">Saturday: <time itemprop="opens" content="09:00:00">9:00 AM</time> - <time itemprop="closes" content="17:00:00">5:00 PM</time> </div> <div itemprop="openingHoursSpecification" itemscope itemtype="https://schema.org/OpeningHoursSpecification"> <link itemprop="dayOfWeek" href="https://schema.org/Sunday">Sunday: <time itemprop="opens" content="09:00:00">9:00 AM</time> - <time itemprop="closes" content="17:00:00">5:00 PM</time> </div> <h2> Contact information </h2> <div> Email address: <a href="mailto:dscott@laurentian.ca" itemprop="email">dscott@laurentian.ca</a> </div> <div> <div itemprop="location address" itemscope itemtype="https://schema.org/PostalAddress"> <h3 itemprop="contactType"> Mailing address </h3><span itemprop="streetAddress">School of Education - Music Resource Centre<br> Laurentian University</span><br> <span itemprop="addressLocality">Sudbury</span><br> <span itemprop="addressRegion">ON</span><br> <span itemprop="addressCountry">Canada</span><br> <span itemprop="postalCode">P3E 2C6</span><br> </div> </div> <h2> Branch relationship </h2> <div> Parent library: <a itemprop="parentOrganization" href="/eg/opac/library/LUSYS">Laurentian University</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Library"> <h1 property="name"> Music Resource Centre </h1> <h2> Opening hours </h2> <div property="openingHoursSpecification" typeof="OpeningHoursSpecification"> <link property="dayOfWeek" href="https://schema.org/Monday">Monday: <time property="opens" content="09:00:00">9:00 AM</time> - <time property="closes" content="17:00:00">5:00 PM</time> </div> <div property="openingHoursSpecification" typeof="OpeningHoursSpecification"> <link property="dayOfWeek" href="https://schema.org/Tuesday">Tuesday: <time property="opens" content="09:00:00">9:00 AM</time> - <time property="closes" content="17:00:00">5:00 PM</time> </div> <div property="openingHoursSpecification" typeof="OpeningHoursSpecification"> <link property="dayOfWeek" href="https://schema.org/Wednesday">Wednesday: <time property="opens" content="09:00:00">9:00 AM</time> - <time property="closes" content="17:00:00">5:00 PM</time> </div> <div property="openingHoursSpecification" typeof="OpeningHoursSpecification"> <link property="dayOfWeek" href="https://schema.org/Thursday">Thursday: <time property="opens" content="09:00:00">9:00 AM</time> - <time property="closes" content="17:00:00">5:00 PM</time> </div> <div property="openingHoursSpecification" typeof="OpeningHoursSpecification"> <link property="dayOfWeek" href="https://schema.org/Friday">Friday: <time property="opens" content="09:00:00">9:00 AM</time> - <time property="closes" content="17:00:00">5:00 PM</time> </div> <div property="openingHoursSpecification" typeof="OpeningHoursSpecification"> <link property="dayOfWeek" href="https://schema.org/Saturday">Saturday: <time property="opens" content="09:00:00">9:00 AM</time> - <time property="closes" content="17:00:00">5:00 PM</time> </div> <div property="openingHoursSpecification" typeof="OpeningHoursSpecification"> <link property="dayOfWeek" href="https://schema.org/Sunday">Sunday: <time property="opens" content="09:00:00">9:00 AM</time> - <time property="closes" content="17:00:00">5:00 PM</time> </div> <h2> Contact information </h2> <div> Email address: <a href="mailto:dscott@laurentian.ca" property="email">dscott@laurentian.ca</a> </div> <div> <div property="location address" typeof="PostalAddress"> <h3 property="contactType"> Mailing address </h3><span property="streetAddress">School of Education - Music Resource Centre<br> Laurentian University</span><br> <span property="addressLocality">Sudbury</span><br> <span property="addressRegion">ON</span><br> <span property="addressCountry">Canada</span><br> <span property="postalCode">P3E 2C6</span><br> </div> </div> <h2> Branch relationship </h2> <div> Parent library: <a property="parentOrganization" href="/eg/opac/library/LUSYS">Laurentian University</a> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": [ "https://schema.org", { "@language": "en-ca" } ], "@type": "Library", "address": { "@id": "_:school_edu_library_1", "@type": "PostalAddress", "addressCountry": "Canada", "addressLocality": "Sudbury", "addressRegion": "ON", "contactType": "Mailing address", "postalCode": "P3E 2C6", "streetAddress": "School of Education - Music Resource Centre Laurentian University" }, "email": "mailto:dscott@laurentian.ca", "location": { "@id": "_:school_edu_library_1" }, "name": "Music Resource Centre", "parentOrganization": "https://laurentian.concat.ca/eg/opac/library/LUSYS", "openingHoursSpecification": [ { "@type": "OpeningHoursSpecification", "closes": "17:00:00", "dayOfWeek": "https://schema.org/Sunday", "opens": "09:00:00" }, { "@type": "OpeningHoursSpecification", "closes": "17:00:00" , "dayOfWeek": "https://schema.org/Saturday", "opens": "09:00:00" }, { "@type": "OpeningHoursSpecification", "closes": "17:00:00", "dayOfWeek": "https://schema.org/Thursday", "opens": "09:00:00" }, { "@type": "OpeningHoursSpecification", "closes": "17:00:00", "dayOfWeek": "https://schema.org/Tuesday", "opens": "09:00:00" }, { "@type": "OpeningHoursSpecification", "closes": "17:00:00", "dayOfWeek": "https://schema.org/Friday", "opens": "09:00:00" }, { "@type": "OpeningHoursSpecification", "closes": "17:00:00", "dayOfWeek": "https://schema.org/Monday", "opens": "09:00:00" }, { "@type": "OpeningHoursSpecification", "closes": "17:00:00", "dayOfWeek": "https://schema.org/Wednesday", "opens": "09:00:00" } ] } </script>

Structured representation of the JSON-LD example.
