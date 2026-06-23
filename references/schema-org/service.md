---
title: "Service"
source_url: https://schema.org/Service
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Service

# Service

A Schema.org Type

- Canonical URL: https://schema.org/Service
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Service)

A service provided by an organization, e.g. delivery service, print services, etc.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[areaServed](/areaServed)

[AdministrativeArea](/AdministrativeArea)or[GeoShape](/GeoShape)or[Place](/Place)or[Text](/Text)[serviceArea](/serviceArea).```
```[audience](/audience)

[Audience](/Audience)[serviceAudience](/serviceAudience).```
```[availableChannel](/availableChannel)

[ServiceChannel](/ServiceChannel)```
```[award](/award)

[Text](/Text)[awards](/awards).```
```[brand](/brand)

[Brand](/Brand)or[Organization](/Organization)```
```[broker](/broker)

[Organization](/Organization)or[Person](/Person)[bookingAgent](/bookingAgent).```
```[category](/category)

[CategoryCode](/CategoryCode)or[PhysicalActivityCategory](/PhysicalActivityCategory)or[Text](/Text)or[Thing](/Thing)or[URL](/URL)```
```[hasCertification](/hasCertification)

[Certification](/Certification)```
```[hasOfferCatalog](/hasOfferCatalog)

[OfferCatalog](/OfferCatalog)```
```[hoursAvailable](/hoursAvailable)

[OpeningHoursSpecification](/OpeningHoursSpecification)```
```[isRelatedTo](/isRelatedTo)

[Product](/Product)or[Service](/Service)```
```[isSimilarTo](/isSimilarTo)

[Product](/Product)or[Service](/Service)```
```[logo](/logo)

[ImageObject](/ImageObject)or[URL](/URL)```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[providerMobility](/providerMobility)

[Text](/Text)```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[serviceOutput](/serviceOutput)

[Thing](/Thing)[produces](/produces).```
```[serviceType](/serviceType)

[GovernmentBenefitsType](/GovernmentBenefitsType)or[Text](/Text)```
```[slogan](/slogan)

[Text](/Text)```
```[termsOfService](/termsOfService)

[Text](/Text)or[URL](/URL)[Thing](/Thing)

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

[Service](/Service)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Product](/Product)or[Service](/Service)[isSimilarTo](/isSimilarTo)

[Product](/Product)or[Service](/Service)[issuedThrough](/issuedThrough)

[Permit](/Permit)[itemOffered](/itemOffered)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction), e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.[orderedItem](/orderedItem)

[Order](/Order)or[OrderItem](/OrderItem)[providesService](/providesService)

[ServiceChannel](/ServiceChannel)[typeOfGood](/typeOfGood)

[OwnershipInfo](/OwnershipInfo)or[TypeAndQuantityNode](/TypeAndQuantityNode)#### More specific Types

-
[BroadcastService](/BroadcastService) -
[CableOrSatelliteService](/CableOrSatelliteService) -
[FinancialProduct](/FinancialProduct) -
[FoodService](/FoodService) -
[GovernmentService](/GovernmentService) -
[TaxiService](/TaxiService) -
[WebAPI](/WebAPI)

### Examples

[Example 1](#eg-0375)

Copied

Example notes or example HTML without markup.

An example of a invoice for a purchase and installation. ACME Home Heating Bill for: New furnace and installation Customer: Jane Doe payment due: 2015-01-30 minimum payment: $0.00 total due: $0.00 payment status: paid order: furnace model ABC123 order: installation labor

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Invoice"> <h1 itemprop="description">New furnace and installation</h1> <div itemprop="broker" itemscope itemtype="https://schema.org/LocalBusiness"> <b itemprop="name">ACME Home Heating</b> </div> <div itemprop="customer" itemscope itemtype="https://schema.org/Person"> <b itemprop="name">Jane Doe</b> </div> <time itemprop="paymentDueDate">2015-01-30</time> <div itemprop="minimumPaymentDue" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="price">0.00</span> <span itemprop="priceCurrency">USD</span> </div> <div itemprop="totalPaymentDue" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="price">0.00</span> <span itemprop="priceCurrency">USD</span> </div> <link itemprop="paymentStatus" href="https://schema.org/PaymentComplete" /> <div itemprop="referencesOrder" itemscope itemtype="https://schema.org/Order"> <span itemprop="description">furnace</span> <time itemprop="orderDate">2014-12-01</time> <span itemprop="orderNumber">123ABC</span> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/Product"> <span itemprop="name">ACME Furnace 3000</span> <meta itemprop="productID" content="ABC123" /> </div> </div> <div itemprop="referencesOrder" itemscope itemtype="https://schema.org/Order"> <span itemprop="description">furnace installation</span> <time itemprop="orderDate">2014-12-02</time> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/Service"> <span itemprop="description">furnace installation</span> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Invoice"> <h1 property="description">New furnace and installation</h1> <div property="broker" typeof="LocalBusiness"> <b property="name">ACME Home Heating</b> </div> <div property="customer" typeof="Person"> <b property="name">Jane Doe</b> </div> <time property="paymentDueDate">2015-01-30</time> <div property="minimumPaymentDue" typeof="PriceSpecification"> <span property="price">0.00</span> <span property="priceCurrency">USD</span> </div> <div property="totalPaymentDue" typeof="PriceSpecification"> <span property="price">0.00</span> <span property="priceCurrency">USD</span> </div> <meta itemprop="paymentStatus" content="PaymentComplete" /> <div property="referencesOrder" typeof="Order"> <span property="description">furnace</span> <time property="orderDate">2014-12-01</time> <span property="orderNumber">123ABC</span> <div property="orderedItem" typeof="Product"> <span property="name">ACME Furnace 3000</span> <meta property="productID" content="ABC123" /> </div> </div> <div property="referencesOrder" typeof="Order"> <span property="description">furnace installation</span> <time property="orderDate">2014-12-02</time> <div property="orderedItem" typeof="Service"> <span property="description">furnace installation</span> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Invoice", "broker": { "@type": "LocalBusiness", "name": "ACME Home Heating" }, "accountId": "xxxx-xxxx-xxxx-1234", "customer": { "@type": "Person", "name": "Jane Doe" }, "paymentDueDate": "2015-01-30", "minimumPaymentDue": { "@type": "PriceSpecification", "price": 0.00, "priceCurrency": "USD" }, "totalPaymentDue": { "@type": "PriceSpecification", "price": 0.00, "priceCurrency": "USD" }, "paymentStatus": "https://schema.org/PaymentComplete", "referencesOrder": [ { "@type": "Order", "description": "furnace", "orderDate": "2014-12-01", "orderNumber": "123ABC", "paymentMethod": "http://purl.org/goodrelations/v1#ByInvoice", "orderedItem": { "@type": "Product", "name": "ACME Furnace 3000", "productID": "ABC123" } }, { "@type": "Order", "description": "furnace installation", "orderDate": "2014-12-02", "paymentMethod": "http://purl.org/goodrelations/v1#ByInvoice", "orderedItem": { "@type": "Service", "description": "furnace installation" } } ] } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0396)

Copied

Example notes or example HTML without markup.

ACME Home Cleaning offers a variety of services in Massachusetts, including: <ul> <li>House cleaning</li> <ul> <li>Apartment light cleaning</li> <li>House light cleaning up to 2 bedrooms</li> <li>House light cleaning 3+ bedrooms</li> </ul> <li>One-time services</li> <ul> <li>Window washing</li> <li>Carpet deep cleaning</li> <li>Move in/out cleaning</li> </ul> </ul>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Service"> <meta itemprop="serviceType" content="Home cleaning" /> <span itemprop="provider" itemscope itemtype="https://schema.org/LocalBusiness"> <span itemprop="name">ACME Home Cleaning</span> </span> offers a variety of services in <span itemprop="areaServed" itemscope itemtype="https://schema.org/State"> <span itemprop="name">Massachusetts</span>, including </span> <ul itemprop="hasOfferCatalog" itemscope itemtype="https://schema.org/OfferCatalog"> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <span itemprop="name">House cleaning</span> <ul itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Apartment light cleaning</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">House light cleaning up to 2 bedrooms</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">House light cleaning 3+ bedrooms</span> </div> </li> </ul> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <span itemprop="name">One-time services</span> <ul itemprop="itemListElement" itemscope itemtype="https://schema.org/OfferCatalog"> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Window washing</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Carpet deep cleaning</span> </div> </li> <li itemprop="itemListElement" itemscope itemtype="https://schema.org/Offer"> <div itemprop="itemOffered" itemscope itemtype="https://schema.org/Service"> <span itemprop="name">Move in/out cleaning</span> </div> </li> </ul> </li> </ul> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Service"> <meta property="serviceType" content="Home cleaning" /> <span property="provider" typeof="LocalBusiness"> <span property="name">ACME Home Cleaning</span> </span> offers a variety of services in <span property="areaServed" typeof="State"> <span property="name">Massachusetts</span>, including </span> <ul property="hasOfferCatalog" typeof="OfferCatalog"> <li property="itemListElement" typeof="OfferCatalog"> <span property="name">House cleaning</span> <ul property="itemListElement" typeof="OfferCatalog"> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Apartment light cleaning</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">House light cleaning up to 2 bedrooms</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">House light cleaning 3+ bedrooms</span> </div> </li> </ul> <li property="itemListElement" typeof="OfferCatalog"> <span property="name">One-time services</span> <ul property="itemListElement" typeof="OfferCatalog"> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Window washing</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Carpet deep cleaning</span> </div> </li> <li property="itemListElement" typeof="Offer"> <div property="itemOffered" typeof="Service"> <span property="name">Move in/out cleaning</span> </div> </li> </ul> </li> </ul> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Service", "serviceType": "Weekly home cleaning", "provider": { "@type": "LocalBusiness", "name": "ACME Home Cleaning" }, "areaServed": { "@type": "State", "name": "Massachusetts" }, "hasOfferCatalog": { "@type": "OfferCatalog", "name": "Cleaning services", "itemListElement": [ { "@type": "OfferCatalog", "name": "House Cleaning", "itemListElement": [ { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Apartment light cleaning" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "House light cleaning up to 2 bedrooms" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "House light cleaning 3+ bedrooms" } } ] }, { "@type": "OfferCatalog", "name": "One-time services", "itemListElement": [ { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Window washing" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Carpet cleaning" } }, { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Move in/out cleaning" } } ] } ] } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0421)

Copied

Example notes or example HTML without markup.

Car for hire driver #123 is within 50 meters of a given location, but is moving.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/TaxiService"> <div itemprop="provider" itemscope itemtype="https://schema.org/LocalBusiness"> <span itemprop="name">driver #123</span> <div itemprop="location" itemscope itemtype="https://schema.org/Place"> <div itemprop="geo" itemscope itemtype="https://schema.org/GeoCircle"> <div itemprop="geoMidpoint" itemscope itemtype="https://schema.org/GeoCoordinates"> <meta itemprop="latitude" content="42.362757" /> <meta itemprop="longitude" content="-71.087109" /> </div> <meta itemprop="geoRadius" content="50" /> </div> </div> </div> <meta itemprop="providerMobility" content="dynamic" /> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="TaxiService"> <div property="provider" typeof="LocalBusiness"> <span property="name">driver #123</span> <div property="location" typeof="Place"> <div property="geo" typeof="GeoCircle"> <div property="geoMidpoint" typeof="GeoCoordinates"> <meta property="latitude" content="42.362757" /> <meta property="longitude" content="-71.087109" /> </div> <meta property="geoRadius" content="50" /> </div> </div> </div> <meta property="providerMobility" content="dynamic" /> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "TaxiService", "provider": { "@type": "LocalBusiness", "name": "driver #123", "location": { "@type": "Place", "geo": { "@type": "GeoCircle", "geoMidpoint": { "@type": "GeoCoordinates", "latitude": "42.362757", "longitude": "-71.087109" }, "geoRadius": "50" } } }, "providerMobility": "dynamic" } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0479)

Copied

Example notes or example HTML without markup.

An example of an online repository that hosts scientific research data (JSON-LD only).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.See https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/DataRepository.md for a complete guide. <script type="application/ld+json"> { "@context": { "@vocab": "https://schema.org/" }, "@type": [ "Service", "ResearchProject" ], "legalName": "Sample Data Repository Office", "name": "SDRO", "url": "https://www.sample-data-repository.org", "description": "The Sample Data Repository Service provides access to data from an imaginary domain accessible from this website.", "sameAs": [ "http://www.re3data.org/repository/r3d1000000xx", "https://twitter.com/SDRO", "https://www.linkedin.com/company/123456789/" ], "category": [ "Biological Oceanography", "Chemical Oceanography" ], "provider": [ { "@type": "ResearchProject", "name": "SDRO Technical Office", "description": "We provide all the infrastructure for the SDRO" }, { "@type": "ResearchProject", "name": "SDRO Science Support Office", "description": "We provide all the science support functionality for the SDRO" } ], "logo": { "@type": "ImageObject", "url": "https://www.sample-data-repository.org/images/logo.jpg" }, "contactPoint": { "@type": "ContactPoint", "name": "Support", "email": "info@bco-dmo.org", "url": "https://www.sample-data-repository.org/about-us", "contactType": "customer support" }, "foundingDate": "2006-09-01", "address": { "@type": "PostalAddress", "streetAddress": "123 Main St.", "addressLocality": "Anytown", "addressRegion": "ST", "postalCode": "12345", "addressCountry": "USA" }, "parentOrganization": { "@type": "Organization", "@id": "http://www.someinstitute.edu", "legalName": "Some Institute", "name": "SI", "url": "http://www.someinstitute.edu", "address": { "@type": "PostalAddress", "streetAddress": "234 Main St.", "addressLocality": "Anytown", "addressRegion": "ST", "postalCode": "12345", "addressCountry": "USA" } }, "identifier": { "@type": "PropertyValue", "name": "Re3data DOI: 10.17616/R37P4C", "propertyID": "https://registry.identifiers.org/registry/doi", "value": "doi:10.17616/R37P4C", "url": "https://doi.org/10.17616/R37P4C" }, "funder": { "@type": "Organization", "@id": "https://doi.org/10.13039/100000141", "legalName": "Division of Ocean Sciences", "alternateName": "OCE", "url": "https://www.nsf.gov/div/index.jsp?div=OCE", "identifier": { "@type": "PropertyValue", "propertyID": "https://registry.identifiers.org/registry/doi", "value": "doi:10.13039/100000141", "url": "https://doi.org/10.13039/100000141" }, "parentOrganization": { "@type": "Organization", "@id": "http://doi.org/10.13039/100000085", "legalName": "Directorate for Geosciences", "alternateName": "NSF-GEO", "url": "http://www.nsf.gov", "identifier": { "@type": "PropertyValue", "propertyID": "https://registry.identifiers.org/registry/doi", "value": "doi:10.13039/100000085", "url": "https://doi.org/10.13039/100000085" }, "parentOrganization": { "@type": "Organization", "@id": "http://dx.doi.org/10.13039/100000001", "legalName": "National Science Foundation", "alternateName": "NSF", "url": "http://www.nsf.gov", "identifier": { "@type": "PropertyValue", "propertyID": "https://registry.identifiers.org/registry/doi", "value": "doi:10.13039/100000001", "url": "https://doi.org/10.13039/100000001" } } } }, "availableChannel": [ { "@type": "ServiceChannel", "serviceUrl": "https://www.sample-data-repository.org/search", "providesService": { "@type": "Service", "name": "SDRO Website Search", "description": "Search for webpages, datasets, authors, funding awards, instrumentation and measurements", "potentialAction": { "@type": "SearchAction", "target": "https://www.sample-data-repository.org/search?keywords={query_string}" } } } ], "hasOfferCatalog": { "@type": "OfferCatalog", "name": "Sample Data Repository Resource Catalog", "itemListElement": [ { "@type": "DataCatalog", "@id": "https://www.sample-data-repository.org/collection/biological-data", "name": "Biological Data", "audience": { "@type": "Audience", "audienceType": "public", "name": "General Public" } }, { "@type": "DataCatalog", "@id": "https://www.sample-data-repository.org/collection/geological-data", "name": "Geological Data", "audience": { "@type": "Audience", "audienceType": "public", "name": "General Public" } } ] } } </script>

Structured representation of the JSON-LD example.
