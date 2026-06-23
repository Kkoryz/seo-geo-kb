---
title: "NutritionInformation"
source_url: https://schema.org/NutritionInformation
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2017-03-02
---

# NutritionInformation

# NutritionInformation

A Schema.org Type

- Canonical URL: https://schema.org/NutritionInformation
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+NutritionInformation)

Nutritional information about the recipe.

| Property | Expected Type | Description |
|---|---|---|
| Properties from
|

```
```[calories](/calories)

[Energy](/Energy)```
```[carbohydrateContent](/carbohydrateContent)

[Mass](/Mass)```
```[cholesterolContent](/cholesterolContent)

[Mass](/Mass)```
```[fatContent](/fatContent)

[Mass](/Mass)```
```[fiberContent](/fiberContent)

[Mass](/Mass)```
```[proteinContent](/proteinContent)

[Mass](/Mass)```
```[saturatedFatContent](/saturatedFatContent)

[Mass](/Mass)```
```[servingSize](/servingSize)

[Text](/Text)```
```[sodiumContent](/sodiumContent)

[Mass](/Mass)```
```[sugarContent](/sugarContent)

[Mass](/Mass)```
```[transFatContent](/transFatContent)

[Mass](/Mass)```
```[unsaturatedFatContent](/unsaturatedFatContent)

[Mass](/Mass)[Thing](/Thing)

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

[NutritionInformation](/NutritionInformation)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[MenuItem](/MenuItem)or[Recipe](/Recipe)### Examples

[Example 1](#eg-0013)

Copied

Example notes or example HTML without markup.

Mom's World Famous Banana Bread By John Smith, May 8, 2009 <img src="bananabread.jpg" alt="Banana bread on a plate" /> This classic banana bread recipe comes from my mom -- the walnuts add a nice texture and flavor to the banana bread. Prep Time: 15 minutes Cook time: 1 hour Yield: 1 loaf Tags: Low fat Nutrition facts: 240 calories, 9 grams fat Ingredients: - 3 or 4 ripe bananas, smashed - 1 egg - 3/4 cup of sugar ... Instructions: Preheat the oven to 350 degrees. Mix in the ingredients in a bowl. Add the flour last. Pour the mixture into a loaf pan and bake for one hour. 140 comments: From Janel, May 5 -- thank you, great recipe! ...

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Recipe"> <span itemprop="name">Mom's World Famous Banana Bread</span> By <span itemprop="author">John Smith</span>, <meta itemprop="datePublished" content="2009-05-08">May 8, 2009 <img itemprop="image" src="bananabread.jpg" alt="Banana bread on a plate" /> <span itemprop="description">This classic banana bread recipe comes from my mom -- the walnuts add a nice texture and flavor to the banana bread.</span> Prep Time: <meta itemprop="prepTime" content="PT15M">15 minutes Cook time: <meta itemprop="cookTime" content="PT1H">1 hour Yield: <span itemprop="recipeYield">1 loaf</span> Tags: <link itemprop="suitableForDiet" href="https://schema.org/LowFatDiet" />Low fat <div itemprop="nutrition" itemscope itemtype="https://schema.org/NutritionInformation"> Nutrition facts: <span itemprop="calories">240 calories</span>, <span itemprop="fatContent">9 grams</span> fat </div> Ingredients: - <span itemprop="recipeIngredient">3 or 4 ripe bananas, smashed</span> - <span itemprop="recipeIngredient" itemscope itemtype="https://schema.org/PropertyValue"><span itemprop="value">1</span> <span itemprop="name">egg</span></span> - <span itemprop="recipeIngredient" itemscope itemtype="https://schema.org/PropertyValue"><span itemprop="value">3/4</span> <meta itemprop="unitCode" content="G21">cup of <span itemprop="name">sugar</span></span> ... Instructions: <span itemprop="recipeInstructions"> Preheat the oven to 350 degrees. Mix in the ingredients in a bowl. Add the flour last. Pour the mixture into a loaf pan and bake for one hour. </span> 140 comments: <div itemprop="interactionStatistic" itemscope itemtype="https://schema.org/InteractionCounter"> <meta itemprop="interactionType" content="https://schema.org/CommentAction" /> <meta itemprop="userInteractionCount" content="140" /> </div> From Janel, May 5 -- thank you, great recipe! ... </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Recipe"> <span property="name">Mom's World Famous Banana Bread</span> By <span property="author">John Smith</span>, <meta property="datePublished" content="2009-05-08">May 8, 2009 <img property="image" src="bananabread.jpg" alt="Banana bread on a plate" /> <span property="description">This classic banana bread recipe comes from my mom -- the walnuts add a nice texture and flavor to the banana bread.</span> Prep Time: <meta property="prepTime" content="PT15M">15 minutes Cook time: <meta property="cookTime" content="PT1H">1 hour Yield: <span property="recipeYield">1 loaf</span> Tags: <link property="suitableForDiet" href="https://schema.org/LowFatDiet" />Low Fat <div property="nutrition" typeof="NutritionInformation"> Nutrition facts: <span property="calories">240 calories</span>, <span property="fatContent">9 grams</span> fat </div> Ingredients: - <span property="recipeIngredient">3 or 4 ripe bananas, smashed</span> - <span property="recipeIngredient" typeof="PropertyValue"><span property="value">1</span> <span property="name">egg</span></span> - <span property="recipeIngredient" typeof="PropertyValue"><span property="value">3/4</span> <meta property="unitCode" content="G21">cup of <span property="name">sugar</span></span> ... Instructions: <span property="recipeInstructions"> Preheat the oven to 350 degrees. Mix in the ingredients in a bowl. Add the flour last. Pour the mixture into a loaf pan and bake for one hour. </span> 140 comments: <div property="interactionStatistic" typeof="InteractionCounter"> <meta property="interactionType" content="https://schema.org/CommentAction" /> <meta property="userInteractionCount" content="140" /> </div> From Janel, May 5 -- thank you, great recipe! ... </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Recipe", "author": "John Smith", "cookTime": "PT1H", "datePublished": "2009-05-08", "description": "This classic banana bread recipe comes from my mom -- the walnuts add a nice texture and flavor to the banana bread.", "image": "bananabread.jpg", "recipeIngredient": [ "3 or 4 ripe bananas, smashed", { "@type": "PropertyValue", "value": 1, "name": "egg" }, { "@type": "PropertyValue", "value": "3/4", "name": "sugar", "unitCode": "G21"} ], "interactionStatistic": { "@type": "InteractionCounter", "interactionType": "https://schema.org/Comment", "userInteractionCount": "140" }, "name": "Mom's World Famous Banana Bread", "nutrition": { "@type": "NutritionInformation", "calories": "240 calories", "fatContent": "9 grams" }, "prepTime": "PT15M", "recipeInstructions": "Preheat the oven to 350 degrees. Mix in the ingredients in a bowl. Add the flour last. Pour the mixture into a loaf pan and bake for one hour.", "recipeYield": "1 loaf", "suitableForDiet": "https://schema.org/LowFatDiet" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0385)

Copied

Example notes or example HTML without markup.

A simple menu example with a single menu section for tacos and a taco menu item. Note that additional menus are possible for specific languages using the inLanguage property.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"Restaurant", "url":"http://www.somerestaurant.com", "name":"Some Restaurant", "description":"This is the Some Restaurant located on 345 Spear St. San Francisco, 94105 CA. It serves Indian-Mexican fusion cuisine", "servesCuisine":[ "Indian-Mexican Fusion" ], "hasMenu":{ "@type":"Menu", "hasMenuSection":{ "@type":"MenuSection", "name":"Tacos", "description":"Tacos inspired by India cuisine.", "image":[ "https://somerestaurant.com/some_tacos.jpg", "https://somerestaurant.com/more_tacos.jpg" ], "offers":{ "@type":"Offer", "availabilityEnds":"2017-03-02T08:22:00", "availabilityStarts":"2017-03-02T08:22:00" }, "hasMenuItem":{ "@type":"MenuItem", "name":"Aloo Gobi Taco", "description":"Mexico City-style street corn tortilla taco filled with a flavorful mixture of mildly south Indian spiced cauliflower, potato, tomato, onions and bell peppers.", "offers":{ "@type":"Offer", "price":"3.50", "priceCurrency":"USD" }, "nutrition":{ "@type":"NutritionInformation", "calories":"170 calories", "fatContent":"3 grams", "fiberContent":"2 grams", "proteinContent":"4 grams" }, "suitableForDiet":"https://schema.org/GlutenFreeDiet" } }, "inLanguage":"English" } } </script>

Structured representation of the JSON-LD example.

[Example 3](#eg-0386)

Copied

Example notes or example HTML without markup.

An example of a menu with nested MenuSections.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"Restaurant", "url":"http://www.thisisarestaurant.com", "name":"The Restaurant", "image":"http://www.example.com/image-of-some-restaurant.jpg", "description":"This is an example restaurant that serves American cuisine.", "servesCuisine":[ "American cuisine" ], "hasMenu":{ "@type":"Menu", "name":"Dine-In Menu", "description":"Menu for in-restaurant dining only.", "hasMenuSection":[ { "@type":"MenuSection", "name":"Dinner", "description":"Dinner dishes", "image":"https://thisisarestaurant.com/dinner_dishes.jpg", "offers":{ "@type":"Offer", "availabilityEnds":"2017-03-02T08:22:00", "availabilityStarts":"2017-03-02T08:22:00" }, "hasMenuSection":[ { "@type":"MenuSection", "name":"Starters", "description":"Appetizers and such", "image":"https://thisisarestaurant.com/starter_dishes.jpg", "offers":{ "@type":"Offer", "availabilityEnds":"2017-03-02T08:22:00", "availabilityStarts":"2017-03-02T08:22:00" }, "hasMenuItem":{ "@type":"MenuItem", "name":"Potato Skins", "description":"Small serving of stuffed potato skins.", "offers":{ "@type":"Offer", "price":"7.49", "priceCurrency":"USD" }, "suitableForDiet":"https://schema.org/GlutenFreeDiet" } }, { "@type":"MenuSection", "name":"Soups & Salads", "description":"Salads and a few choices of soup", "image":"https://thisisarestaurant.com/soup_and_salad_dishes.jpg", "offers":{ "@type":"Offer", "availabilityEnds":"2017-03-02T08:22:00", "availabilityStarts":"2017-03-02T08:22:00" }, "hasMenuItem":{ "@type":"MenuItem", "name":"Pea Soup", "description":"Creamy pea soup topped with melted cheese and sourdough croutons.", "offers":{ "@type":"Offer", "price":"3.49", "priceCurrency":"USD" } } } ] } ] } } </script>

Structured representation of the JSON-LD example.
