---
title: "Order"
source_url: https://schema.org/Order
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Order

# Order

A Schema.org Type

- Canonical URL: https://schema.org/Order
- Equivalent Class: unece:Order
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Order)

An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[acceptedOffer](/acceptedOffer)

[Offer](/Offer)```
```[billingAddress](/billingAddress)

[PostalAddress](/PostalAddress)```
```[broker](/broker)

[Organization](/Organization)or[Person](/Person)[bookingAgent](/bookingAgent).```
```[confirmationNumber](/confirmationNumber)

[Text](/Text)```
```[customer](/customer)

[Organization](/Organization)or[Person](/Person)```
```[discount](/discount)

[Number](/Number)or[Text](/Text)```
```[discountCode](/discountCode)

[Text](/Text)```
```[discountCurrency](/discountCurrency)

[Text](/Text)Use standard formats:

[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR".```
```[isGift](/isGift)

[Boolean](/Boolean)```
```[orderDate](/orderDate)

[Date](/Date)or[DateTime](/DateTime)```
```[orderDelivery](/orderDelivery)

[ParcelDelivery](/ParcelDelivery)```
```[orderNumber](/orderNumber)

[Text](/Text)```
```[orderStatus](/orderStatus)

[OrderStatus](/OrderStatus)```
```[orderedItem](/orderedItem)

[OrderItem](/OrderItem)or[Product](/Product)or[Service](/Service)```
```[partOfInvoice](/partOfInvoice)

[Invoice](/Invoice)```
```[paymentDueDate](/paymentDueDate)

[Date](/Date)or[DateTime](/DateTime)[paymentDue](/paymentDue).```
```[paymentMethod](/paymentMethod)

[PaymentMethod](/PaymentMethod)or[Text](/Text)```
```[paymentMethodId](/paymentMethodId)

[Text](/Text)```
```[paymentUrl](/paymentUrl)

[URL](/URL)```
```[seller](/seller)

[Organization](/Organization)or[Person](/Person)[merchant](/merchant),[vendor](/vendor).[Thing](/Thing)

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

[Order](/Order)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[ParcelDelivery](/ParcelDelivery)[referencesOrder](/referencesOrder)

[Invoice](/Invoice)### Examples

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

[Example 2](#eg-0376)

Copied

Example notes or example HTML without markup.

An example of an order for multiple items, shipped separately. ACME Supplies Customer: Jane Doe Order: Item abc123: 1 Widget: delivered 2015-03-10 Item def456: 3 Widget accessories: shipped 2015-03-12

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Order"> <div itemprop="seller" itemscope itemtype="https://schema.org/Organization"> <b itemprop="name">ACME Supplies</b> </div> <div itemprop="customer" itemscope itemtype="https://schema.org/Person"> <b itemprop="name">Jane Doe</b> </div> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/OrderItem"> Item number: <span itemprop="orderItemNumber">abc123</span> <span itemprop="orderQuantity">1</span> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/Product"> <span itemprop="name">Widget</span> </div> <link itemprop="orderItemStatus" href="https://schema.org/OrderDelivered" />Delivered <div itemprop="orderDelivery" itemscope itemtype="https://schema.org/ParcelDelivery"> <time itemprop="expectedArrivalFrom">2015-03-10</time> </div> </div> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/OrderItem"> Item number: <span itemprop="orderItemNumber">def456</span> <span itemprop="orderQuantity">4</span> <div itemprop="orderedItem" itemscope itemtype="https://schema.org/Product"> <span itemprop="name">Widget accessories</span> </div> <link itemprop="orderItemStatus" href="https://schema.org/OrderInTransit" />Shipped <div itemprop="orderDelivery" itemscope itemtype="https://schema.org/ParcelDelivery"> <time itemprop="expectedArrivalFrom">2015-03-15</time> <time itemprop="expectedArrivalUntil">2015-03-18</time> </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Order"> <div property="seller" typeof="Organization"> <b property="name">ACME Supplies</b> </div> <div property="customer" typeof="Person"> <b property="name">Jane Doe</b> </div> <div property="orderedItem" typeof="OrderItem"> Item number: <span property="orderItemNumber">abc123</span> <span property="orderQuantity">1</span> <div property="orderedItem" typeof="Product"> <span property="name">Widget</span> </div> <link property="orderItemStatus" href="https://schema.org/OrderDelivered" />Delivered <div property="orderDelivery" typeof="ParcelDelivery"> <time property="expectedArrivalFrom">2015-03-10</time> </div> </div> <div property="orderedItem" typeof="OrderItem"> Item number: <span property="orderItemNumber">def456</span> <span property="orderQuantity">4</span> <div property="orderedItem" typeof="Product"> <span property="name">Widget accessories</span> </div> <link property="orderItemStatus" href="https://schema.org/OrderInTransit" />Shipped <div property="orderDelivery" typeof="ParcelDelivery"> <time property="expectedArrivalFrom">2015-03-15</time> <time property="expectedArrivalUntil">2015-03-18</time> </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Order", "seller": { "@type": "Organization", "name": "ACME Supplies" }, "customer": { "@type": "Person", "name": "Jane Doe" }, "orderedItem": [ { "@type": "OrderItem", "orderItemNumber": "abc123", "orderQuantity": 1, "orderedItem": { "@type": "Product", "name": "Widget" }, "orderItemStatus": "https://schema.org/OrderDelivered", "orderDelivery": { "@type": "ParcelDelivery", "expectedArrivalFrom": "2015-03-10" } }, { "@type": "OrderItem", "orderItemNumber": "def456", "orderQuantity": 3, "orderedItem": { "@type": "Product", "name": "Widget accessories" }, "orderItemStatus": "https://schema.org/OrderInTransit", "orderDelivery": { "@type": "ParcelDelivery", "expectedArrivalFrom": "2015-03-15", "expectedArrivalUntil": "2015-03-18" } } ] } </script>

Structured representation of the JSON-LD example.
