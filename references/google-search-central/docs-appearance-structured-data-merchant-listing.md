---
title: "How To Add Merchant Listing Structured Data | Google Search Central | Documentation | Google for Developers"
source_url: https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2024-11-20
---

# How To Add Merchant Listing Structured Data | Google Search Central | Documentation | Google for Developers

# Merchant listing (`Product`

, `Offer`

) structured data

When you add `Product`

markup to your page, it can be eligible for display in merchant
listing experiences on Google Search, including the shopping knowledge panel,
Google Images, popular product results, and product snippets. Merchant listings can
highlight more specific data about a product, such as its price, availability, and shipping and
return information.

This guide focuses on the `Product`

structured data requirements for
merchant listings. If you're not sure which markup to use, read our
[intro to Product markup](/search/docs/appearance/structured-data/product).

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page
content. If you're new to structured data, you can learn more about
[how structured data works](/search/docs/appearance/structured-data/intro-structured-data).

Here's an overview of how to build, test, and release structured data.

- Add the
[required properties](#structured-data-type-definitions). Based on the format you're using, learn where to[insert structured data on the page](/search/docs/appearance/structured-data/intro-structured-data#format-placement). - Follow the
[guidelines](#guidelines). - Validate your code using the
[Rich Results Test](https://search.google.com/test/rich-results)and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results). - Deploy a few pages that include your structured data and use the
[URL Inspection tool](https://support.google.com/webmasters/answer/9012289)to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the`noindex`

tag, or login requirements. If the page looks okay, you can[ask Google to recrawl your URLs](/search/docs/crawling-indexing/ask-google-to-recrawl). - To keep Google informed of future changes, we recommend that you
[submit a sitemap](/search/docs/crawling-indexing/sitemaps/build-sitemap). You can automate this with the[Search Console Sitemap API](/webmaster-tools/v1/sitemaps).

## Examples

The following examples illustrate how to include structured data on your web pages for different situations.

### Product page with an offer

Here's an example of a product page selling a product, with product reviews.

#### JSON-LD

<html> <head> <title>Executive Anvil</title> <script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Product", "name": "Executive Anvil", "image": [ "https://example.com/photos/1x1/photo.jpg", "https://example.com/photos/4x3/photo.jpg", "https://example.com/photos/16x9/photo.jpg" ], "description": "Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height.", "sku": "0446310786", "mpn": "925872", "brand": { "@type": "Brand", "name": "ACME" }, "review": { "@type": "Review", "reviewRating": { "@type": "Rating", "ratingValue": 4, "bestRating": 5 }, "author": { "@type": "Person", "name": "Fred Benson" } }, "aggregateRating": { "@type": "AggregateRating", "ratingValue": 4.4, "reviewCount": 89 }, "offers": { "@type": "Offer", "url": "https://example.com/anvil", "priceCurrency": "USD", "price": 119.99, "priceValidUntil": "2024-11-20", "itemCondition": "https://schema.org/UsedCondition", "availability": "https://schema.org/InStock" } } </script> </head> <body> </body> </html>

#### RDFa

<html> <head> <title>Executive Anvil</title> </head> <body> <div typeof="schema:Product"> <div rel="schema:review"> <div typeof="schema:Review"> <div rel="schema:reviewRating"> <div typeof="schema:Rating"> <div property="schema:ratingValue" content="4"></div> <div property="schema:bestRating" content="5"></div> </div> </div> <div rel="schema:author"> <div typeof="schema:Person"> <div property="schema:name" content="Fred Benson"></div> </div> </div> </div> </div> <div rel="schema:image" resource="https://example.com/photos/4x3/photo.jpg"></div> <div property="schema:mpn" content="925872"></div> <div property="schema:name" content="Executive Anvil"></div> <div property="schema:description" content="Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height."></div> <div rel="schema:image" resource="https://example.com/photos/1x1/photo.jpg"></div> <div rel="schema:brand"> <div typeof="schema:Brand"> <div property="schema:name" content="ACME"></div> </div> </div> <div rel="schema:aggregateRating"> <div typeof="schema:AggregateRating"> <div property="schema:reviewCount" content="89"></div> <div property="schema:ratingValue" content="4.4"></div> </div> </div> <div rel="schema:offers"> <div typeof="schema:Offer"> <div property="schema:price" content="119.99"></div> <div property="schema:availability" content="https://schema.org/InStock"></div> <div property="schema:priceCurrency" content="USD"></div> <div property="schema:priceValidUntil" datatype="xsd:date" content="2024-11-20"></div> <div rel="schema:url" resource="https://example.com/anvil"></div> <div property="schema:itemCondition" content="https://schema.org/UsedCondition"></div> </div> </div> <div rel="schema:image" resource="https://example.com/photos/16x9/photo.jpg"></div> <div property="schema:sku" content="0446310786"></div> </div> </body> </html>

#### Microdata

<html> <head> <title>Executive Anvil</title> </head> <body> <div> <div itemtype="https://schema.org/Product" itemscope> <meta itemprop="mpn" content="925872" /> <meta itemprop="name" content="Executive Anvil" /> <link itemprop="image" href="https://example.com/photos/16x9/photo.jpg" /> <link itemprop="image" href="https://example.com/photos/4x3/photo.jpg" /> <link itemprop="image" href="https://example.com/photos/1x1/photo.jpg" /> <meta itemprop="description" content="Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height." /> <div itemprop="offers" itemtype="https://schema.org/Offer" itemscope> <link itemprop="url" href="https://example.com/anvil" /> <meta itemprop="availability" content="https://schema.org/InStock" /> <meta itemprop="priceCurrency" content="USD" /> <meta itemprop="itemCondition" content="https://schema.org/UsedCondition" /> <meta itemprop="price" content="119.99" /> <meta itemprop="priceValidUntil" content="2024-11-20" /> </div> <div itemprop="aggregateRating" itemtype="https://schema.org/AggregateRating" itemscope> <meta itemprop="reviewCount" content="89" /> <meta itemprop="ratingValue" content="4.4" /> </div> <div itemprop="review" itemtype="https://schema.org/Review" itemscope> <div itemprop="author" itemtype="https://schema.org/Person" itemscope> <meta itemprop="name" content="Fred Benson" /> </div> <div itemprop="reviewRating" itemtype="https://schema.org/Rating" itemscope> <meta itemprop="ratingValue" content="4" /> <meta itemprop="bestRating" content="5" /> </div> </div> <meta itemprop="sku" content="0446310786" /> <div itemprop="brand" itemtype="https://schema.org/Brand" itemscope> <meta itemprop="name" content="ACME" /> </div> </div> </div> </body> </html>

### Pricing

Google recognizes three kinds of prices:

- Active price
- The price at which the product is currently offered.
- Strikethrough price
- During a sale, the higher regular price at which the product is normally offered. It may be displayed as a struck-through price to draw attention to a lowered active price.
- Member price
- The price at which the product is offered to a member of a particular loyalty program.

These prices are encoded using price specifications under the `Offer`

object (with the
exception of the active price, which can also be encoded at the offer level). The respective price
specifications are identified by the price specification properties `priceType`

and `validForMemberTier`

, which must not be used together:

- Active prices have neither a
`priceType`

nor a`validForMemberTier`

property. - Strikethrough prices set the
`priceType`

property to`StrikethroughPrice`

(for a transition period,`ListPrice`

is also allowed) and cannot have a`validForMemberTier`

property. - Member prices are marked with a
`validForMemberTier`

property and cannot have a`priceType`

property.

Price specifications containing both of these properties are ignored.

### Active price

Here are two examples of encoding the active price in JSON-LD. The active price can be specified
using the `price`

property as follows:

"offers": { "@type": "Offer","price": 10.00, "priceCurrency": "USD",... }

Alternatively, the active price can be specified using the `priceSpecification`

property.

"offers": { "@type": "Offer","priceSpecification": { "@type": "UnitPriceSpecification", "price": 10.00, "priceCurrency": "USD" },... }

### Sale pricing

The following example shows a product with a sale price. The current, active price automatically
becomes a sale price when you provide a second price with the original, strikethrough price and
mark it with a [ priceType](#pricetype) property of
value

`https://schema.org/StrikethroughPrice`

. Don't mark the active price with
a `priceType`

property.
{ "@context": "https://schema.org/", "@type": "Product", "name": "Nice trinket", "offers": { "@type": "Offer", "url": "https://www.example.com/trinket_offer","price": 10.00, "priceCurrency": "GBP", "priceSpecification": { "@type": "UnitPriceSpecification", "priceType": "https://schema.org/StrikethroughPrice", "price": 15.00, "priceCurrency": "GBP" }} }

Alternatively, you can use two `UnitPriceSpecification`

objects to specify the sale
price and the strikethrough price:

{ "@context": "https://schema.org/", "@type": "Product", "name": "Nice trinket", "offers": { "@type": "Offer","priceSpecification": [ { "@type": "UnitPriceSpecification", "price": 10.00, "priceCurrency": "GBP" }, { "@type": "UnitPriceSpecification", "priceType": "https://schema.org/StrikethroughPrice", "price": 15.00, "priceCurrency": "GBP" } ]} }

### Member prices

Here are four examples of encoding a member price. In the first example, the active price is
specified with the `price`

property at the offer level, and the member price is given
in a price specification marked with
the [ validForMemberTier](#validForMemberTier) property:

"offers": { "@type": "Offer", "url": "https://www.example.com/trinket_offer", "price": 10.00, "priceCurrency": "GBP","priceSpecification": { "@type": "UnitPriceSpecification", "price": 8.00, "priceCurrency": "GBP", "validForMemberTier": { "@type": "MemberProgramTier", "@id": "https://www.example.com/com/members#tier_gold" } }}

The second example shows both the active price and the member price encoded with price specifications:

"offers": { "@type": "Offer", "url": "https://www.example.com/trinket_offer","priceSpecification": [ { "@type": "UnitPriceSpecification", "price": 10.00, "priceCurrency": "GBP" }, { "@type": "UnitPriceSpecification", "price": 8.00, "priceCurrency": "GBP", "validForMemberTier": { "@type": "MemberProgramTier", "@id": "https://www.example.com/com/members#tier_gold" } } ]}

The third example demonstrates how to encode a sale price, a strikethrough price, and member prices for several loyalty program tiers in a single offer:

"offers": { "@type": "Offer", "url": "https://www.example.com/trinket_offer","priceSpecification": [ { "@type": "UnitPriceSpecification", "price": 9.00, "priceCurrency": "GBP" }, { "@type": "UnitPriceSpecification", "priceType": "https://schema.org/StrikethroughPrice", "price": 10.00, "priceCurrency": "GBP" }, { "@type": "UnitPriceSpecification", "price": 8.00, "priceCurrency": "GBP", "validForMemberTier": { "@type": "MemberProgramTier", "@id": "https://www.example.com/com/members#tier_silver" } }, { "@type": "UnitPriceSpecification", "price": 7.00, "priceCurrency": "GBP", "validForMemberTier": [ { "@type": "MemberProgramTier", "@id": "https://www.example.com/com/members#tier_gold" }, { "@type": "MemberProgramTier", "@id": "https://www.example.com/com/members#tier_platinum" } ] } ]}

The active price could also be encoded at the offer level, as shown in the first example.

In the fourth example, the member price specification shows membership points instead of a member price:

"offers": { "@type": "Offer", "url": "https://www.example.com/trinket_offer", "price": 10.00, "priceCurrency": "GBP","priceSpecification": { "@type": "UnitPriceSpecification", "membershipPointsEarned": 20, "validForMemberTier": { "@type": "MemberProgramTier", "@id": "https://www.example.com/com/members#tier_gold" } }}

### Pricing with unit pricing measures

Here is an example of how to specify a price for 200 ml of a product that is customarily sold in multiples of 100 ml. For example, if you were selling a 200 ml bottle of perfume, you could show customers how much your perfume costs per 100 ml. The following example shows that the perfume costs €100 per 100 ml, which means a 200 ml bottle of perfume would cost €200. This form of pricing is particularly important in the EU, New Zealand, and Australia for products sold by volume, length, or weight.

When the [unit pricing measure](https://support.google.com/merchants/answer/6324455)
and [unit pricing base measure](https://support.google.com/merchants/answer/6324490)
are present, specify the active price inside
a `UnitPriceSpecification`

and use the
[ referenceQuantity](#referenceQuantity) property to provide the unit
pricing.

"offers": { "@type": "Offer", "url": "https://www.example.com/perfume_offer", "priceSpecification": { "@type": "UnitPriceSpecification", "price": 200.00, "priceCurrency": "EUR","referenceQuantity": { "@type": "QuantitativeValue", "value": "200", "unitCode": "ML", "valueReference": { "@type": "QuantitativeValue", "value": "100", "unitCode": "ML" } }} }

### Shipping details

Here's an example of a product page with shipping details. This example would
result in a shipping rate of $3.49 for all users that live in
the US. For more examples, review the
[Shipping](#shipping) section.

#### JSON-LD

<html> <head> <title>Nice trinket</title> <script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Product", "sku": "trinket-12345", "gtin14": "00012345600012", "image": [ "https://example.com/photos/16x9/trinket.jpg", "https://example.com/photos/4x3/trinket.jpg", "https://example.com/photos/1x1/trinket.jpg" ], "name": "Nice trinket", "description": "Trinket with clean lines", "brand": { "@type": "Brand", "name": "MyBrand" }, "offers": { "@type": "Offer", "url": "https://www.example.com/trinket_offer", "itemCondition": "https://schema.org/NewCondition", "availability": "https://schema.org/InStock", "price": 39.99, "priceCurrency": "USD", "priceValidUntil": "2024-11-20", "shippingDetails": { "@type": "OfferShippingDetails", "shippingRate": { "@type": "MonetaryAmount", "value": 3.49, "currency": "USD" }, "shippingDestination": { "@type": "DefinedRegion", "addressCountry": "US" }, "deliveryTime": { "@type": "ShippingDeliveryTime", "handlingTime": { "@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY" }, "transitTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 5, "unitCode": "DAY" } } } }, "review": { "@type": "Review", "reviewRating": { "@type": "Rating", "ratingValue": 4, "bestRating": 5 }, "author": { "@type": "Person", "name": "Fred Benson" } }, "aggregateRating": { "@type": "AggregateRating", "ratingValue": 4.4, "reviewCount": 89 } } </script> </head> <body> </body> </html>

#### RDFa

<html> <head> <title>Nice trinket</title> </head> <body> <div typeof="schema:Product"> <div property="schema:sku" content="trinket-12345"></div> <div property="schema:gtin14" content="00012345600012"></div> <div property="schema:name" content="Nice trinket"></div> <div rel="schema:image" resource="https://example.com/photos/16x9/trinket.jpg"></div> <div rel="schema:image" resource="https://example.com/photos/4x3/trinket.jpg"></div> <div rel="schema:image" resource="https://example.com/photos/1x1/trinket.jpg"></div> <div property="schema:description" content="Trinket with clean lines"></div> <div rel="schema:brand"> <div typeof="schema:Brand"> <div property="schema:name" content="MyBrand"></div> </div> </div> <div rel="schema:offers"> <div typeof="schema:Offer"> <div rel="schema:url" resource="https://example.com/trinket_offer"></div> <div property="schema:itemCondition" content="https://schema.org/NewCondition"></div> <div property="schema:availability" content="https://schema.org/InStock"></div> <div property="schema:price" content="39.99"></div> <div property="schema:priceCurrency" content="USD"></div> <div property="schema:priceValidUntil" datatype="xsd:date" content="2024-11-20"></div> <div rel="schema:shippingDetails"> <div typeof="schema:OfferShippingDetails"> <div rel="schema:shippingRate"> <div typeof="schema:MonetaryAmount"> <div property="schema:value" content="3.49"></div> <div property="schema:currency" content="USD"></div> </div> </div> <div rel="schema:shippingDestination"> <div typeof="schema:DefinedRegion"> <div property="schema:addressCountry" content="US"></div> </div> </div> <div rel="schema:deliveryTime"> <div typeof="schema:ShippingDeliveryTime"> <div rel="schema:handlingTime"> <div typeof="schema:QuantitativeValue"> <div property="schema:minValue" content="0"></div> <div property="schema:maxValue" content="1"></div> <div property="schema:unitCode" content="DAY"></div> </div> </div> <div rel="schema:transitTime"> <div typeof="schema:QuantitativeValue"> <div property="schema:minValue" content="1"></div> <div property="schema:maxValue" content="5"></div> <div property="schema:unitCode" content="DAY"></div> </div> </div> </div> </div> </div> </div> </div> </div> <div rel="schema:review"> <div typeof="schema:Review"> <div rel="schema:reviewRating"> <div typeof="schema:Rating"> <div property="schema:ratingValue" content="4"></div> <div property="schema:bestRating" content="5"></div> </div> </div> <div rel="schema:author"> <div typeof="schema:Person"> <div property="schema:name" content="Fred Benson"></div> </div> </div> </div> </div> <div rel="schema:aggregateRating"> <div typeof="schema:AggregateRating"> <div property="schema:reviewCount" content="89"></div> <div property="schema:ratingValue" content="4.4"></div> </div> </div> </div> </body> </html>

#### Microdata

<html> <head> <title>Nice trinket</title> </head> <body> <div> <div itemtype="https://schema.org/Product" itemscope> <meta itemprop="sku" content="trinket-12345" /> <meta itemprop="gtin14" content="00012345600012" /> <meta itemprop="name" content="Nice trinket" /> <link itemprop="image" href="https://example.com/photos/16x9/trinket.jpg" /> <link itemprop="image" href="https://example.com/photos/4x3/trinket.jpg" /> <link itemprop="image" href="https://example.com/photos/1x1/trinket.jpg" /> <meta itemprop="description" content="Trinket with clean lines" /> <div itemprop="brand" itemtype="https://schema.org/Brand" itemscope> <meta itemprop="name" content="MyBrand" /> </div> <div itemprop="offers" itemtype="https://schema.org/Offer" itemscope> <link itemprop="url" href="https://www.example.com/trinket_offer" /> <meta itemprop="itemCondition" content="https://schema.org/NewCondition" /> <meta itemprop="availability" content="https://schema.org/InStock" /> <meta itemprop="price" content="39.99" /> <meta itemprop="priceCurrency" content="USD" /> <meta itemprop="priceValidUntil" content="2024-11-20" /> <div itemprop="shippingDetails" itemtype="https://schema.org/OfferShippingDetails" itemscope> <div itemprop="shippingRate" itemtype="https://schema.org/MonetaryAmount" itemscope> <meta itemprop="value" content="3.49" /> <meta itemprop="currency" content="USD" /> </div> <div itemprop="shippingDestination" itemtype="https://schema.org/DefinedRegion" itemscope> <meta itemprop="addressCountry" content="US" /> </div> <div itemprop="deliveryTime" itemtype="https://schema.org/ShippingDeliveryTime" itemscope> <div itemprop="handlingTime" itemtype="https://schema.org/QuantitativeValue" itemscope> <meta itemprop="minValue" content="0" /> <meta itemprop="maxValue" content="1" /> <meta itemprop="unitCode" content="DAY" /> </div> <div itemprop="transitTime" itemtype="https://schema.org/QuantitativeValue" itemscope> <meta itemprop="minValue" content="1" /> <meta itemprop="maxValue" content="5" /> <meta itemprop="unitCode" content="DAY" /> </div> </div> </div> </div> <div itemprop="review" itemtype="https://schema.org/Review" itemscope> <div itemprop="author" itemtype="https://schema.org/Person" itemscope> <meta itemprop="name" content="Fred Benson" /> </div> <div itemprop="reviewRating" itemtype="https://schema.org/Rating" itemscope> <meta itemprop="ratingValue" content="4" /> <meta itemprop="bestRating" content="5" /> </div> </div> <div itemprop="aggregateRating" itemtype="https://schema.org/AggregateRating" itemscope> <meta itemprop="reviewCount" content="89" /> <meta itemprop="ratingValue" content="4.4" /> </div> </div> </div> </body> </html>

### Free shipping

Here's an example of providing free shipping to buyers in the US state of New York.

"shippingDetails": { "@type": "OfferShippingDetails", "shippingRate": { "@type": "MonetaryAmount", "value": "0", "currency": "USD" }, "shippingDestination": [ { "@type": "DefinedRegion", "addressCountry": "US", "addressRegion": ["NY"] } ] }

### Return details

Here is an example of a product page with return details. The markup matches a return policy that requires products sold in Switzerland to be returned by mail within 60 days and charges a return fee of 3.49 Swiss Francs.

{ "@context": "https://schema.org/", "@type": "Product", "sku": "trinket-12345", "gtin14": "00012345600012", "image": [ "https://example.com/photos/16x9/trinket.jpg", "https://example.com/photos/4x3/trinket.jpg", "https://example.com/photos/1x1/trinket.jpg" ], "name": "Nice trinket", "description": "Trinket with clean lines", "brand": { "@type": "Brand", "name": "MyBrand" }, "offers": { "@type": "Offer", "url": "https://www.example.com/trinket_offer", "itemCondition": "https://schema.org/NewCondition", "availability": "https://schema.org/InStock", "priceSpecification": { "@type": "PriceSpecification", "price": 39.99, "priceCurrency": "CHF" },"hasMerchantReturnPolicy": { "@type": "MerchantReturnPolicy", "applicableCountry": "CH", "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow", "merchantReturnDays": 60, "returnMethod": "https://schema.org/ReturnByMail", "returnFees": "https://schema.org/ReturnShippingFees", "returnShippingFeesAmount": { "@type": "MonetaryAmount", "value": 3.49, "currency": "CHF" } }} }

### Certifications

The following examples illustrate how to specify certification information using structured data. The first example specifies the German CO2 emissions class "D" for a vehicle.

{ "@context": "https://schema.org/", "@type": "Product", "sku": "1234-5678", "image": "https://www.example.com/vehicle.jpg", "name": "Big Car", "description": "Passenger vehicle with combustion engine", "gtin14": "00012345600012", "mpn": "WH1234", "brand": { "@type": "Brand", "name": "ExampleCarBrand" },"hasCertification": { "@type": "Certification", "issuedBy": { "@type": "Organization", "name": "BMWK" }, "name": "Vehicle_CO2_Class", "certificationRating": { "@type": "Rating", "ratingValue": "D" } },"offers": { "@type": "Offer", "url": "https://www.example.com/vehicle", "itemCondition": "https://schema.org/NewCondition", "availability": "https://schema.org/InStock", "price": 17999.00, "priceCurrency": "EUR" } }

The second example specifies an EPREL energy efficiency label for an LED:

{ "@context": "https://schema.org/", "@type": "Product", "sku": "1234-5678", "image": "https://www.example.com/led.jpg", "name": "LED", "description": "Dimmable LED", "gtin14": "00012345600012", "mpn": "WH1234", "brand": { "@type": "Brand", "name": "ExampleLightingBrand" },"hasCertification": { "@type": "Certification", "issuedBy": { "@type": "Organization", "name": "European_Commission" }, "name": "EPREL", "certificationIdentification": "123456" },"offers": { "@type": "Offer", "url": "https://www.example.com/led", "itemCondition": "https://schema.org/NewCondition", "availability": "https://schema.org/InStock", "price": 2.30, "priceCurrency": "EUR" } }

### 3D model

This example shows how to link a 3D model to a product with the `subjectOf`

property
and the `3DModel`

type.

{ "@context": "https://schema.org/", "@type": "Product", "sku": "1234-5678", "image": "https://www.example.com/sofa.jpg", "name": "Water heater", "description": "White 3-Seat Sofa", "gtin14": "00012345600012", "mpn": "S1234W3", "brand": { "@type": "Brand", "name": "ExampleSofaBrand" },"subjectOf": { "@type": "3DModel", "encoding": { "@type": "MediaObject", "contentUrl": "https://example.com/sofa.gltf" } },"offers": { "@type": "Offer", "url": "https://www.example.com/whitechaiselongue", "itemCondition": "https://schema.org/NewCondition", "availability": "https://schema.org/InStock", "price": 1299.00, "priceCurrency": "USD" } }

## Guidelines

For your `Product`

markup to be eligible for merchant listing experiences, you must follow these guidelines:

[General structured data guidelines](/search/docs/appearance/structured-data/sd-policies)[Search Essentials](/search/docs/essentials)[Technical guidelines](#technical-guidelines)[Content guidelines](#content-guidelines)[Free listings guidelines](https://support.google.com/merchants/answer/12073010)(for merchant listing experiences)

### Technical guidelines

- Only pages where a shopper can purchase a product are eligible for merchant listing experiences, not pages with links to other sites that sell the product. Google may attempt to verify merchant listing product data before showing the information in search results.
- Product rich results only support pages that focus on a single product (or multiple variants
of the same product). For example, "shoes in our shop" is not a specific product.
This includes product variants where
[each product variant has a distinct URL](/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites#how-google-understands-urls-for-product-variants). We recommend focusing on adding markup to product pages instead of pages that list products or a category of products. - For details about how to mark up product variants, refer to
[product variant structured data documentation](/search/docs/appearance/structured-data/product-variants). - When offering products for sale in multiple currencies, have a distinct URL per currency. For example, if a product is available for sale in Canadian and US dollars, use two distinct URLs, one per currency.
isn't supported automatically as a subtype of Product. For now, include both`Car`

and`Car`

types if you want to attach ratings to it and be eligible for the Search feature. For example in JSON-LD:`Product`

{ "@context": "https://schema.org", "@type": ["Product", "Car"], ... }

- If you're a merchant optimizing for all types of shopping results, we recommend putting
`Product`

structured data in the initial HTML for best results. **For JavaScript-generated**: Be aware that`Product`

markup[dynamically-generated markup](/search/docs/appearance/structured-data/generate-structured-data-with-javascript)can make Shopping crawls less frequent and less reliable, which can be an issue for fast-changing content like product availability and price. If you're using JavaScript to generate`Product`

markup, make sure your server has enough computing resources to handle increased traffic from Google.

### Content guidelines

- We don't allow content that promotes widely prohibited or regulated goods, services, or information that may facilitate serious, immediate, or long term harm to people. This includes content related to firearms and weapons, recreational drugs, tobacco and vaping products, and gambling-related products.

## Structured data type definitions

You must include the required properties for your content to be eligible for display as a rich result. You can also include the recommended properties to add more information to your structured data, which could provide a better user experience.

### Product information

`Product`


The full definition of `Product`

is available at
[schema.org/Product](https://schema.org/Product). When you mark up
your content for product information, use the following properties of the
`Product`

type:

| Required properties | |
|---|---|
`name` |
The name of the product. |
`image` |
Repeated The URL of a product photo. Pictures clearly showing the product (for example, against a white background) are preferred. Additional image guidelines: - Image URLs must be crawlable and indexable. To check if Google can access your URLs, use
the
[URL Inspection tool](https://support.google.com/webmasters/answer/9012289). - Images must represent the marked up content.
- Images must be in a file format that's
[supported by Google Images](/search/docs/appearance/google-images#supported-image-formats). - For best results, we recommend providing multiple high-resolution images (minimum of 50K pixels when multiplying width and height) with the following aspect ratios: 16x9, 4x3, and 1x1.
For example: "image": [ "https://example.com/photos/1x1/photo.jpg", "https://example.com/photos/4x3/photo.jpg", "https://example.com/photos/16x9/photo.jpg" ] |
`offers` |
A nested Product snippets accept an `AggregateOffer`
but merchant listings require an
`Offer` |

| Recommended properties | |
|---|---|
`aggregateRating` |
A nested |
`audience` |
Optional information about the suggested audience for the product, such as the
suggested gender and age group. Only the |
`brand.name` |
Include the brand of the product in the
|
`color` |
The color or color combination of the product (for example, "red" or "yellow/sky blue").
See also the
|
`description` |
The product description. While the product description is not mandatory, it is strongly recommended to provide a description of the product in this property. |
`gtin | gtin8 | gtin12 | gtin13 | gtin14 | isbn` |
Include all applicable global identifiers; these are described at
{ "@context": "https://schema.org", "@type": ["Product", "Book"], ... } |
`hasAdultConsideration` |
Indicates that the product is designated as adult-oriented for example, because it
contains nudity or sexual content. If you sell products that are considered adult-oriented according to Google's
|
`hasCertification` |
Certifications, such as energy efficiency ratings, associated with a product. Up to
10 certifications can be specified. This property is particularly relevant in
European countries. See also the list of |
`inProductGroupWithID` |
The ID of a product group that this product variant belongs to. See also
|
`isVariantOf` |
A product group that this product variant belongs to, if applicable. For details on
how to add markup for product variants, refer to
|
`material` |
The material or material combination the product is made from, such as "Leather"
or "Cotton/Polyester". See also
|
`mpn` |
The manufacturer part number. This property uniquely identifies the product for a given manufacturer. |
`pattern` |
The pattern of the product, such as "polka dots" or "striped". See also
|
`review` |
A nested `Product` schema.org type.If you add a review for the product, the reviewer's name must be a valid name for a
|
`size` |
The size of the product, such as "XL" or "medium". See also |
`sku` |
The merchant-specific identifier for the product. Specify at most one value. - The
`sku` value must use unicode characters that are valid for interchange. - The
`sku` value must not contain any whitespace characters (as defined by the[Unicode whitespace property](https://en.wikipedia.org/wiki/Unicode_character_property#Whitespace)). - We recommend that the
`sku` value only contain ASCII characters.
|
`subjectOf` |
A 3D model for the product, if applicable. See the list of `3DModel` value. |

`3DModel`


The full definition of `3DModel`

is available at

.
[schema.org/3DModel](https://schema.org/3DModel)

Use the following properties to link to a 3D model. Currently only models in [glTF](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html) format are supported.

| Required properties | |
|---|---|
`encoding` |
The media for the 3D model. |
`encoding.contentUrl` |
The link to a 3D model definition file in |

### Offer details

`Offer`


The full definition of `Offer`

is available at
[schema.org/Offer](https://schema.org/Offer). When marking up
offers within a product, use the following properties of the `schema.org`

[ Offer](https://schema.org/Offer) type.

| Required properties | |
|---|---|
`price` or `priceSpecification.price` |
The current, active offer price of a product. Follow the
Here's an example of the "offers": { "@type": "Offer", Unlike product snippets, merchant listing experiences require a price greater than zero.
The active price is required but may be nested inside a
|
`priceCurrency` or `priceSpecification.priceCurrency` |
The currency used to describe the product price, in three-letter
|
`priceSpecification` |
The active price can also be specified using The
|

| Recommended properties | |
|---|---|
`availability` |
The possible product availability options. The short names without the URL prefix
are also supported (for example `https://schema.org/BackOrder` : The item is on back order.`https://schema.org/Discontinued` : The item has been discontinued.`https://schema.org/InStock` : The item is in stock.`https://schema.org/InStoreOnly` : The item is only available for purchase in store.`https://schema.org/LimitedAvailability` : The item has limited availability.`https://schema.org/OnlineOnly` : The item is available online only.`https://schema.org/OutOfStock` : The item is currently out of stock.`https://schema.org/PreOrder` : The item is available for pre-order.`https://schema.org/PreSale` : The item is available for ordering and delivery before general availability.`https://schema.org/SoldOut` : The item has been sold out.
Don't specify more than one value. |
`hasMerchantReturnPolicy` |
Nested information about the return policies associated with an |
`itemCondition` |
Condition of the item offered for sale. The short names without the URL prefix
are also supported (for example `https://schema.org/NewCondition` : The item is new.`https://schema.org/RefurbishedCondition` : The item has been refurbished.`https://schema.org/UsedCondition` : The item is used (it is not new).
Don't specify more than one value. |
`shippingDetails` |
Nested information about the shipping policy associated with an
|
`url` |
A URL of the product web page from which a shopper can purchase the product. This URL may be the preferred URL for the current page with all variant options appropriately selected. The URL can be omitted. Don't provide multiple URLs. For details on how to add markup for product variants, refer to
|

`UnitPriceSpecification`


The full definition of `UnitPriceSpecification`

is available at

.
Use the following properties to capture more complex pricing schemes.
[schema.org/UnitPriceSpecification](https://schema.org/UnitPriceSpecification)

| Required properties | |
|---|---|
`price` |
The offer price of a product. See also the |
`priceCurrency` |
The currency used to describe the product price, in three-letter
|

| Recommended properties | |
|---|---|
`membershipPointsEarned` |
The (whole) number of points that members of a particular loyalty program earn with
this purchase. Use this property only together with
|
`priceType` |
The presence of this property marks the full, original listing price of a product,
if applicable. Only use this property if you want Google to show sale pricing for
your product. You must set the
If you use the
`priceSpecification` |
`referenceQuantity` |
The quantity of the product offered for the given price. See the
example |
`validForMemberTier` |
The presence of this property indicates that this price is valid for members of a particular loyalty program. You can specify multiple member tiers if the price is the same for them and multiple price specifications with this property if the price is different for different member tiers.
If you use the
`priceSpecification` |

If both `priceType`

and `validForMemberTier`

are used, the price
specification is ignored.

`QuantitativeValue`

(for unit pricing)

This section talks about using `QuantitativeValue`

for
the `referenceQuantity`

property of a unit pricing specification.
(`QuantitativeValue`

is also used for shipping durations, but with different
rules.) The full definition of `QuantitativeValue`

is available at

.
[schema.org/QuantitativeValue](https://schema.org/QuantitativeValue)

`QuantitativeValue`

can be used for pricing that is based on a unit measure, such
as buying flooring per square meter, or liquids per half gallon. See the example
[Pricing with unit pricing measures](#unit-pricing-example) and the article
[Unit pricing measure](https://support.google.com/merchants/answer/6324455)
in Google Merchant Center Help for a detailed discussion on unit
pricing.

Use the following properties to capture unit pricing details.

| Required properties | |
|---|---|
`unitCode` |
The unit of measurement. Either the UN/CEFACT codes or their human-readable
equivalents as listed in Google Merchant Center Help
|
`value` |
The numeric value of the unit sold. |

| Recommended properties | |
|---|---|
`valueReference` |
The base quantity in which the product is priced. |

`SizeSpecification`


The `SizeSpecification`

type is used to indicate the size of a product.
The full definition of the type is available at

.
[schema.org/SizeSpecification](https://schema.org/SizeSpecification)

| Recommended properties | |
|---|---|
`name` |
A human readable name for the size, such as "XL". See the
|
`sizeGroup` |
The suggested size group for the product, if applicable. The interpretation of
the group is defined by the `https://schema.org/WearableSizeGroupRegular` : The item size is "regular".`https://schema.org/WearableSizeGroupPetite` : The item size is "petite".`https://schema.org/WearableSizeGroupPlus` : The item size is "plus".`https://schema.org/WearableSizeGroupTall` : The item size is "tall".`https://schema.org/WearableSizeGroupBig` : The item size is "big".`https://schema.org/WearableSizeGroupMaternity` : The item size is "maternity".
The short names without the URL prefix are also supported (for example, See also
`size_type` as well
(`regular` , `petite` , `plus` , `tall` ,
`big` , and `maternity` ), but other search engines may not,
so it is recommended to use the standard `schema.org` enumeration values. |
`sizeSystem` |
The size system for the product, if applicable. Supported values are: `https://schema.org/WearableSizeSystemAU` : The size system in Australia.`https://schema.org/WearableSizeSystemBR` : The size system in Brazil.`https://schema.org/WearableSizeSystemCN` : The size system in China.`https://schema.org/WearableSizeSystemDE` : The size system in Germany.`https://schema.org/WearableSizeSystemEurope` : The size system in Europe.`https://schema.org/WearableSizeSystemFR` : The size system in France.`https://schema.org/WearableSizeSystemIT` : The size system in Italy.`https://schema.org/WearableSizeSystemJP` : The size system in Japan.`https://schema.org/WearableSizeSystemMX` : The size system in Mexico.`https://schema.org/WearableSizeSystemUK` : The size system in the United Kingdom.`https://schema.org/WearableSizeSystemUS` : The size system in the United States.
The short names without the URL prefix are also supported (for example, See also `size_system` as well
(for example, `UR` , `BR` , `CN` , `DE` , `EU` ), but other search engines may not,
so it is recommended to use the standard `schema.org` enumeration values. |

`PeopleAudience`


The full definition of `PeopleAudience`

is available at

.
[schema.org/PeopleAudience](https://schema.org/PeopleAudience)

Use the following properties when indicating the recommended audience for a product.
See also [Supported structured data attributes and values](https://support.google.com/merchants/answer/6386198)
in Google Merchant Center Help.

| Recommended properties | |
|---|---|
`suggestedGender` |
The suggested gender the product is suitable for. Must be one of the following values: `https://schema.org/Male` `https://schema.org/Female` `Unisex` : This (case-insensitive) value is not in the schema.org standard and must not have a`https://schema.org/` prefix.
See Note that Google will complete |
`suggestedMaxAge` (or `suggestedAge.maxValue` ) |
The suggested maximum age for the product, in years. Google maps the maximum suggested ages for products onto the following fixed set of numerical values: `0.25` : For newborns`1.0` : For infants`5.0` : For toddlers`13.0` : For kids
|
`suggestedMinAge` (or `suggestedAge.minValue` ) |
The suggested minimum age for the product, in years. Google maps the minimum suggested ages for products onto the following fixed set of numerical values: `0` : For newborns`0.25` : For infants`1.0` : For toddlers`5.0` : For kids`13.0` : For adults
|

`Certification`


The full definition of `Certification`

is available at

.[schema.org/Certification](https://schema.org/Certification)

Use the following properties to specify the certification.

| Required properties | |
|---|---|
`issuedBy` |
The authority or certification body responsible for issuing the certification. Use the property `EC` or`European_Commission` for energy labels in the EU`ADEME` for French CO2 emissions classes for vehicles`BMWK` for German CO2 emissions classes for vehicles
| `name` |
The name of the certification. At this time, we support the following values: `EPREL` , which represents energy efficiency certifications in the EU European Registry for Energy Labeling (EPREL) database.`Vehicle_CO2_Class` for the overall CO2 class of a vehicle`Vehicle_CO2_Class_Discharged_Battery` for the CO2 class of a vehicle with a discharged battery
|

| Recommended properties | |
|---|---|
`certificationIdentification` |
The code of the certification. For example, for the EPREL certificate with the link
|
`certificationRating` |
The value of the certification. This property is ignored for certifications that
have the `ratingValue` `bestRating` `worstRating`
The Here's an example of the hasCertification": { "@type": "Certification", "issuedBy": { "@type": "Organization", "name": "European_Commission" } "name": "EPREL", "url": "https://eprel.ec.europa.eu/screen/product/ovens/53553", "certificationIdentification": "53553", "certificationRating": { "@type": "Rating", "ratingValue": "A+", "bestRating": "A++", "worstRating": "D" } } Here's an example of the "hasCertification": { "@type": "Certification", "issuedBy": { "@type": "Organization", "name": "ADEME" } "name": "Vehicle_CO2_Class", "certificationRating": { "@type": "Rating", "ratingValue": "E", "bestRating": "A", "worstRating": "G" } } |

### Shipping

`OfferShippingDetails`


`OfferShippingDetails`

enables people to see shipping costs and
estimated delivery timeframes based on their location and your company's shipping policies.
To make your products eligible for the shipping details enhancement, add the following
`OfferShippingDetails`

properties to your product pages in addition to
`Product`

structured data.

Sometimes merchants might have multiple options for users to select when shipping a product to
a destination (for example, Express Overnight, Rushed 2-day, and Standard). You can indicate
each of these by using multiple `shippingDetails`

properties, each with different
combinations of the `shippingRate`

and `deliveryTime`

properties.

While `OfferShippingDetails`

isn't required, the following properties are required if you want your shipping details to be eligible for the shipping details enhancement.

The full definition of `OfferShippingDetails`

is available at
[schema.org/OfferShippingDetails](https://schema.org/OfferShippingDetails).

| Required properties | |
|---|---|
`deliveryTime` |
The total delay between the receipt of the order and the goods reaching the final
customer. The following properties can be nested in the `handlingTime` `transitTime`
Don't provide more than one |
`shippingDestination` |
Indicates shipping destinations. Specify the
|
`shippingRate` |
Information about the cost of shipping to the specified destination.
At least one of You can only specify one
|
`shippingRate.currency` |
The currency of the shipping cost, in 3-letter
|
`shippingRate.value` or `shippingRate.maxValue` |
The cost of shipping to the To specify free shipping, set the value to |

`DefinedRegion`


`DefinedRegion`

is used to create custom areas so that accurate shipping costs
and transit times can be set across multiple shipping services. This is currently only
supported for a restricted set of countries, as documented in
[Set up regions](https://support.google.com/merchants/answer/7410946)
in Google Merchant Center Help.

| Required properties | |
|---|---|
`addressCountry` |
The two-letter country code, in |

| Recommended properties | |
|---|---|
Choose either `addressRegion` or `postalCode` |
Identifies the region for the customer delivery area. If omitted,
the whole country is the defined region. Multiple regions can be listed,
but you cannot mix different ways of specifying the regions in one
|
`addressRegion` |
If you include this property, the region must be a 2- or 3-digit ISO 3166-2 subdivision code, without country prefix. Currently, Google Search only supports the US, Australia, and Japan. Examples: "NY" (for US, state of New York), "NSW" (for Australia, state of New South Wales), or "03" (for Japan, Iwate prefecture). Do not provide both a region and postal code information. |
`postalCode` |
The postal code. For example, 94043. Currently postal codes are supported for Australia, Canada, and the US. |

`ShippingDeliveryTime`



is used to share the total delay between the receipt of an order and the goods reaching
the final customer.
[ShippingDeliveryTime](https://schema.org/ShippingDeliveryTime)

| Recommended properties | |
|---|---|
`handlingTime` |
The typical delay between the receipt of the order and the goods leaving the warehouse. |
`transitTime` |
The typical delay between when the order has been sent for delivery and when the goods reach the final customer. |

`QuantitativeValue`

(for shipping times)

`QuantitativeValue`

is used here to represent shipping times. A minimum and
maximum number of days must be specified. (`QuantitativeValue`

is also used
for unity pricing, with different validation rules for properties.)

| Required properties | |
|---|---|
`maxValue` |
The maximum number of days. The value must be a non-negative, whole number. |
`minValue` |
The minimum number of days. The value must be a non-negative, whole number. |
`unitCode` |
The units of the minimum/maximum values. The value must be |

### Returns

`MerchantReturnPolicy`


Use the following properties to make your merchant listing eligible to show return policy information, including return fees and the window of time to return a product.

| Required properties | |
|---|---|
`applicableCountry` |
The country code that the return policy applies to, using the two-letter
|
`returnPolicyCategory` |
The type of return policy. Use one of the following values: `https://schema.org/MerchantReturnFiniteReturnWindow` : There's a set number of days to return a product.`https://schema.org/MerchantReturnNotPermitted` : Returns aren't permitted.`https://schema.org/MerchantReturnUnlimitedWindow` : There's an unlimited amount of time to return a product.
If you use |

| Recommended properties | |
|---|---|
`merchantReturnDays` |
The number of days from the delivery date that a product can be returned. This
property is required if you set the `MerchantReturnFiniteReturnWindow` . |
`returnFees` |
The type of return fees. Use one of the following supported values: `https://schema.org/FreeReturn` : There's no charge to the consumer to return the product. If used, don't include theproperty.`returnShippingFeesAmount` `https://schema.org/ReturnFeesCustomerResponsibility` : The consumer needs to handle and pay for the return shipping themselves. If used, don't include theproperty.`returnShippingFeesAmount` `https://schema.org/ReturnShippingFees` : There's a shipping fee charged by the merchant to the consumer to return the product. Specify the (non-zero) shipping fee using theproperty.`returnShippingFeesAmount`
|
`returnMethod` |
The type of return method offered. This is only recommended if you set the
`https://schema.org/ReturnAtKiosk` : The item can be returned at a kiosk.`https://schema.org/ReturnByMail` : The item can be returned by mail.`https://schema.org/ReturnInStore` : The item can be returned in a store.
|
`returnShippingFeesAmount` |
The cost of shipping for returning a product. This property is only required if there's a
non-zero shipping fee to be paid by the consumer to the merchant to return a product, in which case `https://schema.org/ReturnShippingFees` .
If the return is free,
`returnFees` |

## Alternative approaches to configuring shipping and return settings with Google

Retailer shipping and return policies can get complicated and may change frequently. If you're having
trouble indicating and keeping your shipping and return details up-to-date with markup
and have a Google Merchant Center account, consider configuring your
[shipping settings](https://support.google.com/merchants/answer/6069284)
and
[return policies](https://support.google.com/merchants/answer/10220642)
in Google Merchant Center Help. You can alternatively configure account-level
[shipping and return policies in Search Console](https://support.google.com/webmasters/answer/14907594),
which get automatically added to Merchant Center.

### Combining multiple shipping and return configurations

If you define shipping or return policies in multiple places, Google uses the following order of precedence (from strongest to weakest):

- Product-level
[feeds submitted in Merchant Center](https://support.google.com/merchants/answer/188477) [Settings in the Content API for Shopping](/shopping-content/guides/free-listings-return-settings)- Settings in Merchant Center or Search Console
- Product-level merchant listing markup
[Organization-level markup](/search/docs/appearance/structured-data/organization)

## Monitor rich results with Search Console

Search Console is a tool that helps you monitor how your pages perform in Google Search. You don't have to sign up for Search Console to be included in Google Search results, but it can help you understand and improve how Google sees your site. We recommend checking Search Console in the following cases:

[After deploying structured data for the first time](#after-deploying)[After releasing new templates or updating your code](#after-releasing)[Analyzing traffic periodically](#analyzing-periodically)

### After deploying structured data for the first time

After Google has indexed your pages, look for issues using the relevant
[Rich result status report](https://support.google.com/webmasters/answer/7552505).
Ideally, there will be an increase of valid items, and no increase in invalid items. If you find issues
in your structured data:

[Fix the invalid items](#troubleshooting).[Inspect a live URL](https://support.google.com/webmasters/answer/9012289#test_live_page)to check if the issue persists.[Request validation](https://support.google.com/webmasters/answer/13300208)using the status report.

### After releasing new templates or updating your code

When you make significant changes to your website, monitor for increases in structured data invalid items.- If you see an
**increase in invalid items**, perhaps you rolled out a new template that doesn't work, or your site interacts with the existing template in a new and bad way. - If you see a
**decrease in valid items**(not matched by an increase in invalid items), perhaps you are no longer embedding structured data in your pages. Use the[URL Inspection tool](https://support.google.com/webmasters/answer/9012289)to learn what is causing the issue.

### Analyzing traffic periodically

Analyze your Google Search traffic using the[Performance Report](https://support.google.com/webmasters/answer/7576553). The data will show you how often your page appears as a rich result in Search, how often users click on it and what is the average position you appear on search results. You can also automatically pull these results with the

[Search Console API](/webmaster-tools/search-console-api-original/v3/how-tos/search_analytics).

There are two Search Console reports related to `Product`

structured data:

: For pages where shoppers can buy products.[Merchant listings report](https://search.google.com/search-console/r/merchant-listings): For other product related pages such as product reviews and aggregator sites.[Product snippets report](https://search.google.com/search-console/r/product)

Both reports provide warnings and errors related to `Product`

structured data, but
are separate due to the different requirements for the associated experiences. For example, the
[Merchant listings report](https://search.google.com/search-console/r/merchant-listings)
includes checks for product snippets that include `Offer`

structured data, so the
[Product snippets](https://search.google.com/search-console/r/product)
report only needs to be consulted for non-merchant listing pages.

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results.
For a list of common reasons why Google may not show your content in a rich result, see the
[General Structured Data Guidelines](/search/docs/appearance/structured-data/sd-policies). - You might have an error in your structured data. Check the
[list of structured data errors](https://support.google.com/webmasters/answer/13300873)and the[Unparsable structured data report](https://support.google.com/webmasters/answer/9166415). - If you received a structured data manual action against your page, the structured data on
the page will be ignored (although the page can still appear in Google Search results). To fix
[structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the[Manual Actions report](https://support.google.com/webmasters/answer/9044175). - Review the
[guidelines](#guidelines)again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues. [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208).- Allow time for re-crawling and re-indexing. Remember that it may take several days after
publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the
[Google Search crawling and indexing FAQ](/search/help/crawling-index-faq). - Post a question in the
[Google Search Central forum](https://support.google.com/webmasters/community).
