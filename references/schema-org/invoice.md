---
title: "Invoice"
source_url: https://schema.org/Invoice
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2015-01-30
---

# Invoice

# Invoice

A Schema.org Type

- Canonical URL: https://schema.org/Invoice
- Equivalent Class: unece:Invoice
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Invoice)

A statement of the money due for goods or services; a bill.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[accountId](/accountId)

[Text](/Text)```
```[billingPeriod](/billingPeriod)

[Duration](/Duration)```
```[broker](/broker)

[Organization](/Organization)or[Person](/Person)[bookingAgent](/bookingAgent).```
```[category](/category)

[CategoryCode](/CategoryCode)or[PhysicalActivityCategory](/PhysicalActivityCategory)or[Text](/Text)or[Thing](/Thing)or[URL](/URL)```
```[confirmationNumber](/confirmationNumber)

[Text](/Text)```
```[customer](/customer)

[Organization](/Organization)or[Person](/Person)```
```[minimumPaymentDue](/minimumPaymentDue)

[MonetaryAmount](/MonetaryAmount)or[PriceSpecification](/PriceSpecification)```
```[paymentDueDate](/paymentDueDate)

[Date](/Date)or[DateTime](/DateTime)[paymentDue](/paymentDue).```
```[paymentMethod](/paymentMethod)

[PaymentMethod](/PaymentMethod)or[Text](/Text)```
```[paymentMethodId](/paymentMethodId)

[Text](/Text)```
```[paymentStatus](/paymentStatus)

[PaymentStatusType](/PaymentStatusType)or[Text](/Text)```
```[provider](/provider)

[Organization](/Organization)or[Person](/Person)[carrier](/carrier).```
```[referencesOrder](/referencesOrder)

[Order](/Order)```
```[scheduledPaymentDate](/scheduledPaymentDate)

[Date](/Date)```
```[totalPaymentDue](/totalPaymentDue)

[MonetaryAmount](/MonetaryAmount)or[PriceSpecification](/PriceSpecification)[Thing](/Thing)

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

[Invoice](/Invoice)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Order](/Order)### Examples

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
