---
title: "PriceSpecification"
source_url: https://schema.org/PriceSpecification
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2015-01-30
---

# PriceSpecification

# PriceSpecification

A Schema.org Type

- Canonical URL: https://schema.org/PriceSpecification
- Equivalent Class: fibo-fnd-pas-pas:Price
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+PriceSpecification)

A structured value representing a price or price range. Typically, only the subclasses of this type are used for markup. It is recommended to use

[MonetaryAmount](/MonetaryAmount)to describe independent amounts of money such as a salary, credit card limits, etc.| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[eligibleQuantity](/eligibleQuantity)

[QuantitativeValue](/QuantitativeValue)```
```[eligibleTransactionVolume](/eligibleTransactionVolume)

[PriceSpecification](/PriceSpecification)```
```[maxPrice](/maxPrice)

[Number](/Number)```
```[membershipPointsEarned](/membershipPointsEarned)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)```
```[minPrice](/minPrice)

[Number](/Number)```
```[price](/price)

[Number](/Number)or[Text](/Text)Usage guidelines:

- Use the
[priceCurrency](/priceCurrency)property (with standard formats:[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR") instead of including[ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign)such as '$' in the value. - Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
- Note that both
[RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute)and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting. - Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.

```
```[priceCurrency](/priceCurrency)

[Text](/Text)[PriceSpecification](/PriceSpecification)and its subtypes.Use standard formats:

[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR".```
```[validForMemberTier](/validForMemberTier)

[MemberProgramTier](/MemberProgramTier)```
```[validFrom](/validFrom)

[Date](/Date)or[DateTime](/DateTime)```
```[validThrough](/validThrough)

[Date](/Date)or[DateTime](/DateTime)```
```[valueAddedTaxIncluded](/valueAddedTaxIncluded)

[Boolean](/Boolean)[Thing](/Thing)

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

[PriceSpecification](/PriceSpecification)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[EmployeeRole](/EmployeeRole)or[JobPosting](/JobPosting)[eligibleTransactionVolume](/eligibleTransactionVolume)

[Demand](/Demand)or[Offer](/Offer)or[PriceSpecification](/PriceSpecification)[healthPlanCopay](/healthPlanCopay)

[HealthPlanCostSharingSpecification](/HealthPlanCostSharingSpecification)[minimumPaymentDue](/minimumPaymentDue)

[Invoice](/Invoice)[netWorth](/netWorth)

[Person](/Person)[priceComponent](/priceComponent)

[CompoundPriceSpecification](/CompoundPriceSpecification)[UnitPriceSpecification](/UnitPriceSpecification)nodes that apply in parallel for the[CompoundPriceSpecification](/CompoundPriceSpecification)node.[priceSpecification](/priceSpecification)

[Demand](/Demand)or[DonateAction](/DonateAction)or[Offer](/Offer)or[TradeAction](/TradeAction)[totalPaymentDue](/totalPaymentDue)

[Invoice](/Invoice)[totalPrice](/totalPrice)

[Reservation](/Reservation)or[Ticket](/Ticket)Usage guidelines:

- Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
- Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

#### More specific Types

-
[CompoundPriceSpecification](/CompoundPriceSpecification) -
[DeliveryChargeSpecification](/DeliveryChargeSpecification) -
[PaymentChargeSpecification](/PaymentChargeSpecification) -
[UnitPriceSpecification](/UnitPriceSpecification)

### Examples

[Example 1](#eg-0374)

Copied

Example notes or example HTML without markup.

An example of a credit card bill (invoice). ACME Bank Bill for: January 2015 Visa invoice link: http://www.acmebank.com/invoice.pdf Customer: Jane Doe account ID: xxxx-xxxx-xxxx-1234 payment due: 2015-01-30 minimum payment: $15.00 total due: $200.00 billing period: 2014-12-21 to 2015-01-20 payment due

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Invoice"> <h1 itemprop="description">January 2015 Visa</h1> <a itemprop="url" href="http://acmebank.com/invoice.pdf">Invoice PDF</a> <div itemprop="broker" itemscope itemtype="https://schema.org/BankOrCreditUnion"> <b itemprop="name">ACME Bank</b> </div> <span itemprop="accountId">xxxx-xxxx-xxxx-1234</span> <div itemprop="customer" itemscope itemtype="https://schema.org/Person"> <b itemprop="name">Jane Doe</b> </div> <time itemprop="paymentDueDate">2015-01-30</time> <div itemprop="minimumPaymentDue" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="price">15.00</span> <span itemprop="priceCurrency">USD</span> </div> <div itemprop="totalPaymentDue" itemscope itemtype="https://schema.org/PriceSpecification"> <span itemprop="price">200.00</span> <span itemprop="priceCurrency">USD</span> </div> <meta itemprop="billingPeriod" content="P30D" />starts:2014-12-21 30 days <link itemprop="paymentStatus" href="https://schema.org/PaymentDue" /> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Invoice"> <h1 property="description">January 2015 Visa</h1> <a property="url" href="http://acmebank.com/invoice.pdf">Invoice PDF</a> <div property="broker" typeof="BankOrCreditUnion"> <b property="name">ACME Bank</b> </div> <span property="accountId">xxxx-xxxx-xxxx-1234</span> <div property="customer" typeof="Person"> <b property="name">Jane Doe</b> </div> <time property="paymentDueDate">2015-01-30T12:00:00</time> <div property="minimumPaymentDue" typeof="PriceSpecification"> <span property="price">15.00</span> <span property="priceCurrency">USD</span> </div> <div property="totalPaymentDue" typeof="PriceSpecification"> <span property="price">200.00</span> <span property="priceCurrency">USD</span> </div> <meta property="billingPeriod" content="P30D" />starts:2014-12-21 30 days <link property="paymentStatus" href="https://schema.org/PaymentDue" /> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Invoice", "description": "January 2015 Visa bill.", "url": "http://acmebank.com/invoice.pdf", "broker": { "@type": "BankOrCreditUnion", "name": "ACME Bank" }, "accountId": "xxxx-xxxx-xxxx-1234", "customer": { "@type": "Person", "name": "Jane Doe" }, "paymentDueDate": "2015-01-30T12:00:00", "minimumPaymentDue": { "@type": "PriceSpecification", "price": 15.00, "priceCurrency": "USD" }, "totalPaymentDue": { "@type": "PriceSpecification", "price": 200.00, "priceCurrency": "USD" }, "billingPeriod": "P30D", "paymentStatus": "https://schema.org/PaymentDue" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0375)

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

[Example 3](#eg-0397)

Copied

Example notes or example HTML without markup.

Joes' Pizza 123 Main Street Cambridge, MA 02142 delivers within 5 km of its store with a minimum order of $20.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/FoodEstablishment"> <span itemprop="name">Joe's Pizza</span> <div itemprop="location" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">123 Main Street</span> <span itemprop="addressLocality">Cambridge</span> <span itemprop="addressRegion">MA</span> <span itemprop="postalCode">02142</span> </div> delivers within 5 km of its store <div itemprop="makesOffer" itemscope itemtype="https://schema.org/Offer"> <div itemprop="eligibleRegion" itemscope itemtype="https://schema.org/GeoCircle"> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <meta itemprop="streetAddress" content="123 Main Street" /> <meta itemprop="addressLocality" content="Cambridge" /> <meta itemprop="addressRegion" content="MA" /> <meta itemprop="postalCode" content="02142" /> </div> <meta itemprop="geoRadius" content="5000" /> </div> with a minimum order of $20. <div itemprop="priceSpecification" itemscope itemtype="https://schema.org/DeliveryChargeSpecification"> <meta itemprop="appliesToDeliveryMethod" link="http://purl.org/goodrelations/v1#DeliveryModeOwnFleet"> <div itemprop="eligibleTransactionVolume" itemscope itemtype="https://schema.org/PriceSpecification"> <meta itemprop="price" content="20.00" /> <meta itemprop="priceCurrency" content="USD" /> </div> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="FoodEstablishment"> <span property="name">Joe's Pizza</span> <div property="location" typeof="PostalAddress"> <span property="streetAddress">123 Main Street</span> <span property="addressLocality">Cambridge</span> <span property="addressRegion">MA</span> <span property="postalCode">02142</span> </div> delivers within 5 km of its store with a minimum order of $20. <div property="makesOffer" typeof="Offer"> <div property="priceSpecification" typeof="DeliveryChargeSpecification"> <meta property="appliesToDeliveryMethod" link="http://purl.org/goodrelations/v1#DeliveryModeOwnFleet"> <div property="eligibleTransactionVolume" typeof="PriceSpecification"> <meta property="price" content="20.00" /> <meta property="priceCurrency" content="USD" /> </div> <div property="eligibleRegion" typeof="GeoCircle"> <div property="address" typeof="PostalAddress"> <meta property="streetAddress" content="123 Main Street" /> <meta property="addressLocality" content="Cambridge" /> <meta property="addressRegion" content="MA" /> <meta property="postalCode" content="02142" /> </div> <meta property="geoRadius" content="5000" /> </div> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "FoodEstablishment", "name": "Joe's Pizza", "location": { "@type": "PostalAddress", "@id": "http://example.com/address", "streetAddress": "123 Main Street", "addressLocality": "Cambridge", "addressRegion": "MA", "postalCode": "02142" }, "makesOffer": { "@type": "Offer", "priceSpecification": { "@type": "DeliveryChargeSpecification", "appliesToDeliveryMethod": "http://purl.org/goodrelations/v1#DeliveryModeOwnFleet", "eligibleTransactionVolume": { "@type": "PriceSpecification", "price": "20.00", "priceCurrency": "USD" }, "eligibleRegion": { "@type": "GeoCircle", "address": { "@id": "http://www.example.com/address" }, "geoRadius": "5000" } } } } </script>

Structured representation of the JSON-LD example.
