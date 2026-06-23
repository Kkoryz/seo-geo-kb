---
title: "Product"
source_url: https://schema.org/Product
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# Product

# Product

A Schema.org Type

- Canonical URL: https://schema.org/Product
-
Equivalent Class: unece:TradeProduct

Equivalent Class: fibo-fnd-pas-pas:Product [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+Product)

Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[additionalProperty](/additionalProperty)

[PropertyValue](/PropertyValue)Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

```
```[aggregateRating](/aggregateRating)

[AggregateRating](/AggregateRating)```
```[asin](/asin)

[Text](/Text)or[URL](/URL)[Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details. ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.

```
```[audience](/audience)

[Audience](/Audience)[serviceAudience](/serviceAudience).```
```[award](/award)

[Text](/Text)[awards](/awards).```
```[brand](/brand)

[Brand](/Brand)or[Organization](/Organization)```
```[category](/category)

[CategoryCode](/CategoryCode)or[PhysicalActivityCategory](/PhysicalActivityCategory)or[Text](/Text)or[Thing](/Thing)or[URL](/URL)```
```[color](/color)

[Text](/Text)```
```[colorSwatch](/colorSwatch)

[ImageObject](/ImageObject)or[URL](/URL)[Product](/Product). Should match the textual description specified in the[color](/color)property. This can be a URL or a fully described ImageObject.```
```[countryOfAssembly](/countryOfAssembly)

[Text](/Text)```
```[countryOfLastProcessing](/countryOfLastProcessing)

[Text](/Text)[Product](/Product)) was last processed and tested before importation.```
```[countryOfOrigin](/countryOfOrigin)

[Country](/Country)In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of

[CreativeWork](/CreativeWork)it is difficult to provide fully general guidance, and properties such as[contentLocation](/contentLocation)and[locationCreated](/locationCreated)may be more applicable.In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.

```
```[depth](/depth)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)```
```[displayLocation](/displayLocation)

[Place](/Place)```
```[funding](/funding)

[Grant](/Grant)[Grant](/Grant)that directly or indirectly provide funding or sponsorship for this item. See also[ownershipFundingInfo](/ownershipFundingInfo).Inverse property:

[fundedItem](/fundedItem)```
```[gtin](/gtin)

[Text](/Text)or[URL](/URL)[GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.A correct

[gtin](/gtin)value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a[valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator)and meet the other rules for valid GTINs. See also[GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)and[Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number)for more details. Left-padding of the gtin values is not required or encouraged. The[gtin](/gtin)property generalizes the earlier[gtin8](/gtin8),[gtin12](/gtin12),[gtin13](/gtin13), and[gtin14](/gtin14)properties.The GS1

[digital link specifications](https://www.gs1.org/standards/Digital-Link/)expresses GTINs as URLs (URIs, IRIs, etc.). Digital Links should be populated into the[hasGS1DigitalLink](/hasGS1DigitalLink)attribute.Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.

```
```[gtin12](/gtin12)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin13](/gtin13)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin14](/gtin14)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[gtin8](/gtin8)

[Text](/Text)[GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)for more details.```
```[hasAdultConsideration](/hasAdultConsideration)

[AdultOrientedEnumeration](/AdultOrientedEnumeration)```
```[hasCertification](/hasCertification)

[Certification](/Certification)```
```[hasEnergyConsumptionDetails](/hasEnergyConsumptionDetails)

[EnergyConsumptionDetails](/EnergyConsumptionDetails)```
```[hasGS1DigitalLink](/hasGS1DigitalLink)

[URL](/URL)[GS1 digital link](https://www.gs1.org/standards/gs1-digital-link)associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a[Product](/Product)or an[Organization](/Organization), and for the correct granularity. In particular, for products:- A Digital Link that contains a serial number (AI
`21`

) should only be present on instances of[IndividualProduct](/IndividualProduct) - A Digital Link that contains a lot number (AI
`10`

) should be annotated as[SomeProducts](/SomeProducts)if only products from that lot are sold, or[IndividualProduct](/IndividualProduct)if there is only a specific product. - A Digital Link that contains a global model number (AI
`8013`

) should be attached to a[Product](/Product)or a[ProductModel](/ProductModel).

```
```[hasMeasurement](/hasMeasurement)

[QuantitativeValue](/QuantitativeValue)```
```[hasMerchantReturnPolicy](/hasMerchantReturnPolicy)

[MerchantReturnPolicy](/MerchantReturnPolicy)[hasProductReturnPolicy](/hasProductReturnPolicy).```
```[height](/height)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)```
```[inProductGroupWithID](/inProductGroupWithID)

[Text](/Text)[productGroupID](/productGroupID)for a[ProductGroup](/ProductGroup)that this product[isVariantOf](/isVariantOf).```
```[isAccessoryOrSparePartFor](/isAccessoryOrSparePartFor)

[Product](/Product)```
```[isConsumableFor](/isConsumableFor)

[Product](/Product)```
```[isFamilyFriendly](/isFamilyFriendly)

[Boolean](/Boolean)```
```[isRelatedTo](/isRelatedTo)

[Product](/Product)or[Service](/Service)```
```[isSimilarTo](/isSimilarTo)

[Product](/Product)or[Service](/Service)```
```[isVariantOf](/isVariantOf)

[ProductGroup](/ProductGroup)or[ProductModel](/ProductModel)[ProductModel](/ProductModel), this is a pointer (from a ProductModel) to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive. In the case of a[ProductGroup](/ProductGroup), the group description also serves as a template, representing a set of Products that vary on explicitly defined, specific dimensions only (so it defines both a set of variants, as well as which values distinguish amongst those variants). When used with[ProductGroup](/ProductGroup), this property can apply to any[Product](/Product)included in the group.Inverse property:

[hasVariant](/hasVariant)```
```[itemCondition](/itemCondition)

[OfferItemCondition](/OfferItemCondition)```
```[keywords](/keywords)

[DefinedTerm](/DefinedTerm)or[Text](/Text)or[URL](/URL)```
```[logo](/logo)

[ImageObject](/ImageObject)or[URL](/URL)```
```[manufacturer](/manufacturer)

[Organization](/Organization)```
```[material](/material)

[Product](/Product)or[Text](/Text)or[URL](/URL)```
```[mobileUrl](/mobileUrl)

[Text](/Text)[mobileUrl](/mobileUrl)property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.To discourage over-use, and reflecting intial usecases, the property is expected only on

[Product](/Product)and[Offer](/Offer), rather than[Thing](/Thing). The general trend in web technology is towards[responsive design](https://en.wikipedia.org/wiki/Responsive_web_design)in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established[url](/url)property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all[url](/url)markup to use[mobileUrl](/mobileUrl)for more mobile-oriented pages. The property is intended for the case when items (primarily[Product](/Product)and[Offer](/Offer)) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.```
```[model](/model)

[ProductModel](/ProductModel)or[Text](/Text)```
```[mpn](/mpn)

[Text](/Text)```
```[negativeNotes](/negativeNotes)

[ItemList](/ItemList)or[ListItem](/ListItem)or[Text](/Text)or[WebContent](/WebContent)[positiveNotes](/positiveNotes)). For symmetryIn the case of a

[Review](/Review), the property describes the[itemReviewed](/itemReviewed)from the perspective of the review; in the case of a[Product](/Product), the product itself is being described. Since product descriptions tend to emphasise positive claims, it may be relatively unusual to find[negativeNotes](/negativeNotes)used in this way. Nevertheless for the sake of symmetry,[negativeNotes](/negativeNotes)can be used on[Product](/Product).The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list).

```
```[nsn](/nsn)

[Text](/Text)[NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number)(nsn) of a[Product](/Product).```
```[offers](/offers)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction)to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a[Demand](/Demand). While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.Inverse property:

[itemOffered](/itemOffered)```
```[pattern](/pattern)

[DefinedTerm](/DefinedTerm)or[Text](/Text)```
```[positiveNotes](/positiveNotes)

[ItemList](/ItemList)or[ListItem](/ListItem)or[Text](/Text)or[WebContent](/WebContent)[negativeNotes](/negativeNotes)) pro/con lists for reviews.In the case of a

[Review](/Review), the property describes the[itemReviewed](/itemReviewed)from the perspective of the review; in the case of a[Product](/Product), the product itself is being described.The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).

```
```[productID](/productID)

[Text](/Text)`meta itemprop="productID" content="isbn:123-456-789"`

.
```
```[productionDate](/productionDate)

[Date](/Date)```
```[purchaseDate](/purchaseDate)

[Date](/Date)```
```[releaseDate](/releaseDate)

[Date](/Date)```
```[review](/review)

[Review](/Review)[reviews](/reviews).```
```[size](/size)

[DefinedTerm](/DefinedTerm)or[QuantitativeValue](/QuantitativeValue)or[SizeSpecification](/SizeSpecification)or[Text](/Text)[SizeSpecification](/SizeSpecification); in other cases, the[width](/width),[height](/height),[depth](/depth)and[weight](/weight)properties may be more applicable.```
```[sku](/sku)

[Text](/Text)```
```[slogan](/slogan)

[Text](/Text)```
```[weight](/weight)

[Mass](/Mass)or[QuantitativeValue](/QuantitativeValue)```
```[width](/width)

[Distance](/Distance)or[QuantitativeValue](/QuantitativeValue)[Thing](/Thing)

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

[Product](/Product)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[Grant](/Grant)[Grant](/Grant). See also[ownershipFundingInfo](/ownershipFundingInfo).[hasVariant](/hasVariant)

[ProductGroup](/ProductGroup)[Product](/Product)that is a member of this[ProductGroup](/ProductGroup)(or[ProductModel](/ProductModel)).[incentivizedItem](/incentivizedItem)

[FinancialIncentive](/FinancialIncentive)DefinedTermSets are used for product and service categories such as the United Nations Standard Products and Services Code:

```
{
"@type": "DefinedTerm",
"inDefinedTermSet": "https://www.unspsc.org/",
"termCode": "261315XX",
"name": "Photovoltaic module"
}
```


For a specific product or service, use the Product type:```
{
"@type": "Product",
"name": "Kenmore White 17" Microwave",
}
```


For multiple different incentivized items, use multiple [DefinedTerm](/DefinedTerm)or[Product](/Product).[isAccessoryOrSparePartFor](/isAccessoryOrSparePartFor)

[Product](/Product)[isBasedOn](/isBasedOn)

[CreativeWork](/CreativeWork)[isBasedOnUrl](/isBasedOnUrl)

[CreativeWork](/CreativeWork)[isConsumableFor](/isConsumableFor)

[Product](/Product)[isRelatedTo](/isRelatedTo)

[Product](/Product)or[Service](/Service)[isSimilarTo](/isSimilarTo)

[Product](/Product)or[Service](/Service)[itemOffered](/itemOffered)

[Demand](/Demand)or[Offer](/Offer)[businessFunction](/businessFunction), e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.[itemShipped](/itemShipped)

[ParcelDelivery](/ParcelDelivery)[material](/material)

[CreativeWork](/CreativeWork)or[Product](/Product)[orderedItem](/orderedItem)

[Order](/Order)or[OrderItem](/OrderItem)[productSupported](/productSupported)

[ContactPoint](/ContactPoint)[typeOfGood](/typeOfGood)

[OwnershipInfo](/OwnershipInfo)or[TypeAndQuantityNode](/TypeAndQuantityNode)#### More specific Types

-
[DietarySupplement](/DietarySupplement) -
[Drug](/Drug) -
[IndividualProduct](/IndividualProduct) -
[ProductCollection](/ProductCollection) -
[ProductGroup](/ProductGroup) -
[ProductModel](/ProductModel) -
[SomeProducts](/SomeProducts) -
[Vehicle](/Vehicle)

### Acknowledgements

GoodRelations Vocabulary Terms

[uses](https://blog.schema.org/2012/11/08/good-relations-and-schema-org/)terminology from the GoodRelations Vocabulary for E-Commerce, created by Martin Hepp. GoodRelations is a data model for sharing e-commerce data on the Web. More information about GoodRelations can be found at

[http://purl.org/goodrelations/](http://purl.org/goodrelations/).

### Examples

[Example 1](#4658)

Copied

Example notes or example HTML without markup.

<div> <h2>Laptop Battery Replacement</h2> <p>A consumable battery for Model X</p> <p>GTIN: 5901234123457</p> <p>Category: Consumable</p> </div> <div> <h2>Virtual Pump Twin</h2> <p>Digital Twin of the physical water pump for simulation</p> <p>DID: did:web:example.com:product:pump-twin-001</p> <p>Category: Digital Twin</p> </div> <div> <h2>CRM Module</h2> <p>Software module for customer relationship management</p> <p>DID: did:web:example.com:product:crm-module-001</p> <p>Category: Software Component</p> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Product"> <h2 itemprop="name">Laptop Battery Replacement</h2> <p itemprop="description">A consumable battery for Model X</p> <span itemprop="gtin">5901234123457</span> <span itemprop="category">Consumable</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Product Type Code</span> <span itemprop="description">UN/CEFACT UNCL 1001 code for Consumable</span> <meta itemprop="propertyID" content="https://service.unece.org/trade/untdid/d19b/tred/tred1001.htm"> <span itemprop="value">711</span> </div> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Product Role</span> <span itemprop="value">Consumable</span> </div> </div> <div itemscope itemtype="https://schema.org/Product"> <h2 itemprop="name">Virtual Pump Twin</h2> <p itemprop="description">Digital Twin of the physical water pump for simulation</p> <div itemprop="identifier" itemscope itemtype="https://schema.org/PropertyValue"> <meta itemprop="propertyID" content="DID"> <span itemprop="value">did:web:example.com:product:pump-twin-001</span> </div> <span itemprop="category">Digital Twin</span> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">Product Role</span> <span itemprop="value">Digital Twin</span> </div> </div> <div itemscope itemtype="https://schema.org/SoftwareApplication"> <h2 itemprop="name">CRM Module</h2> <p itemprop="description">Software module for customer relationship management</p> <div itemprop="identifier" itemscope itemtype="https://schema.org/PropertyValue"> <meta itemprop="propertyID" content="DID"> <span itemprop="value">did:web:example.com:product:crm-module-001</span> </div> <meta itemprop="applicationCategory" content="BusinessApplication"> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Product"> <h2 property="name">Laptop Battery Replacement</h2> <p property="description">A consumable battery for Model X</p> <span property="gtin">5901234123457</span> <span property="category">Consumable</span> <div property="additionalProperty" typeof="PropertyValue"> <span property="name">Product Type Code</span> <span property="description">UN/CEFACT UNCL 1001 code for Consumable</span> <meta property="propertyID" content="https://service.unece.org/trade/untdid/d19b/tred/tred1001.htm"> <span property="value">711</span> </div> <div property="additionalProperty" typeof="PropertyValue"> <span property="name">Product Role</span> <span property="value">Consumable</span> </div> </div> <div vocab="https://schema.org/" typeof="Product"> <h2 property="name">Virtual Pump Twin</h2> <p property="description">Digital Twin of the physical water pump for simulation</p> <div property="identifier" typeof="PropertyValue"> <meta property="propertyID" content="DID"> <span property="value">did:web:example.com:product:pump-twin-001</span> </div> <span property="category">Digital Twin</span> <div property="additionalProperty" typeof="PropertyValue"> <span property="name">Product Role</span> <span property="value">Digital Twin</span> </div> </div> <div vocab="https://schema.org/" typeof="SoftwareApplication"> <h2 property="name">CRM Module</h2> <p property="description">Software module for customer relationship management</p> <div property="identifier" typeof="PropertyValue"> <meta property="propertyID" content="DID"> <span property="value">did:web:example.com:product:crm-module-001</span> </div> <meta property="applicationCategory" content="BusinessApplication"> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": [ "https://schema.org", { "uncefact": "https://service.unece.org/trade/uncefact/" } ], "@graph": [ { "@id": "urn:example:product:battery-x001", "@type": "Product", "name": "Laptop Battery Replacement", "description": "A consumable battery for Model X", "gtin": "5901234123457", "category": "Consumable", "additionalProperty": [ { "@type": "PropertyValue", "name": "Product Type Code", "description": "UN/CEFACT UNCL 1001 code for Consumable", "propertyID": "https://service.unece.org/trade/untdid/d19b/tred/tred1001.htm", "value": "711" }, { "@type": "PropertyValue", "name": "Product Role", "value": "Consumable" } ] }, { "@id": "urn:example:product:pump-twin-001", "@type": "Product", "name": "Virtual Pump Twin", "description": "Digital Twin of the physical water pump for simulation", "identifier": { "@type": "PropertyValue", "propertyID": "DID", "value": "did:web:example.com:product:pump-twin-001" }, "category": "Digital Twin", "additionalProperty": { "@type": "PropertyValue", "name": "Product Role", "value": "Digital Twin" } }, { "@id": "urn:example:product:crm-module-001", "@type": "SoftwareApplication", "name": "CRM Module", "description": "Software module for customer relationship management", "identifier": { "@type": "PropertyValue", "propertyID": "DID", "value": "did:web:example.com:product:crm-module-001" }, "applicationCategory": "BusinessApplication" } ] } </script>

Structured representation of the JSON-LD example.

[Example 2](#4660)

Copied

Example notes or example HTML without markup.

<div> <h1>Circular Smartphone</h1> <p>Product ID (DID): did:web:example.com:product:12345</p> <p><a href="https://id.example.com/01/01234567890128/21/12345">View Digital Product Passport</a></p> <p>UUID: urn:uuid:123e4567-e89b-12d3-a456-426614174000</p> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Product"> <h1 itemprop="name">Circular Smartphone</h1> <!-- Digital Identity (DID) - Decentralized identifier for supply chain traceability --> <p><strong>Product ID (DID):</strong> <span itemprop="identifier" itemscope itemtype="https://schema.org/PropertyValue"> <meta itemprop="propertyID" content="DID"> <span itemprop="value">did:web:example.com:product:12345</span> </span> <em>(Decentralized Web Identifier - enables verifiable product authentication across the supply chain)</em> </p> <!-- Universal Unique Identifier - Standard UUID for universal identification --> <p><strong>UUID:</strong> <span itemprop="identifier" itemscope itemtype="https://schema.org/PropertyValue"> <meta itemprop="propertyID" content="UUID"> <span itemprop="value">urn:uuid:123e4567-e89b-12d3-a456-426614174000</span> </span> <em>(Universal Unique Identifier - ensures global uniqueness for lifecycle tracking)</em> </p> <!-- GS1 Digital Link - Primary access point to Digital Product Passport --> <p><a itemprop="url" href="https://id.example.com/01/01234567890128/21/12345"> <strong>View Digital Product Passport</strong> </a> <em>(GS1 Digital Link - standard for accessing comprehensive product information, materials, repairability data, and environmental impact)</em> </p> <!-- Repairability Index --> <div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating"> <meta itemprop="ratingValue" content="8"> <meta itemprop="bestRating" content="10"> <span itemprop="name">Repairability Index</span> <span itemprop="description">Official repairability score (0-10) measuring ease of repair, spare parts availability, and design durability</span> </div> <!-- Sustainability information as additional properties --> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">sparePartAvailability</span> <span itemprop="value">P5Y</span> </div> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">carbonFootprint</span> <span itemprop="value">45 kg CO2-eq</span> </div> <div itemprop="additionalProperty" itemscope itemtype="https://schema.org/PropertyValue"> <span itemprop="name">recyclableContent</span> <span itemprop="value">92%</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Product"> <h1 property="name">Circular Smartphone</h1> <!-- Digital Identity (DID) - Decentralized identifier for supply chain traceability --> <p><strong>Product ID (DID):</strong> <span property="identifier" typeof="PropertyValue"> <meta property="propertyID" content="DID"> <span property="value">did:web:example.com:product:12345</span> </span> <br/><em>(Decentralized Web Identifier - enables verifiable product authentication across the supply chain)</em> </p> <!-- Universal Unique Identifier - Standard UUID for universal identification --> <p><strong>UUID:</strong> <span property="identifier" typeof="PropertyValue"> <meta property="propertyID" content="UUID"> <span property="value">urn:uuid:123e4567-e89b-12d3-a456-426614174000</span> </span> <br/><em>(Universal Unique Identifier - ensures global uniqueness for lifecycle tracking)</em> </p> <!-- GS1 Digital Link - Primary access point to Digital Product Passport --> <p><a property="url" href="https://id.example.com/01/01234567890128/21/12345"> <strong>View Digital Product Passport</strong> </a> <br/><em>(GS1 Digital Link - standard for accessing comprehensive product information, materials, repairability data, and environmental impact)</em> </p> <!-- Repairability Index --> <div property="aggregateRating" typeof="AggregateRating"> <meta property="ratingValue" content="8"> <meta property="bestRating" content="10"> <span property="name">Repairability Index</span> <span property="description">Official repairability score (0-10) measuring ease of repair, spare parts availability, and design durability</span> </div> <!-- Sustainability information as additional properties --> <div property="additionalProperty" typeof="PropertyValue"> <span property="name">sparePartAvailability</span> <span property="value">P5Y</span> </div> <div property="additionalProperty" typeof="PropertyValue"> <span property="name">carbonFootprint</span> <span property="value">45 kg CO2-eq</span> </div> <div property="additionalProperty" typeof="PropertyValue"> <span property="name">recyclableContent</span> <span property="value">92%</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Product", "name": "Circular Smartphone", "description": "A repairable smartphone designed for circular economy with modular components, supporting product-as-a-service models and extended lifecycle management", "identifier": [ { "@type": "PropertyValue", "propertyID": "DID", "value": "did:web:example.com:product:12345", "description": "Decentralized Web Identifier for verifiable supply chain authentication" }, { "@type": "PropertyValue", "propertyID": "UUID", "value": "urn:uuid:123e4567-e89b-12d3-a456-426614174000", "description": "Universal Unique Identifier for global lifecycle tracking" } ], "url": "https://id.example.com/01/01234567890128/21/12345", "aggregateRating": { "@type": "AggregateRating", "ratingValue": 8, "bestRating": 10, "name": "Repairability Index", "description": "Official repairability score (0-10) measuring ease of repair, spare parts availability, and design durability" }, "award": "Circular Economy Ready", "additionalProperty": [ { "@type": "PropertyValue", "name": "sparePartAvailability", "value": "P5Y", "description": "Spare parts available for 5 years" }, { "@type": "PropertyValue", "name": "carbonFootprint", "value": "45 kg CO2-eq", "description": "Carbon footprint in CO2 equivalent" }, { "@type": "PropertyValue", "name": "recyclableContent", "value": "92%", "description": "Percentage of recyclable content" } ] } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0010)

Copied

Example notes or example HTML without markup.

Kenmore White 17" Microwave <img src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' /> Rated 3.5/5 based on 11 customer reviews $55.00 In stock Product description: 0.7 cubic feet countertop microwave. Has six preset cooking categories and convenience features like Add-A-Minute and Child Lock. Customer reviews: Not a happy camper - by Ellie, April 1, 2011 1/5 stars The lamp burned out and now I have to replace it. Value purchase - by Lucas, March 25, 2011 4/5 stars Great microwave for the price. It is small and fits in my apartment. ...

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Product"> <span itemprop="name">Kenmore White 17" Microwave</span> <img itemprop="image" src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' /> <div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating"> Rated <span itemprop="ratingValue">3.5</span>/5 based on <span itemprop="reviewCount">11</span> customer reviews </div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <!--price is 1000, a number, with locale-specific thousands separator and decimal mark, and the $ character is marked up with the machine-readable code "USD" --> <span itemprop="priceCurrency" content="USD">$</span><span itemprop="price" content="1000.00">1,000.00</span> <link itemprop="availability" href="https://schema.org/InStock" />In stock </div> Product description: <span itemprop="description">0.7 cubic feet countertop microwave. Has six preset cooking categories and convenience features like Add-A-Minute and Child Lock.</span> Customer reviews: <div itemprop="review" itemscope itemtype="https://schema.org/Review"> <span itemprop="name">Not a happy camper</span> - by <span itemprop="author">Ellie</span>, <meta itemprop="datePublished" content="2011-04-01">April 1, 2011 <div itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating"> <meta itemprop="worstRating" content = "1"> <span itemprop="ratingValue">1</span>/ <span itemprop="bestRating">5</span>stars </div> <span itemprop="reviewBody">The lamp burned out and now I have to replace it. </span> </div> <div itemprop="review" itemscope itemtype="https://schema.org/Review"> <span itemprop="name">Value purchase</span> - by <span itemprop="author">Lucas</span>, <meta itemprop="datePublished" content="2011-03-25">March 25, 2011 <div itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating"> <meta itemprop="worstRating" content = "1"/> <span itemprop="ratingValue">4</span>/ <span itemprop="bestRating">5</span>stars </div> <span itemprop="reviewBody">Great microwave for the price. It is small and fits in my apartment.</span> </div> ... </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Product"> <span property="name">Kenmore White 17" Microwave</span> <img property="image" src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' /> <div property="aggregateRating" typeof="AggregateRating"> Rated <span property="ratingValue">3.5</span>/5 based on <span property="reviewCount">11</span> customer reviews </div> <div property="offers" typeof="Offer"> <!--price is 1000, a number, with locale-specific thousands separator and decimal mark, and the $ character is marked up with the machine-readable code "USD" --> <span property="priceCurrency" content="USD">$</span><span property="price" content="1000.00">1,000.00</span> <link property="availability" href="https://schema.org/InStock" />In stock </div> Product description: <span property="description">0.7 cubic feet countertop microwave. Has six preset cooking categories and convenience features like Add-A-Minute and Child Lock.</span> Customer reviews: <div property="review" typeof="Review"> <span property="name">Not a happy camper</span> - by <span property="author">Ellie</span>, <meta property="datePublished" content="2011-04-01">April 1, 2011 <div property="reviewRating" typeof="Rating"> <meta property="worstRating" content = "1"> <span property="ratingValue">1</span>/ <span property="bestRating">5</span>stars </div> <span property="reviewBody">The lamp burned out and now I have to replace it. </span> </div> <div property="review" typeof="Review"> <span property="name">Value purchase</span> - by <span property="author">Lucas</span>, <meta property="datePublished" content="2011-03-25">March 25, 2011 <div property="reviewRating" typeof="Rating"> <meta property="worstRating" content = "1"/> <span property="ratingValue">4</span>/ <span property="bestRating">5</span>stars </div> <span property="reviewBody">Great microwave for the price. It is small and fits in my apartment.</span> </div> ... </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Product", "aggregateRating": { "@type": "AggregateRating", "ratingValue": "3.5", "reviewCount": "11" }, "description": "0.7 cubic feet countertop microwave. Has six preset cooking categories and convenience features like Add-A-Minute and Child Lock.", "name": "Kenmore White 17\" Microwave", "image": "kenmore-microwave-17in.jpg", "offers": { "@type": "Offer", "availability": "https://schema.org/InStock", "price": "55.00", "priceCurrency": "USD" }, "review": [ { "@type": "Review", "author": "Ellie", "datePublished": "2011-04-01", "reviewBody": "The lamp burned out and now I have to replace it.", "name": "Not a happy camper", "reviewRating": { "@type": "Rating", "bestRating": "5", "ratingValue": "1", "worstRating": "1" } }, { "@type": "Review", "author": "Lucas", "datePublished": "2011-03-25", "reviewBody": "Great microwave for the price. It is small and fits in my apartment.", "name": "Value purchase", "reviewRating": { "@type": "Rating", "bestRating": "5", "ratingValue": "4", "worstRating": "1" } } ] } </script>

Structured representation of the JSON-LD example.

[Example 4](#eg-0011)

Copied

Example notes or example HTML without markup.

<img src="dell-30in-lcd.jpg" alt="A Dell UltraSharp monitor" /> Dell UltraSharp 30" LCD Monitor 87 out of 100 based on 24 user ratings $1250 to $1495 from 8 sellers Sellers: <a href="save-a-lot-monitors.com/dell-30.html"> Save A Lot Monitors - $1250</a> <a href="jondoe-gadgets.com/dell-30.html"> Jon Doe's Gadgets - $1350</a> ...

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Product"> <img itemprop="image" src="dell-30in-lcd.jpg" alt="A Dell UltraSharp monitor"/> <span itemprop="name">Dell UltraSharp 30" LCD Monitor</span> <div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating"> <span itemprop="ratingValue">87</span> out of <span itemprop="bestRating">100</span> based on <span itemprop="ratingCount">24</span> user ratings </div> <div itemprop="offers" itemscope itemtype="https://schema.org/AggregateOffer"> <meta itemprop="priceCurrency" content="USD" /> <span itemprop="lowPrice" content="1250">$1250</span> to <span itemprop="highPrice" content="1495">$1495</span> from <span itemprop="offerCount">8</span> sellers Sellers: <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <a itemprop="url" href="save-a-lot-monitors.com/dell-30.html"> Save A Lot Monitors - $1250</a> </div> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <a itemprop="url" href="jondoe-gadgets.com/dell-30.html"> Jon Doe's Gadgets - $1350</a> </div> </div> ... </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Product"> <img property="image" src="dell-30in-lcd.jpg" alt="A Dell UltraSharp monitor"> <span property="name">Dell UltraSharp 30" LCD Monitor</span> <div property="aggregateRating" typeof="AggregateRating"> <span property="ratingValue">87</span> out of <span property="bestRating">100</span> based on <span property="ratingCount">24</span> user ratings </div> <div property="offers" typeof="AggregateOffer"> <meta property="priceCurrency" content="USD" /> <span property="lowPrice" content="1250">$1250</span> to <span property="highPrice" content="1495">$1495</span> from <span property="offerCount">8</span> sellers Sellers: <div property="offers" typeof="Offer"> <a property="url" href="save-a-lot-monitors.com/dell-30.html">Save A Lot Monitors - $1250</a> </div> <div property="offers" typeof="Offer"> <a property="url" href="jondoe-gadgets.com/dell-30.html">Jon Doe's Gadgets - $1350</a> </div> ... </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Product", "aggregateRating": { "@type": "AggregateRating", "bestRating": "100", "ratingCount": "24", "ratingValue": "87" }, "image": "dell-30in-lcd.jpg", "name": "Dell UltraSharp 30\" LCD Monitor", "offers": { "@type": "AggregateOffer", "priceCurrency": "USD", "highPrice": "1495", "lowPrice": "1250", "offerCount": "8", "offers": [ { "@type": "Offer", "url": "save-a-lot-monitors.com/dell-30.html" }, { "@type": "Offer", "url": "jondoe-gadgets.com/dell-30.html" } ] } } </script>

Structured representation of the JSON-LD example.

[Example 5](#eg-0208)

Copied

Example notes or example HTML without markup.

<div> <!-- http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600 --> <span>315</span> <div> <img alt="Photo of product" src="http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg" /> <a href="http://multivarki.ru/brand_502/"> <span>BRAND 502</span> </a> <div> <span>4399 р.</span> </div>... <div> ... </div> </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/ItemList"> <link itemprop="url" href="http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600"><span itemprop="numberOfItems">315</span> <div itemprop="itemListElement" itemscope itemtype="https://schema.org/Product"> <img alt="Photo of product" itemprop="image" src="http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg"> <a itemprop="url" href="http://multivarki.ru/brand_502/"><span itemprop="name">BRAND 502</span></a> <div itemprop="offers" itemscope itemtype="https://schema.org/Offer"> <meta property="priceCurrency" content="RUB"> <span itemprop="price" content="4399.00">4399 р.</span> </div>... </div> <div itemprop="itemListElement" itemtype="https://schema.org/Product"> ... </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="ItemList"> <link property="url" href="http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600"><span property="numberOfItems">315</span> <div property="itemListElement" typeof="Product"> <img property="image" alt="Photo of product" src="http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg"> <a property="url" href="http://multivarki.ru/brand_502/"><span property="name">BRAND 502</span></a> <div property="offers" typeof="Offer"> <meta property="priceCurrency" content="RUB">руб <meta property="price" content="4399.00">4 399,00 <link property="itemCondition" href="https://schema.org/NewCondition"> </div>... </div> <div property="itemListElement" typeof="Product"> ... </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ItemList", "url": "http://multivarki.ru?filters%5Bprice%5D%5BLTE%5D=39600", "numberOfItems": "315", "itemListElement": [ { "@type": "Product", "image": "http://img01.multivarki.ru.ru/c9/f1/a5fe6642-18d0-47ad-b038-6fca20f1c923.jpeg", "url": "http://multivarki.ru/brand_502/", "name": "Brand 502", "offers": { "@type": "Offer", "priceCurrency": "RUB", "price": "4399.00" } }, { "@type": "Product", "name": "..." } ] } </script>

Structured representation of the JSON-LD example.

[Example 6](#eg-3475)

Copied

Example notes or example HTML without markup.

<h1>Crew neck white t-shirt</h1> <p>White t-shirt made of soft and lightweight cotton jersey, ensuring comfort, a refined mélange texture adds sporty appeal.</p> <a href="https://gs1.appareldemo.com/01/09506000164908">Manufacturer information</a>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div class="itemscope" itemtype="https://schema.org/Product"> <h1 itemprop="title">Crew neck white t-shirt</h1> <p itemprop="description">White t-shirt made of soft and lightweight cotton jersey, ensuring comfort, a refined mélange texture adds sporty appeal.</p> <a iteprop="hasGS1DigitalLink" href="https://gs1.appareldemo.com/01/09506000164908">Manufacturer information</a> <meta itemprop="gtin" content="09506000164908" /> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Product", "name": "Crew neck white t-shirt", "description": "White t-shirt made of soft and lightweight cotton jersey, ensuring comfort, a refined mélange texture adds sporty appeal.", "hasGS1DigitalLink": "https://gs1.appareldemo.com/01/09506000164908", "gtin": "09506000164908" } </script>

Structured representation of the JSON-LD example.

[Example 7](#eg-3617a)

Copied

Example notes or example HTML without markup.

Offer with free shipping in the US and Canada (in the V2 Shipping format).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Product", "name": "JSON Example", "offers": { "@type": "Offer", "shippingDetails": { "@type": "OfferShippingDetails", "height": "12 in", "width": "45 cm", "depth": "0.3 m", "weight": "1.2 kg", "hasShippingService": { "@type": "ShippingService", "shippingConditions": { "@type": "ShippingConditions", "shippingDestination": [ { "@type": "DefinedRegion", "addressCountry": "US" }, { "@type": "DefinedRegion", "addressCountry": "CA" } ], "shippingRate": "0" } } } } } </script>

Structured representation of the JSON-LD example.

[Example 8](#eg-3617c)

Copied

Example notes or example HTML without markup.

Offer with shipping costs of $10 + $1/kg for orders $35-$200, to the US and Canada, with a handling time of 3.5 hours on weekdays (in the V2 format).

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Product", "name": "JSON Example", "offers": { "@type": "Offer", "shippingDetails": { "@type": "OfferShippingDetails", "height": "12 in", "width": "45 cm", "depth": "300 mm", "weight": "1.2 kg", "hasShippingService": { "@type": "ShippingService", "handlingTime": { "@type": "ServicePeriod", "cutoffTime": "14:30:00-07:00", "duration": { "@type": "QuantitativeValue", "maxValue": "30", "unitCode": "min" } }, "shippingConditions": { "@type": "ShippingConditions", "shippingDestination": [ { "@type": "DefinedRegion", "addressCountry": "US" }, { "@type": "DefinedRegion", "addressCountry": "CA" } ], "orderValue": { "@type": "MonetaryAmount", "minValue": "35", "maxValue": "200" }, "shippingRate": { "@type": "ShippingRateSettings", "shippingRate": { "@type": "MonetaryAmount", "value": "10", "currency": "USD" }, "weightPercentage": "1.0" }, "transitTime": { "@type": "ServicePeriod", "duration": { "maxValue": "3.5", "unitCode": "h" }, "businessDays": [ { "dayOfWeek": "Monday" }, { "dayOfWeek": "Tuesday" }, { "dayOfWeek": "Wednesday" }, { "dayOfWeek": "Thursday" }, { "dayOfWeek": "Friday" } ] } } } } } } </script>

Structured representation of the JSON-LD example.

[Example 9](#eg-4505)

Copied

Example notes or example HTML without markup.

<strong>Château Snotty 2020</strong> The snottiest red wine on the market. <ul> <li>Organic red wine, made in France</li> <li>2020 Vintage, a very interesting year</li> <li>75 cl bottle</li> <li>Cru du Pichet d'Or</li> <li>Best before 2026</li> <li>Contains Sulfite</li> <li>Please recycle the glass bottle</li> </ul>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": { "@vocab": "https://schema.org/", "gs1": "https://ref.gs1.org/voc/", "unece": "https://vocabulary.uncefact.org/" }, "@graph": [ { "@type": [ "https://schema.org/DefinedRegion", "https://schema.org/PostalAddress" ], "@id": "http://example.com/lechateausnottyaddress", "addressCountry": "FR", "addressLocality": "L'Introuvable", "addressRegion": "Charentes" }, { "@type": ["QuantitativeValue", "gs1:QuantitativeValue", "unece:MeasureType"], "@id": "http://example.com/lechateausnottynetmass", "name": "Net mass", "unitCode": "KGM", "unitText": "kg.", "value": 0.75, "gs1:unitCode": "KGM", "gs1:value": 0.75, "unece:MeasureTypeValue": 75, "unece:MeasureTypeCode": "unece:WeightUnitMeasureCode#KGM", "unece:measuredAttributeCode": "unece:MeasuredAttributeCodeList#AAA" }, { "@type": ["QuantitativeValue", "gs1:QuantitativeValue", "unece:MeasureType"], "@id": "http://example.com/lechateausnottygrossmass", "name": "Gross mass", "unitCode": "KGM", "unitText": "kg.", "value": 1, "gs1:unitCode": "KGM", "gs1:value": 1, "unece:MeasureTypeValue": 1, "unece:MeasureTypeCode": "unece:WeightUnitMeasureCode#KGM", "unece:measuredAttributeCode": "unece:MeasuredAttributeCodeList#ACN" }, { "@type": [ "Organization", "gs1:Organization", "unece:TradeParty" ], "@id": "http://example.com/lechateausnotty", "name": "Domaine du Château Snotty", "address": { "@id": "http://example.com/lechateausnottyaddress" }, "unece:allianceName": "Les Châteaux obscurs de Charente" }, { "@type": [ "Organization", "gs1:Organization" ], "@id": "http://example.com/oenologuesatteres", "name": "Association des Œnologues attérés" }, { "@type": [ "Certification", "unece:TradeProductCertification" ], "@id": "http://example.com/certifiedpretentiouswine", "name": "Certified Pretentious Wine", "certificationIdentification": "pichetdor", "issuedBy": { "@id": "http://example.com/oenologuesatteres" }, "certificationRating": { "@type": "Rating", "ratingValue": "Pichet d'Or" } }, { "@type": [ "Product", "unece:TradeProduct", "gs1:Beverage" ], "name": "Château Snotty 2020", "description": [ { "@value": "The snottiest red wine on the market.", "@language": "en" }, { "@value": "Le vin le plus prétentieux du marché.", "@language": "fr" } ], "url": "https://www.example.com/chateau-snotty", "image": "https://www.example.com/chateau-snotty.jpg", "offers": { "@type": "Offer", "availability": "https://schema.org/InStock", "priceValidUntil": "2026-01-01", "price": "999.00", "priceCurrency": "EUR", "seller": { "@id": "http://example.com/lechateausnotty" }, "hasMerchantReturnPolicy": { "@type": "MerchantReturnPolicy", "applicableCountry": "EU", "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted" }, "shippingDetails": { "@type": "OfferShippingDetails", "shippingDestination": { "@type": "DefinedRegion", "name": "Europe", "addressCountry": "EU" }, "shippingRate": { "@type": "MonetaryAmount", "name": "Free", "value": 0, "currency": "EUR" }, "deliveryTime": { "@type": "ShippingDeliveryTime", "handlingTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 2, "unitText": "Days", "unitCode": "DAY" }, "transitTime": { "@type": "QuantitativeValue", "minValue": 1, "maxValue": 5, "unitText": "Days", "unitCode": "DAY" } }, "hasShippingService": { "@type": "ShippingService", "name": "Postal Service", "fulfillmentType": "https://schema.org/FulfillmentTypeDelivery", "shippingConditions": { "@type": "ShippingConditions", "shippingOrigin": { "@id": "http://example.com/lechateausnottyaddress" }, "orderValue": { "@type": "MonetaryAmount", "value": 100.0, "currency": "EUR" } } } } }, "manufacturer": { "@id": "http://example.com/lechateausnotty" }, "weight": [{ "@id": "http://example.com/lechateausnottynetmass" }, { "@id": "http://example.com/lechateausnottygrossmass" }], "productionDate": "2020-10-01", "hasCertification": { "@id": "http://example.com/certifiedpretentiouswine" }, "aggregateRating": { "@type": "AggregateRating", "ratingCount": 33, "ratingValue": 4.7, "bestRating": 5, "worstRating": 1 }, "review": { "@type": "Review", "reviewRating": { "@type": "Rating", "ratingValue": 5, "bestRating": 5, "worstRating": 1 }, "reviewBody": { "@value": "Oncques n'a jamais vu de vin plus prétentieux", "@language": "fr" }, "author": { "@type": "Person", "name": "Jean d'Eau" } }, "gs1:bestBeforeDate": "2027-01-01", "gs1:AdditiveDetails": { "@type": "gs1:AdditiveDetails", "gs1:additiveName": "Sulfite", "gs1:additiveLevelOfContainment": "gs1:LevelOfContainmentCode-CONTAINS" }, "gs1:netWeight": { "@id": "http://example.com/lechateausnottynetmass" }, "gs1:beverageVintage": "2020", "gs1:gpcCategoryCode": "10000276", "gs1:percentageOfAlcoholByVolume": 4.0, "gs1:vintner": "Domaine du Château Snotty", "gs1:alcoholicBeverageSubregion": "FR-16", "gs1:sweetnessLevelOfAlcoholicBeverage": "gs1:SweetnessLevelOfAlcoholicBeverageCode-DRY", "gs1:growingMethod": "gs1:GrowingMethodCode-ORGANIC", "gs1:packagingMarkedLabelAccreditation": "gs1:PackagingMarkedLabelAccreditationCode-EU_ECO_LABEL", "gs1:consumerSalesCondition": "gs1:ConsumerSalesConditionsCode-RESTRICTED_TO_SELL_16", "gs1:seller": { "@id": "http://example.com/lechateausnotty" }, "unece:specifiedMarking": { "@type": "unece:Marking", "unece:packagingMarkingTypeCode": [ "unece:PackagingMarkingCodeList#32", "unece:PackagingMarkingCodeList#9" ] }, "unece:fromDeliveryLifeSpanMeasure": { "@type": "unece:SupplyChainPackaging", "unece:DurationUnitMeasureCode": "unece:DurationUnitMeasureCode#MON", "unece:DurationUnitMeasureTypeValue": 6 }, "unece:recyclableIndicator": true, "unece:applicableTradeProductCertification": { "@id": "http://example.com/certifiedpretentiouswine" }, "unece:manufacturerParty": { "@id": "http://example.com/lechateausnotty" }, "unece:netWeightMeasure": { "@id": "http://example.com/lechateausnottynetmass" }, "unece:grossWeightMeasure": { "@id": "http://example.com/lechateausnottygrossmass" } } ] } </script>

Structured representation of the JSON-LD example.
