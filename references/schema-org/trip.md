---
title: "Trip"
source_url: https://schema.org/Trip
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Trip

# Trip

A Schema.org Type

- Canonical URL: https://schema.org/Trip
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Trip)

A trip or journey. An itinerary of visits to one or more places.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

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

[URL](/URL)Instances of

[Trip](/Trip)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction), e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.[partOfTrip](/partOfTrip)

[Trip](/Trip)[Trip](/Trip)is a subTrip of another Trip. For example Day 1, Day 2, etc. of a multi-day trip.[subTrip](/subTrip)

[Trip](/Trip)[Trip](/Trip)that is a subTrip of this Trip. For example Day 1, Day 2, etc. of a multi-day trip.#### More specific Types

### Acknowledgements

Tourism Structured Web Data Community Group

[Tourism Structured Web Data Community Group](https://www.w3.org/community/tourismdata).

### Examples

[Example 1](#eg-0264)

Copied

Example notes or example HTML without markup.

<div class="tourist-trip-wrapper"> <h1> Australia and New Zealand </h1> <p> This trip is modeled as two distinct Tourist Trips using the subTrip property. </p> <div class="has-part-wrapper"> <div> <h2> Australia </h2> <p> This is a trip on its own. </p> </div> <div> <h2> New Zealand </h2> <p> This is another trip nested inside the main one. </p> </div> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div> <div itemtype="https://schema.org/TouristTrip" itemscope> <meta itemprop="name" content="Australia and New Zealand" /> <meta itemprop="description" content="This trip is modeled as two distinct Tourist Trips using the subTrip property." /> <div itemprop="subTrip" itemtype="https://schema.org/TouristTrip" itemscope> <meta itemprop="name" content="Australia" /> <meta itemprop="description" content="This is a trip on its own." /> </div> <div itemprop="subTrip" itemtype="https://schema.org/TouristTrip" itemscope> <meta itemprop="name" content="New Zealand" /> <meta itemprop="description" content="This is another trip nested inside the main one." /> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div> <div vocab="https://schema.org/" typeof="TouristTrip"> <div property="name" content="Australia and New Zealand"></div> <div property="description" content="This trip is modeled as two distinct Tourist Trips using the subTrip property."></div> <div rel="subTrip"> <div typeof="TouristTrip"> <div property="name" content="Australia"></div> <div property="description" content="This is a trip on its own."></div> </div> </div> <div rel="subTrip"> <div typeof="TouristTrip"> <div property="description" content="This is another trip nested inside the main one."></div> <div property="name" content="New Zealand"></div> </div> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org", "@type": "TouristTrip", "name": "Australia and New Zealand", "description": "This trip is modeled as two distinct Tourist Trips using the subTrip property.", "subTrip": [ { "@type": "TouristTrip", "name": "Australia", "description": "This is a trip on its own." }, { "@type": "TouristTrip", "name": "New Zealand", "description": "This is another trip nested inside the main one." } ] }

Structured representation of the JSON-LD example.

[Example 2](#eg-0441)

Copied

Example notes or example HTML without markup.

<div> <div> <h1> Your ideal trip to England </h1> <div> The dozen best places and areas that should be on you list when visiting England. Choose you own order but visit as many as you can. </div> <ul> <li> <a href="https://en.wikipedia.org/wiki/London"> <span style="font-weight:bold;">London</span></a>: <span>While it's not impossible to plan a trip to England without visiting London, it's certainly not to be advised, as the nation's sprawling capital boasts plenty of attractions to keep you busy.</span> </li> <li> <a href="https://en.wikipedia.org/wiki/Edinburgh"> <span style="font-weight:bold;">Edinburgh</span></a>: <span>One of Scotland's most attractive cities, the capital city of Edinburgh is also one of England's most visited destinations.</span> </li> <li> <a href="https://en.wikipedia.org/wiki/Bath,_Somerset"> <span style="font-weight:bold;">Bath</span></a>: <span>Although one of England's smaller cities, Bath more than makes up for its diminutive size with a multitude of things to see and do.</span> </li> <li> <a href="https://en.wikipedia.org/wiki/Stonehenge"> <span style="font-weight:bold;">Stonehenge</span></a>: <span>One of the planet's oldest World Heritage Sites, Stonehenge has been a place of pilgrimage for more than 4,500 years.</span> </li> <li> <a href="https://en.wikipedia.org/wiki/Windsor,_Berkshire"> <span style="font-weight:bold;">Windsor</span></a>: <span>The historic town of Windsor, conveniently located a short train ride west of London, offers plenty of fun things for tourists to do.</span> </li> <li> <a href="https://en.wikipedia.org/wiki/Cotswolds"> <span style="font-weight:bold;">The Cotswolds</span></a>: <span>Covering almost 1,287 square kilometers of pristine countryside, the beautiful Cotswolds is undoubtedly one of the most photographed corners of England.</span> </li> <li> <a href="https://en.wikipedia.org/wiki/Lake_District_National_Park"> <span style="font-weight:bold;">The Lake District</span></a>: <span>In the north west of England and covering an area of 1,448 square kilometers is more of England's most beautiful scenery: the Lake District National Park.</span> </li> <li> <a href="https://en.wikipedia.org/wiki/York"> <span style="font-weight:bold;">York</span></a>: <span>One of northern England's most popular tourist destinations, the medieval city of York, long the ecclesiastical capital of the Church of England, boasts one of the country's most magnificent cathedrals.</span> </li> <li> <a href="https://en.wikipedia.org/wiki/Oxford"> <span style="font-weight:bold;">Oxford</span></a>: <span>England has long been a center of learning, with Oxford being one of the two most famous university towns also ranking highly as tourist destinations.</span> </li> <li> <a href="https://en.wikipedia.org/wiki/Cambridge"> <span style="font-weight:bold;">Cambridge</span></a>: <span>England has long been a center of learning, with Cambridge being one of the two most famous university towns also ranking highly as tourist destinations.</span> </li> <li> <a href="https://en.wikipedia.org/wiki/Canterbury"> <span style="font-weight:bold;">Canterbury</span></a>: <span>Pay a visit to historic Canterbury, and you'll soon discover why this beautiful city continues to be such a draw for visitors to England.</span> </li> <li> <a href="https://en.wikipedia.org/wiki/Loch_Ness"> <span style="font-weight:bold;">York</span></a>: <span>Despite the fact that the legends of mythical monsters have largely been debunked (just don't tell the locals), spectacular Loch Ness remains an extremely popular tourist attraction for travelers heading to Scotland."</span> </li> </ul> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div> <div itemtype="https://schema.org/Trip" itemscope=""> <h1 itemprop="name"> Your ideal trip to England </h1> <div itemprop="description"> The dozen best places and areas that should be on you list when visiting England. Choose you own order but visit as many as you can. </div> <ul> <li itemprop="itinerary" itemtype="https://schema.org/City" itemscope=""> <a href="https://en.wikipedia.org/wiki/London"> <span itemprop="name" style="font-weight:bold;">London</span></a>: <span itemprop="description">While it's not impossible to plan a trip to England without visiting London, it's certainly not to be advised, as the nation's sprawling capital boasts plenty of attractions to keep you busy.</span> </li> <li itemprop="itinerary" itemtype="https://schema.org/City" itemscope=""> <a href="https://en.wikipedia.org/wiki/Edinburgh"> <span itemprop="name" style="font-weight:bold;">Edinburgh</span></a>: <span itemprop="description">One of Scotland's most attractive cities, the capital city of Edinburgh is also one of England's most visited destinations.</span> </li> <li itemprop="itinerary" itemtype="https://schema.org/City" itemscope=""> <a href="https://en.wikipedia.org/wiki/Bath,_Somerset"> <span itemprop="name" style="font-weight:bold;">Bath</span></a>: <span itemprop="description">Although one of England's smaller cities, Bath more than makes up for its diminutive size with a multitude of things to see and do.</span> </li> <li itemprop="itinerary" itemtype="https://schema.org/LandmarksOrHistoricalBuildings" itemscope=""> <a href="https://en.wikipedia.org/wiki/Stonehenge"> <span itemprop="name" style="font-weight:bold;">Stonehenge</span></a>: <span itemprop="description">One of the planet's oldest World Heritage Sites, Stonehenge has been a place of pilgrimage for more than 4,500 years.</span> </li> <li itemprop="itinerary" itemtype="https://schema.org/AdministrativeArea" itemscope=""> <a href="https://en.wikipedia.org/wiki/Windsor,_Berkshire"> <span itemprop="name" style="font-weight:bold;">Windsor</span></a>: <span itemprop="description">The historic town of Windsor, conveniently located a short train ride west of London, offers plenty of fun things for tourists to do.</span> </li> <li itemprop="itinerary" itemtype="https://schema.org/AdministrativeArea" itemscope=""> <a href="https://en.wikipedia.org/wiki/Cotswolds"> <span itemprop="name" style="font-weight:bold;">The Cotswolds</span></a>: <span itemprop="description">Covering almost 1,287 square kilometers of pristine countryside, the beautiful Cotswolds is undoubtedly one of the most photographed corners of England.</span> </li> <li itemprop="itinerary" itemtype="https://schema.org/AdministrativeArea" itemscope=""> <a href="https://en.wikipedia.org/wiki/Lake_District_National_Park"> <span itemprop="name" style="font-weight:bold;">The Lake District</span></a>: <span itemprop="description">In the north west of England and covering an area of 1,448 square kilometers is more of England's most beautiful scenery: the Lake District National Park.</span> </li> <li itemprop="itinerary" itemtype="https://schema.org/City" itemscope=""> <a href="https://en.wikipedia.org/wiki/York"> <span itemprop="name" style="font-weight:bold;">York</span></a>: <span itemprop="description">One of northern England's most popular tourist destinations, the medieval city of York, long the ecclesiastical capital of the Church of England, boasts one of the country's most magnificent cathedrals.</span> </li> <li itemprop="itinerary" itemtype="https://schema.org/City" itemscope=""> <a href="https://en.wikipedia.org/wiki/Oxford"> <span itemprop="name" style="font-weight:bold;">Oxford</span></a>: <span itemprop="description">England has long been a center of learning, with Oxford being one of the two most famous university towns also ranking highly as tourist destinations.</span> </li> <li itemprop="itinerary" itemtype="https://schema.org/City" itemscope=""> <a href="https://en.wikipedia.org/wiki/Cambridge"> <span itemprop="name" style="font-weight:bold;">Cambridge</span></a>: <span itemprop="description">England has long been a center of learning, with Cambridge being one of the two most famous university towns also ranking highly as tourist destinations.</span> </li> <li itemprop="itinerary" itemtype="https://schema.org/City" itemscope=""> <a href="https://en.wikipedia.org/wiki/Canterbury"> <span itemprop="name" style="font-weight:bold;">Canterbury</span></a>: <span itemprop="description">Pay a visit to historic Canterbury, and you'll soon discover why this beautiful city continues to be such a draw for visitors to England.</span> </li> <li itemprop="itinerary" itemtype="https://schema.org/LakeBodyOfWater" itemscope=""> <a href="https://en.wikipedia.org/wiki/Loch_Ness"> <span itemprop="name" style="font-weight:bold;">York</span></a>: <span itemprop="description">Despite the fact that the legends of mythical monsters have largely been debunked (just don't tell the locals), spectacular Loch Ness remains an extremely popular tourist attraction for travelers heading to Scotland."</span> </li> </ul> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div> <div vocab="https://schema.org/" typeof="Trip"> <h1 property="name"> Your ideal trip to England </h1> <div property="description"> The dozen best places and areas that should be on you list when visiting England. Choose you own order but visit as many as you can. </div> <ul> <li property="itinerary" typeof="City"> <a href="https://en.wikipedia.org/wiki/London"> <span property="name" style="font-weight:bold;">London</span></a>: <span property="description">While it's not impossible to plan a trip to England without visiting London, it's certainly not to be advised, as the nation's sprawling capital boasts plenty of attractions to keep you busy.</span> </li> <li property="itinerary" typeof="City"> <a href="https://en.wikipedia.org/wiki/Edinburgh"> <span property="name" style="font-weight:bold;">Edinburgh</span></a>: <span property="description">One of Scotland's most attractive cities, the capital city of Edinburgh is also one of England's most visited destinations.</span> </li> <li property="itinerary" typeof="City"> <a href="https://en.wikipedia.org/wiki/Bath,_Somerset"> <span property="name" style="font-weight:bold;">Bath</span></a>: <span property="description">Although one of England's smaller cities, Bath more than makes up for its diminutive size with a multitude of things to see and do.</span> </li> <li property="itinerary" typeof="LandmarksOrHistoricalBuildings"> <a href="https://en.wikipedia.org/wiki/Stonehenge"> <span property="name" style="font-weight:bold;">Stonehenge</span></a>: <span property="description">One of the planet's oldest World Heritage Sites, Stonehenge has been a place of pilgrimage for more than 4,500 years.</span> </li> <li property="itinerary" typeof="AdministrativeArea"> <a href="https://en.wikipedia.org/wiki/Windsor,_Berkshire"> <span property="name" style="font-weight:bold;">Windsor</span></a>: <span property="description">The historic town of Windsor, conveniently located a short train ride west of London, offers plenty of fun things for tourists to do.</span> </li> <li property="itinerary" typeof="AdministrativeArea"> <a href="https://en.wikipedia.org/wiki/Cotswolds"> <span property="name" style="font-weight:bold;">The Cotswolds</span></a>: <span property="description">Covering almost 1,287 square kilometers of pristine countryside, the beautiful Cotswolds is undoubtedly one of the most photographed corners of England.</span> </li> <li property="itinerary" typeof="AdministrativeArea"> <a href="https://en.wikipedia.org/wiki/Lake_District_National_Park"> <span property="name" style="font-weight:bold;">The Lake District</span></a>: <span property="description">In the north west of England and covering an area of 1,448 square kilometers is more of England's most beautiful scenery: the Lake District National Park.</span> </li> <li property="itinerary" typeof="City"> <a href="https://en.wikipedia.org/wiki/York"> <span property="name" style="font-weight:bold;">York</span></a>: <span property="description">One of northern England's most popular tourist destinations, the medieval city of York, long the ecclesiastical capital of the Church of England, boasts one of the country's most magnificent cathedrals.</span> </li> <li property="itinerary" typeof="City"> <a href="https://en.wikipedia.org/wiki/Oxford"> <span property="name" style="font-weight:bold;">Oxford</span></a>: <span property="description">England has long been a center of learning, with Oxford being one of the two most famous university towns also ranking highly as tourist destinations.</span> </li> <li property="itinerary" typeof="City"> <a href="https://en.wikipedia.org/wiki/Cambridge"> <span property="name" style="font-weight:bold;">Cambridge</span></a>: <span property="description">England has long been a center of learning, with Cambridge being one of the two most famous university towns also ranking highly as tourist destinations.</span> </li> <li property="itinerary" typeof="City"> <a href="https://en.wikipedia.org/wiki/Canterbury"> <span property="name" style="font-weight:bold;">Canterbury</span></a>: <span property="description">Pay a visit to historic Canterbury, and you'll soon discover why this beautiful city continues to be such a draw for visitors to England.</span> </li> <li property="itinerary" typeof="LakeBodyOfWater"> <a href="https://en.wikipedia.org/wiki/Loch_Ness"> <span property="name" style="font-weight:bold;">York</span></a>: <span property="description">Despite the fact that the legends of mythical monsters have largely been debunked (just don't tell the locals), spectacular Loch Ness remains an extremely popular tourist attraction for travelers heading to Scotland."</span> </li> </ul> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org", "@type": "Trip", "name": "Your ideal trip to England", "description": "The dozen best places and areas that should be on you list when visiting England. Choose you own order but visit as many as you can", "itinerary": [ { "@type": "City", "name": "London", "description": "While it's not impossible to plan a trip to England without visiting London, it's certainly not to be advised, as the nation's sprawling capital boasts plenty of attractions to keep you busy", "url": "https://en.wikipedia.org/wiki/London" }, { "@type": "City", "name": "Edinburgh", "description": "One of Scotland's most attractive cities, the capital city of Edinburgh is also one of England's most visited destinations.", "url": "https://en.wikipedia.org/wiki/Edinburgh" }, { "@type": "City", "name": "Bath", "description": "Although one of England's smaller cities, Bath more than makes up for its diminutive size with a multitude of things to see and do.", "url": "https://en.wikipedia.org/wiki/Bath,_Somerset" }, { "@type": "LandmarksOrHistoricalBuildings", "name": "Stonehenge", "description": "One of the planet's oldest World Heritage Sites, Stonehenge has been a place of pilgrimage for more than 4,500 years.", "url": "https://en.wikipedia.org/wiki/Stonehenge" }, { "@type": "AdministrativeArea", "name": "Windsor", "description": "The historic town of Windsor, conveniently located a short train ride west of London, offers plenty of fun things for tourists to do.", "url": "https://en.wikipedia.org/wiki/Windsor,_Berkshire" }, { "@type": "AdministrativeArea", "name": "The Cotswolds", "description": "Covering almost 1,287 square kilometers of pristine countryside, the beautiful Cotswolds is undoubtedly one of the most photographed corners of England.", "url": "https://en.wikipedia.org/wiki/Cotswolds" }, { "@type": "AdministrativeArea", "name": "The Lake District", "description": "In the north west of England and covering an area of 1,448 square kilometers is more of England's most beautiful scenery: the Lake District National Park.", "url": "https://en.wikipedia.org/wiki/Lake_District_National_Park" }, { "@type": "City", "name": "York", "description": "One of northern England's most popular tourist destinations, the medieval city of York, long the ecclesiastical capital of the Church of England, boasts one of the country's most magnificent cathedrals.", "url": "https://en.wikipedia.org/wiki/York" }, { "@type": "City", "name": "Oxford", "description": "England has long been a center of learning, with Oxford being one of the two most famous university towns also ranking highly as tourist destinations.", "url": "https://en.wikipedia.org/wiki/Oxford" }, { "@type": "City", "name": "Cambridge", "description": "England has long been a center of learning, with Cambridge being one of the two most famous university towns also ranking highly as tourist destinations.", "url": "https://en.wikipedia.org/wiki/Cambridge" }, { "@type": "City", "name": "Canterbury", "description": "Pay a visit to historic Canterbury, and you'll soon discover why this beautiful city continues to be such a draw for visitors to England.", "url": "https://en.wikipedia.org/wiki/Canterbury" }, { "@type": "LakeBodyOfWater", "name": "Loch Ness", "description": "Despite the fact that the legends of mythical monsters have largely been debunked (just don't tell the locals), spectacular Loch Ness remains an extremely popular tourist attraction for travelers heading to Scotland.", "url": "https://en.wikipedia.org/wiki/Loch_Ness" } ] }

Structured representation of the JSON-LD example.
