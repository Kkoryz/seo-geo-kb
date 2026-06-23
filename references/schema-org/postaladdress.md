---
title: "PostalAddress"
source_url: https://schema.org/PostalAddress
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# PostalAddress

# PostalAddress

A Schema.org Type

- Canonical URL: https://schema.org/PostalAddress
-
Equivalent Class: gs1:PostalAddress

Equivalent Class: cmns-loc:Address

Equivalent Class: unece:TradeAddress

Equivalent Class: fibo-fnd-plc-adr:PostalAddress [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+PostalAddress)

The mailing address.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[addressCountry](/addressCountry)

[Country](/Country)or[Text](/Text)[ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1)format, for example "US". For backward compatibility, a 3-letter[ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3)country code such as "SGP" or a full country name such as "Singapore" can also be used.```
```[addressLocality](/addressLocality)

[Text](/Text)```
```[addressRegion](/addressRegion)

[AdministrativeArea](/AdministrativeArea)or[Text](/Text)[Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country)such as the Province in Italy or Region in Germany.```
```[extendedAddress](/extendedAddress)

[Text](/Text)```
```[postOfficeBoxNumber](/postOfficeBoxNumber)

[Text](/Text)```
```[postalCode](/postalCode)

[Text](/Text)```
```[streetAddress](/streetAddress)

[Text](/Text)[ContactPoint](/ContactPoint)

```
```[areaServed](/areaServed)

[AdministrativeArea](/AdministrativeArea)or[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)[serviceArea](/serviceArea).```
```[availableLanguage](/availableLanguage)

[Language](/Language)or[Text](/Text)[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also[inLanguage](/inLanguage).```
```[contactOption](/contactOption)

[ContactPointOption](/ContactPointOption)```
```[contactType](/contactType)

[Text](/Text)```
```[email](/email)

[Text](/Text)```
```[faxNumber](/faxNumber)

[Text](/Text)```
```[hoursAvailable](/hoursAvailable)

[OpeningHoursSpecification](/OpeningHoursSpecification)```
```[productSupported](/productSupported)

[Product](/Product)or[Text](/Text)```
```[telephone](/telephone)

[Text](/Text)[Thing](/Thing)

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

[PostalAddress](/PostalAddress)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[GeoCoordinates](/GeoCoordinates)or[GeoShape](/GeoShape)or[Organization](/Organization)or[Person](/Person)or[Place](/Place)[billingAddress](/billingAddress)

[Order](/Order)[deliveryAddress](/deliveryAddress)

[ParcelDelivery](/ParcelDelivery)[gameLocation](/gameLocation)

[Game](/Game)or[VideoGameSeries](/VideoGameSeries)[itemLocation](/itemLocation)

[ArchiveComponent](/ArchiveComponent)[legalAddress](/legalAddress)

[Organization](/Organization)[location](/location)

[Action](/Action)or[Event](/Event)or[InteractionCounter](/InteractionCounter)or[Organization](/Organization)[originAddress](/originAddress)

[ParcelDelivery](/ParcelDelivery)[servicePostalAddress](/servicePostalAddress)

[ServiceChannel](/ServiceChannel)### Examples

[Example 1](#eg-0001)

Copied

Example notes or example HTML without markup.

Jane Doe <img src="janedoe.jpg" alt="Photo of Jane Doe"/> Professor 20341 Whitworth Institute Suite 123 405 Whitworth Seattle WA 98052 (425) 123-4567 <a href="mailto:jane-doe@xyz.edu">jane-doe@illinois.edu</a> Jane's home page: <a href="http://www.janedoe.com">janedoe.com</a> Graduate students: <a href="http://www.xyz.edu/students/alicejones.html">Alice Jones</a> <a href="http://www.xyz.edu/students/bobsmith.html">Bob Smith</a>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Jane Doe</span> <img src="janedoe.jpg" itemprop="image" alt="Photo of Jane Doe"/> <span itemprop="jobTitle">Professor</span> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress"> 20341 Whitworth Institute Suite 123 405 N. Whitworth </span> <span itemprop="addressLocality">Seattle</span>, <span itemprop="addressRegion">WA</span> <span itemprop="postalCode">98052</span> </div> <span itemprop="telephone">(425) 123-4567</span> <a href="mailto:jane-doe@xyz.edu" itemprop="email"> jane-doe@xyz.edu</a> Jane's home page: <a href="http://www.janedoe.com" itemprop="url">janedoe.com</a> Graduate students: <a href="http://www.xyz.edu/students/alicejones.html" itemprop="colleague"> Alice Jones</a> <a href="http://www.xyz.edu/students/bobsmith.html" itemprop="colleague"> Bob Smith</a> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Person"> <span property="name">Jane Doe</span> <img src="janedoe.jpg" property="image" alt="Photo of Jane Doe"/> <span property="jobTitle">Professor</span> <div property="address" typeof="PostalAddress"> <span property="streetAddress"> 20341 Whitworth Institute Suite 123 405 N. Whitworth </span> <span property="addressLocality">Seattle</span>, <span property="addressRegion">WA</span> <span property="postalCode">98052</span> </div> <span property="telephone">(425) 123-4567</span> <a href="mailto:jane-doe@xyz.edu" property="email"> jane-doe@xyz.edu</a> Jane's home page: <a href="http://www.janedoe.com" property="url">janedoe.com</a> Graduate students: <a href="http://www.xyz.edu/students/alicejones.html" property="colleague"> Alice Jones</a> <a href="http://www.xyz.edu/students/bobsmith.html" property="colleague"> Bob Smith</a> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Person", "address": { "@type": "PostalAddress", "addressLocality": "Seattle", "addressRegion": "WA", "postalCode": "98052", "streetAddress": "20341 Whitworth Institute 405 N. Whitworth", "extendedAddress": "Suite 123" }, "colleague": [ "http://www.xyz.edu/students/alicejones.html", "http://www.xyz.edu/students/bobsmith.html" ], "email": "mailto:jane-doe@xyz.edu", "image": "janedoe.jpg", "jobTitle": "Professor", "name": "Jane Doe", "telephone": "(425) 123-4567", "url": "http://www.janedoe.com" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0007)

Copied

Example notes or example HTML without markup.

Google.Org Contact Details: Main address: 38 avenue de l'Opéra, F-75002 Paris, France Tel: ( 33 1) 42 68 53 00, Fax: ( 33 1) 42 68 53 01 E-mail: secretariat (at) google.org URL: <a href="http://www.google.org">www.google.org</a> SIRET Code: 443 061 841 00039 VAT Number: FR64443061841 Members: - National Scientific Members in 100 countries and territories: Country1, Country2, ... - Scientific Union Members, 30 organizations listed in this Yearbook: Member 1, Member 2 History:

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Organization"> <span itemprop="name">Google.org (GOOG)</span> Contact Details: <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> Main address: <span itemprop="streetAddress">38 avenue de l'Opéra</span> <span itemprop="postalCode">F-75002</span> <span itemprop="addressLocality">Paris, France</span> , </div> Tel:<span itemprop="telephone">( 33 1) 42 68 53 00 </span>, Fax:<span itemprop="faxNumber">( 33 1) 42 68 53 01 </span>, E-mail: <span itemprop="email">secretariat@example.com</span> SIRET Code: 443 061 841 00039<meta itemprop="iso6523Code" content="0009:44306184100039" /> VAT Number: FR64443061841<meta itemprop="iso6523Code" content="9957:FR64443061841" /> Members: - National Scientific Members in 100 countries and territories: Country1, Country2, ... - Scientific Union Members, 30 organizations listed in this Yearbook: List of Alumni: <span itemprop="alumni" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Jack Dan</span> </span>, <span itemprop="alumni" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">John Smith</span> </span>, History: </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Organization"> <span property="name">Google.org (GOOG)</span> Contact Details: <div property="address" typeof="PostalAddress"> Main address: <span property="streetAddress">38 avenue de l'Opera</span> <span property="postalCode">F-75002</span> <span property="addressLocality">Paris, France</span> , </div> Tel:<span property="telephone">( 33 1) 42 68 53 00 </span>, Fax:<span property="faxNumber">( 33 1) 42 68 53 01 </span>, E-mail: <span property="email">secretariat@example.com</span> SIRET Code: 443 061 841 00039<meta itemprop="iso6523Code" content="0009:44306184100039" /> VAT Number: FR64443061841<meta itemprop="iso6523Code" content="9957:FR64443061841" /> Members: - National Scientific Members in 100 countries and territories: Country1, Country2, ... - Scientific Union Members, 30 organizations listed in this Yearbook: List of Alumni: <span property="alumni" typeof="Person"> <span property="name">Jack Dan</span> </span>, <span property="alumni" typeof="Person"> <span property="name">John Smith</span> </span> History: </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Organization", "address": { "@type": "PostalAddress", "addressLocality": "Paris, France", "postalCode": "F-75002", "streetAddress": "38 avenue de l'Opéra" }, "email": "secretariat@example.com", "faxNumber": "+33142685301", "iso6523Code": [ "0009:44306184100039", "9957:FR64443061841" ], "member": [ { "@type": "Organization" }, { "@type": "Organization" } ], "alumni": [ { "@type": "Person", "name": "Jack Dan" }, { "@type": "Person", "name": "John Smith" } ], "name": "Google.org (GOOG)", "telephone": "+33 1 42 68 53 00" } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0012)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Sep 14</div> <div class="event-title">Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">9:30 PM</div> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" itemprop="name"> Typhoon with Radiation City </div> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-09-14T21:30">Sat Sep 14</div> <div class="event-title" property="name">Typhoon with Radiation City</div> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <span property="offers" typeof="Offer"> <div class="event-price"> <meta property="priceCurrency" content="USD" />$ <meta property="price" content="13.00" />13.00 </div> <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "Typhoon with Radiation City", "offers": { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0015)

Copied

Example notes or example HTML without markup.

<h1>Beachwalk Beachwear & Giftware</h1> A superb collection of fine gifts and clothing to accent your stay in Mexico Beach. 3102 Highway 98 Mexico Beach, FL Phone: 850-648-4200

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/LocalBusiness"> <h1><span itemprop="name">Beachwalk Beachwear & Giftware</span></h1> <span itemprop="description"> A superb collection of fine gifts and clothing to accent your stay in Mexico Beach.</span> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">3102 Highway 98</span> <span itemprop="addressLocality">Mexico Beach</span>, <span itemprop="addressRegion">FL</span> </div> Phone: <span itemprop="telephone">850-648-4200</span> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="LocalBusiness"> <h1><span property="name">Beachwalk Beachwear & Giftware</span></h1> <span property="description"> A superb collection of fine gifts and clothing to accent your stay in Mexico Beach.</span> <div property="address" typeof="PostalAddress"> <span property="streetAddress">3102 Highway 98</span> <span property="addressLocality">Mexico Beach</span>, <span property="addressRegion">FL</span> </div> Phone: <span property="telephone">850-648-4200</span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "LocalBusiness", "address": { "@type": "PostalAddress", "addressLocality": "Mexico Beach", "addressRegion": "FL", "streetAddress": "3102 Highway 98" }, "description": "A superb collection of fine gifts and clothing to accent your stay in Mexico Beach.", "name": "Beachwalk Beachwear & Giftware", "telephone": "850-648-4200" } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0019)

Copied

Example notes or example HTML without markup.

Google Inc. P.O. Box 1234 Mountain View, CA 94043 United States

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="name">Google Inc.</span> P.O. Box<span itemprop="postOfficeBoxNumber">1234</span> <span itemprop="addressLocality">Mountain View</span>, <span itemprop="addressRegion">CA</span> <span itemprop="postalCode">94043</span> <span itemprop="addressCountry">United States</span> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="PostalAddress"> <span property="name">Google Inc.</span> P.O. Box<span property="postOfficeBoxNumber">1234</span> <span property="addressLocality">Mountain View</span>, <span property="addressRegion">CA</span> <span property="postalCode">94043</span> <span property="addressCountry">United States</span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "PostalAddress", "addressCountry": "United States", "addressLocality": "Mountain View", "addressRegion": "CA", "name": "Google Inc.", "postOfficeBoxNumber": "1234", "postalCode": "94043" } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-0171)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Sep 14</div> <div class="event-title">Typhoon with Radiation City</div> <div class="event-title">CANCELLED - Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">9:30 PM</div> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" itemprop="name"> CANCELLED - Typhoon with Radiation City </div> <meta itemprop="eventStatus" content="https://schema.org/EventCancelled"> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"> <a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" property="name"> CANCELLED - Typhoon with Radiation City </div> <meta property="eventStatus" content="https://schema.org/EventCancelled"> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div property="offers" typeof="Offer"> $<div class="event-price" property="price">13.00</div> <meta property="priceCurrency" content="USD"><a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "eventStatus": "https://schema.org/EventCancelled", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "CANCELLED - Typhoon with Radiation City", "offers": { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" } </script>

Structured representation of the JSON-LD example.

[Example 7](#eg-0172)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Oct 12</div> <div><span>(previously scheduled for Sept 14th)</span></div> <div class="event-title">Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">10:00 PM</div> <span> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-10-12T22:00"> Sat Oct 12 </div> <div class="event-title" itemprop="name"> Typhoon with Radiation City </div> <meta itemprop="eventStatus" content="https://schema.org/EventRescheduled"><span itemprop="previousStartDate" content="2013-09-14T21:30">(previously scheduled for Sept 14th)</span> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time"> 10:00 PM </div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-10-12T22:00">Sat Oct 12</div> <div class="event-title" property="name">Typhoon with Radiation City</div> <meta property="eventStatus" content="https://schema.org/EventRescheduled"> <span property="previousStartDate" content="2013-09-14T21:30">(previously scheduled for Sept 14th)</span> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">10:00 PM</div> <span property="offers" typeof="Offer"> <div class="event-price"> <meta property="priceCurrency" content="USD" />$ <meta property="price" content="13.00" />13.00 </div> <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@graph": [ { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, { "@type": "Offer", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" } ] } </script>

Structured representation of the JSON-LD example.

[Example 8](#eg-0173)

Copied

Example notes or example HTML without markup.

<div class="event-wrapper"> <div class="event-date">Sat Sep 14</div> <div class="event-title">SOLD OUT! Typhoon with Radiation City</div> <div class="event-venue"> The Hi-Dive <div class="address"> 7 S. Broadway<br> Denver, CO 80209 </div> </div> <div class="event-time">10:00 PM</div> <span> <div class="event-price">$13.00</div> <a href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="event-wrapper" itemscope itemtype="https://schema.org/Event"> <div class="event-date" itemprop="startDate" content="2013-09-14T21:30"> Sat Sep 14 </div> <div class="event-title" itemprop="name"> SOLD OUT! Typhoon with Radiation City </div> <div class="event-venue" itemprop="location" itemscope itemtype="https://schema.org/Place"> <span itemprop="name">The Hi-Dive</span> <div class="address" itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">7 S. Broadway</span><br> <span itemprop="addressLocality">Denver</span>, <span itemprop="addressRegion">CO</span> <span itemprop="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <meta itemprop="availability" content="https://schema.org/SoldOut"> <div class="event-price" itemprop="price" content="13.00">$13.00</div> <meta itemprop="priceCurrency" content="USD"><a itemprop="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" class="event-wrapper" typeof="Event"> <div class="event-date" property="startDate" content="2013-09-14T21:30">Sat Sep 14</div> <div class="event-title" property="name">SOLD OUT! Typhoon with Radiation City</div> <div class="event-venue" property="location" typeof="Place"> <span property="name">The Hi-Dive</span> <div class="address" property="address" typeof="PostalAddress"> <span property="streetAddress">7 S. Broadway</span><br> <span property="addressLocality">Denver</span>, <span property="addressRegion">CO</span> <span property="postalCode">80209</span> </div> </div> <div class="event-time">9:30 PM</div> <span property="offers" typeof="Offer"> <meta property="availability" content="https://schema.org/SoldOut"> <div class="event-price"> <meta property="priceCurrency" content="USD" />$ <meta property="price" content="13.00" />13.00 </div> <a property="url" href="http://www.ticketfly.com/purchase/309433">Tickets</a> </span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": "80209", "streetAddress": "7 S. Broadway" }, "name": "The Hi-Dive" }, "name": "SOLD OUT! Typhoon with Radiation City", "offers": { "@type": "Offer", "availability": "https://schema.org/SoldOut", "price": "13.00", "priceCurrency": "USD", "url": "http://www.ticketfly.com/purchase/309433" }, "startDate": "2013-09-14T21:30" } </script>

Structured representation of the JSON-LD example.

[Example 9](#eg-0174)

Copied

Example notes or example HTML without markup.

JSON-LD description of a scheduled Event with limited ticket availability and performer details indicated using sameAs.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context" : "https://schema.org", "@type" : "Event", "name" : "Typhoon with Radiation City", "startDate" : "2013-09-14T21:30", "location" : { "@type" : "Place", "sameAs" : "http://www.hi-dive.com", "name" : "The Hi-Dive", "address" : { "@type" : "PostalAddress", "streetAddress" : "7 S. Broadway", "addressLocality" : "Denver", "addressRegion" : "CO", "postalCode" : "80209" } }, "performer" : [ { "@type" : "MusicGroup", "name" : "Typhoon", "sameAs" : "http://en.wikipedia.org/wiki/Typhoon_(American_band)" }, { "@type" : "MusicGroup", "name" : "RadiationCity", "sameAs" : "http://en.wikipedia.org/wiki/Radiation_City" }], "offers" : { "@type" : "Offer", "availability" : "https://schema.org/LimitedAvailability", "priceCurrency": "USD", "price" : "13.00", "url" : "http://www.ticketfly.com/purchase/309433" }, "typicalAgeRange" : "18+" } </script>

Structured representation of the JSON-LD example.

[Example 10](#eg-0197)

Copied

Example notes or example HTML without markup.

<div> <div> <h1>Delia's Daily Supplies</h1> <p>For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: Monday-Friday 7am-11pm</p> <p>Phone: 555-0100-1110</p> </div> <address> <span> Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span>Boston</span>, <span>MA, USA</span> </address> <div> <h2>Philippa's Pharmacy</h2> <p>A superb collection of fine pharmaceuticals...</p> <p>Open: Monday-Thursday 9am-noon</p> <p>Phone: 555-0100-1111</p> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Store"> <div> <h1 itemprop="name">Delia's Daily Supplies</h1> <p itemprop="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span itemprop="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm</span></p> <p>Phone: <span itemprop="telephone" content="+155501001110">555-0100-1110</span></p> </div> <address itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress"> Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span itemprop="addressLocality">Boston</span>, <span itemprop="addressRegion">MA</span>, <span itemprop="addressCountry">USA</span> </address> <div itemprop="department" itemscope itemtype="https://schema.org/Pharmacy"> <h2 itemprop="name">Philippa's Pharmacy</h2> <p itemprop="description">A superb collection of fine pharmaceuticals...</p> <p>Open: <span itemprop="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span itemprop="telephone" content="+155501001111">555-0100-1111</span></p> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Store"> <div> <h1 property="name">Delia's Daily Supplies</h1> <p property="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span property="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm </span></p> <p>Phone: <span property="telephone" content="+155501001110">555-0100-1110</span></p> </div> <address property="address" typeof="PostalAddress"> <span property="streetAddress"> Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span property="addressLocality">Boston</span>, <span property="addressRegion">MA</span>, <span property="addressCountry">USA</span> </address> <div property="department" typeof="Pharmacy"> <h2 property="name">Philippa's Pharmacy</h2> <p property="description">A superb collection of fine pharmaceuticals...</p> <p>Open: <span property="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span property="telephone" content="+155501001111">555-0100-1111</span></p> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Store", "name": "Delia's Daily Supplies", "description": "For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.", "openingHours": "Mo-Fr 07:00-23:00", "telephone": "+155501001110", "address": { "@type": "PostalAddress", "streetAddress": "Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101", "addressLocality": "Boston", "addressRegion": "MA", "addressCountry": "USA" }, "department": { "@type": "Pharmacy", "name": "Philippa's Pharmacy", "description": "A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.", "openingHours": "Mo-Th 09:00-12:00", "telephone": "+155501001111" } } </script>

Structured representation of the JSON-LD example.

[Example 11](#eg-0198)

Copied

Example notes or example HTML without markup.

<div> <div> <h1>Delia's Daily Supplies</h1> <p>For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: Monday-Friday 7am-11pm</p> <p>Phone: 555-0100-1110</p> </div> <address> <span>Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span>Boston</span>, <span>MA, USA</span> </address> <div> <h2>Philippa's Pharmacy</h2> <p>A superb collection of fine pharmaceuticals...</p> <p>Open: Monday-Thursday 9am-noon</p> <p>Phone: 555-0100-1111</p> <address> <span>Unit 42b, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span>Boston</span>, <span>MA, USA</span> </address> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Store"> <div> <h1 itemprop="name">Delia's Daily Supplies</h1> <p itemprop="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span itemprop="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm</span></p> <p>Phone: <span itemprop="telephone" content="+155501001110">555-0100-1110</span></p> </div> <address itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span itemprop="addressLocality">Boston</span>, <span itemprop="addressRegion">MA</span>, <span itemprop="addressCountry">USA</span> </address> <div itemprop="department" itemscope itemtype="https://schema.org/Pharmacy"> <h2 itemprop="name">Philippa's Pharmacy</h2> <p itemprop="description">A superb collection of fine pharmaceuticals...</p> <p>Open: <span itemprop="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span itemprop="telephone" content="+155501001111">555-0100-1111</span></p> <address itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">Unit 42b, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span itemprop="addressLocality">Boston</span>, <span itemprop="addressRegion">MA</span>, <span itemprop="addressCountry">USA</span> </address> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Store"> <div> <h1 property="name">Delia's Daily Supplies</h1> <p property="description">For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.</p> <p>Open: <span property="openingHours" content="Mo-Fr 07:00-23:00">Monday-Friday 7am-11pm</span></p> <p>Phone: <span property="telephone" content="+155501001110">555-0100-1110</span></p> </div> <address property="address" typeof="PostalAddress"> <span property="streetAddress">Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span property="addressLocality">Boston</span>, <span property="addressRegion">MA</span>, <span property="addressCountry">USA</span> </address> <div property="department" typeof="Pharmacy"> <h2 property="name">Philippa's Pharmacy</h2> <p property="description">A superb collection of fine pharmaceuticals...</p> <p>Open: <span property="openingHours" content="Mo-Th 09:00-12:00">Monday-Thursday 9am-noon</span></p> <p>Phone: <span property="telephone" content="+155501001111">555-0100-1111</span></p> <address property="address" typeof="PostalAddress"> <span property="streetAddress">Unit 42b, Land of Bargains Shopping Paradise, 12 Highway 101</span>, <span property="addressLocality">Boston</span>, <span property="addressRegion">MA</span>, <span property="addressCountry">USA</span> </address> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Store", "name": "Delia's Daily Supplies", "description": "For your daily newspapers, candies, snacks and (via our in-store pharmacy) drugs and healthcare products to keep you and your family happy, healthy and supplied with all your daily needs.", "openingHours": "Mo-Fr 07:00-23:00", "telephone": "+155501001110", "address": { "@type": "PostalAddress", "streetAddress": "Unit 42, Land of Bargains Shopping Paradise, 12 Highway 101", "addressLocality": "Boston", "addressRegion": "MA", "addressCountry": "USA" }, "department": { "@type": "Pharmacy", "name": "Philippa's Pharmacy", "description": "A superb collection of fine pharmaceuticals for your beauty and healthcare needs, a department of Delia's Drugstore. Call our desk to speak to the on-duty pharmacist any morning Monday-Thursday.", "openingHours": "Mo-Th 09:00-12:00", "telephone": "+155501001111", "address": { "@type": "PostalAddress", "streetAddress": "Unit 42b, Land of Bargains Shopping Paradise, 12 Highway 101", "addressLocality": "Boston", "addressRegion": "MA", "addressCountry": "USA" } } } </script>

Structured representation of the JSON-LD example.

[Example 12](#eg-0202)

Copied

Example notes or example HTML without markup.

An example of a more fully specified MusicEvent, including a tour image, full venue address, multiple performers, and multiple ticket classes.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> [{ "@context" : "https://schema.org", "@type" : "MusicEvent", "name" : "B.B. King with Jonathon \"Boogie\" Long", "image" : "http://www.bbking.com/gallery/b-b-king-live.jpg", "url" : "http://www.bbking.com/events/apr12-providence.html", "startDate" : "2014-04-12T19:30", "doorTime" : "18:30:00", "endDate" : "2014-04-12T22:00", "location" : { "@type" : "Place", "name" : "Lupo's Heartbreak Hotel", "sameAs" : "http://lupos.com/", "address" : { "@type" : "PostalAddress", "streetAddress" : "79 Washington St.", "addressLocality" : "Providence", "addressRegion" : "RI", "postalCode" : "02903", "addressCountry" : "US" } }, "offers" : [ { "@type" : "Offer", "name" : "General Admission", "priceCurrency": "USD", "price" : "63.25", "availability" : "SoldOut", "url" : "http://www.ticketmaster.com/event/17004C29" },{ "@type" : "Offer", "name" : "VIP Experience", "url" : "http://www.example.com/Abcde12345", "priceCurrency": "USD", "price" : "299.00", "validFrom" : "2014-02-05T10:00", "validThrough" : "2014-03-19T23:59" } ], "performer" : [ { "@type" : "MusicGroup", "name" : "B.B. King", "sameAs" : "http://en.wikipedia.org/wiki/B.B._King" },{ "@type" : "MusicGroup", "name" : "Jonathon \"Boogie\" Long", "sameAs" : "http://jonathonboogielong.com/" } ], "eventStatus" : "EventRescheduled", "previousStartDate" : "2013-09-30T19:30", "typicalAgeRange" : "18+" }] </script>

Structured representation of the JSON-LD example.

[Example 13](#eg-0461)

Copied

Example notes or example HTML without markup.

<a href="nba-miami-philidelphia-game3.html"> NBA Eastern Conference First Round Playoff Tickets: Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1) </a> Thu, 04/21/16 8:00 p.m. <a href="wells-fargo-center.html"> Wells Fargo Center </a> Philadelphia, PA Priced from: $35 1938 tickets left

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Event"> <a itemprop="url" href="nba-miami-philidelphia-game3.html"> NBA Eastern Conference First Round Playoff Tickets: <span itemprop="name"> Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1) </span> </a> <meta itemprop="startDate" content="2016-04-21T20:00"> Thu, 04/21/16 8:00 p.m. <div itemprop="location" itemscope itemtype="https://schema.org/Place"> <a itemprop="url" href="wells-fargo-center.html"> Wells Fargo Center </a> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="addressLocality">Philadelphia</span>, <span itemprop="addressRegion">PA</span> </div> </div> <div itemprop="offers" itemscope itemtype="https://schema.org/AggregateOffer"> <meta itemprop="priceCurrency" content="USD" /> Priced from: <span itemprop="lowPrice" content="35">$35</span> <span itemprop="offerCount">1938</span> tickets left </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Event"> <a property="url" href="nba-miami-philidelphia-game3.html"> NBA Eastern Conference First Round Playoff Tickets: <span property="name"> Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1) </span> </a> <meta property="startDate" content="2016-04-21T20:00"> Thu, 04/21/16 8:00 p.m. <div property="location" typeof="Place"> <a property="url" href="wells-fargo-center.html"> Wells Fargo Center </a> <div property="address" typeof="PostalAddress"> <span property="addressLocality">Philadelphia</span>, <span property="addressRegion">PA</span> </div> </div> <div property="offers" typeof="AggregateOffer"> <meta property="priceCurrency" content="USD" /> Priced from: <span property="lowPrice" content="35">$35</span> <span property="offerCount">1938</span> tickets left </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Event", "name": "Miami Heat at Philadelphia 76ers - Game 3 (Home Game 1)", "location": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Philadelphia", "addressRegion": "PA" }, "url": "wells-fargo-center.html" }, "offers": { "@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "35", "offerCount": "1938" }, "startDate": "2016-04-21T20:00", "url": "nba-miami-philidelphia-game3.html" } </script>

Structured representation of the JSON-LD example.
