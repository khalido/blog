---
title: "DSS-2018-07: Michael Allwright and Inna Kolyshkina"
date: 2018-07-12
description: "notes taken during/after this meetup"
tags:
- meetup
---

Data Science Sydney's [2018-07 meetup](https://www.meetup.com/Data-Science-Sydney/events/252700977).

- data literacy is important for senior execs who data scientists are workng for - there are courses out there for them

# Michael Allwright: "DATA FOR BAD OR GOOD? THE MINERVA COLLECTIVE"

> Michael is Co-Founder and CEO of The [Minerva Collective](http://www.minervacollective.org), a not for profit which uses data and data sharing for social good, and runs a data analytics consulting company focussed on using data for good.

- we all have tons of data being collected about us, by shops, banks, facebook, health records, etc
- its scary - which is why we have talks about data privacy etc
- see black mirror episode [nosedive](https://www.imdb.com/title/tt5497778/) and [China's social media score](https://www.wikiwand.com/en/Social_Credit_System) for people
- but there is lots of data being used for good
  - in developing countries blindness is being data treated
  - its helping cancer researchers detect early stage cancer using machine learning
  - neuroscience generates big big data - ML has the potential to deal with it
- getting back to Minerva
- 98K kids in the EU go missing every year - the police used telco data to analyze and break up kidnapping rings
- Mike studied pure math and did data work in the UK, like modelling building usage and which ones to shut down to save money
- onto corp work at PWC and an identity crisis - which led to travel, and a decision to focus on humans, became a hipster at Bondi beach talking about using data to change soceity... then... drumroll... the [data science breakfast meetup](https://www.meetup.com/The-Sydney-Data-Science-Breakfast-Meetup-Group/) was born (looks interesting, should go)
- wanted to do something good, but lots of issues about getting access to data to do stuff with, so joined up with Data republic to form the Minerva Collective. DR provides a secure platform and Minerva gets data and analysts on it to do data for good.
- run 6 events and many projects, a few examples:
- Domestive violence - effects 1/6 Aus women
  - ran several workshops with experts and groups.
  - learned perps want to change their behaviour but there are long waiting lists, so is there an opportunity to intervence earlier?
  - Uni of Melbourne is doing a lot of work here on collecting data, tracking ppl etc
  - learned can look at biometric data, telco and bank data of perps using machine learning to predict interventions, also provide awarness etc
- Financial Stress - 64% adults face financial stress in AU
  - developed a getting by index of financial stress hotspots
  - looking at bank data to build real time models to develop risk scores for a number of risk factors and use this for early interventions
- Solar power in Africa - ppl have more cellphones than power
  - there is lots of data, using this to predict best churn/agents/solutions etc
- and there is a lot more stuff they are doing
- think about: **what is my mission in data science?**

**q&a:**

- what tools to use?
  - most important is the ability to frame the problem and deliver a simple solution visually.
- domestic violence data sources are very private, how did they get?
  - this was done as part of a NSW initiative where they incentivzed preps to opt-in to share their data
- DV is often under-reported, so is the data reliable?
  - the Uni of Melbourne was tracking perps
- how do you go from proof of concept to actually ruling out?
  - biggest challange is this, to move on from concepts and hackathons to something operational.
  - has gotten a lot of traction in the consulting side
- take on AI ethics
  - not sure, but there is a broad spectrum - from WMD's to targetting ppl to help them

# Inna Kolyshkina: "USING DATA SCIENCE METHODS FOR PREDICTIVE ASSET MANAGEMENT FOR A LARGE AUSTRALIAN UTILITIES COMPANY. USE CASE."

>  Inna Kolyshkina is Director of Data Science in [Analytikk Consulting Services](http://analytikk.com), a Data Analytics consultancy.

> This talk describes a recent project delivered to a large Australian utilities company [..] it enabled the organisation to proactively identify problematic or costly assets prior to asset failure and to use predicted future costs to inform annual maintenance planning.

- founded [IAPA](https://www.iapa.org.au/), first data scientist at a big4 in Australia
- Predictive Asset Management analytics - asset owning companies want to proactively optimize maintainence planning and prevent failures
- in the past, client used common sense - this doesn't work to well. Of the shelf solutions developed for other countries didn't work too well either, and regulators wanted better/local ones (company had to justify funding to regulators)
- had 12 years of data, which they wanted to use to forecast the next 10 years of asset maintainence cost, failure occurence and duration for several types of assets
- solution had to be transparent and auditable, easy to implement and compliant with regulation
- Data was huge and untidy - this is normal. millions of records, 500 variables, different types
  - only 15 years of data and they wanted 10 years of prediction
  - it was sparse, high levels of random variation, lots of zeros, and so on
- convential view was a bathtub curve - new asset increases reliability, decreases cost, enters mature phase then cost and failures go up with age. this was wrong
- after initial data eval, had to go back to tell them data wasn't enough, added more data like climate etc
- used standard data science models like decision trees, boosting, random forests (more) to data science the data. three models were fit for each data type
- finally, expressed models as decision treer, combined with classic techniques

**q&a**

- how to optimize model?
  - first did feature selection - so already knew all the important factors / significant predictors - looked at deviance, r-squared, lasso regression, then fit a GLM model
- how did you get all these data sciencey things across to the old school company?
 - key was that clients were engineers, they could understand.
 - Have to build trust and gain respect - did a proper requirements collection, understood what they had already done, explained where else the data science techniques worked
 - build a proof of concept, walked them through it. had several meetings around the proof of concept
- objective measures - how did the DS forecasts compare to their engineering judgements?
 - asked stakeholders - when will you believe the model resutls?
 - regulators hire econmetricians who just use linear models, don't understand data science - so the final linear model makes sense to them
 - tested model on data they hadn't seen
 - main interest of the client was to find the most expensive assets
- energy space is tough as regulator is more innumerate than the models - how did they percieve this?
  - they used data science methods for feature selection and then choose a linear model - so it was understandable
  - client played regulator with the consultant and asked difficult questions, etc
- data enrichment - how did they know what/which more to get?
  - asked the client what other data would be useful/relevant to the question - they already knew what could be relevant
- data cleanup
  - audited the data, got business rules, basic checks
  - the zero data - e.g some assets have very low failure rates so there isn't much failure data - used special stats techniques there
- what would they say to the regulator?
  - send them to a data literacy course
  - talk about whats happening in the world, mainstream methods data scienctists are using, stats reference
- what did you spend the most time on?
  - data audit, checks and cleaning
- did you consider other approaches like interpretative model?
  - regulators hire consultants, who are generally econometrician, who accept linear models, otherwise they would have used decision trees or something like that