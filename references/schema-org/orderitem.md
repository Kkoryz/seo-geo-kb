---
title: "OrderItem"
source_url: https://schema.org/OrderItem
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# OrderItem

# OrderItem

A Schema.org Type

- Canonical URL: https://schema.org/OrderItem
- Equivalent Class: unece:LineTradeAgreement
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+OrderItem)

An order item is a line of an order. It includes the quantity and shipping details of a bought offer.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[orderDelivery](/orderDelivery)

[ParcelDelivery](/ParcelDelivery)```
```[orderItemNumber](/orderItemNumber)

[Text](/Text)```
```[orderItemStatus](/orderItemStatus)

[OrderStatus](/OrderStatus)```
```[orderQuantity](/orderQuantity)

[Number](/Number)or[QuantitativeValue](/QuantitativeValue)```
```[orderedItem](/orderedItem)

[OrderItem](/OrderItem)or[Product](/Product)or[Service](/Service)[Thing](/Thing)

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

[OrderItem](/OrderItem)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Order](/Order)or[OrderItem](/OrderItem)### Examples

[Example 1](#eg-0376)

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
