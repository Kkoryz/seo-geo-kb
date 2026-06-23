---
title: "RestrictedDiet"
source_url: https://schema.org/RestrictedDiet
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# RestrictedDiet

# RestrictedDiet

A Schema.org Enumeration Type

- Canonical URL: https://schema.org/RestrictedDiet
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+RestrictedDiet)

A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons.

Instances of

[RestrictedDiet](/RestrictedDiet)may appear as a value for the following properties| Property | On Types | Description |
|---|---|---|
|
|

[MenuItem](/MenuItem)or[Recipe](/Recipe)#### Enumeration members

-
[DiabeticDiet](/DiabeticDiet) -
[GlutenFreeDiet](/GlutenFreeDiet) -
[HalalDiet](/HalalDiet) -
[HinduDiet](/HinduDiet) -
[KosherDiet](/KosherDiet) -
[LowCalorieDiet](/LowCalorieDiet) -
[LowFatDiet](/LowFatDiet) -
[LowLactoseDiet](/LowLactoseDiet) -
[LowSaltDiet](/LowSaltDiet) -
[VeganDiet](/VeganDiet) -
[VegetarianDiet](/VegetarianDiet)

### Examples

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
