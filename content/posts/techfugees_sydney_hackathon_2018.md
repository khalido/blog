---
title: "Techfugees Sydney Hackathon 2018"
date: 2018-11-23
tags:
- hackathon
---

This hackathon is about developing tech solutions to the challanges refugees face.

- [Hackathon Details](https://www.eventbrite.com.au/e/techfugees-sydney-hackathon-in-blacktown-2018-tickets-50896768605), [twtr](https://twitter.com/techfugeesaust1), [#Hack4Refugees](https://twitter.com/hashtag/Hack4Refugees)

# kickoff

- [Annie](https://twitter.com/annie_parker) introduced the hackathon as a means to bringing ppl together to solve problems. Tech ppl should and can contribute to issues - this is the fourth techfugee hackathon in Sydney.
- NGO partners:
  - [SSI](https://www.ssi.org.au/) is the largest settlement ngo in Australia
  - [Startts](http://www.startts.org.au/) works on torture and trauma
- pick a theme from out of 10, and think about how your product fits needs, who does it help, etc etc.
  - what problems do users face, why, and is this a problem or symptom?
  - is the problem actually solvable with your idea/proposal?
  - what kind of skills are needed for your idea?
- pitch: introduce someone, set scene, the problem and then the solution and its impact (KISS)
- [dev site](https://techfugees-australia-2018.devpost.com/)

## hackathon themes

Dour - works wth [SSI](https://www.ssi.org.au/). Works with communities to empower ppl to change their lives - 800+ staff. Spoke about themes for the hackathon:

- how to support ppl past the 5yr refegee suport eligibilit period?
  - programs like language, documents, jobs, social networks, career dev, etc etc
- how to address the culture gap?
- Access to housing
- issues with justice and crime - lack of support for ppl who come out of juvie or jail
- disability - increasing disability in newly arrived refugees
- language
- mental health
- domestic and family violence
- transtion from education to jobs/life - outcomes aren't great

## Refugee stories

Mentors for teams to understand the usefullness of what they're building:

Enya:

- started [misssahara.com](https://www.misssahara.com/) - beauty pageant for African women
- grew up in Blacktown, met lots of barriers. studied at UNSW, Masters in Intl Dev
- a lot of young ppl can't get involved in programs and services as they have been here for more than 5 years

Luqman

- from Malaysia, was in a kids refugee for 7 years, came to Australia at age 11 in 2013
- went to school for the first time (no schooling in kids refugee) in Australia, tough, hung out with wrong ppl
- now at Homebush Bay, hacker, age 15

engineer lady

- studying to be a civil engineer, wrote a poetry book
- not eligible for HECS - why does she need to be certified as a refugee when she is already here as a refugee?
- platform to find and match scholarships?
- refugees need equality

Dour

- from south Sudan
- got scholarship from an org in Kings Cross, changed his life
- support in the local settlement areas is very important, defines the kind of things they end up doing

Salima and ? (from Afghanistan)

- Nurse, youth worker, help refugees to settle in
- biggest challanges: english, isolated becuase of the that, helped to meet and befriend others from Afghanistan
- Didn't know about services avaialble to her - found out about SSI 4 yrs after arriving in Australia
- What supports do they wish existed?

# My idea: AikBot

There are lots of things people are working on, as well as tons of existing information out there.

Prototype:

![](/img/prototype_chat_1.png) ![](/img/prototype_chat_2.png)

Have a simple, easy to use way to ask questions about services available, and where possible help the user to use them by asking questions relevant for that service and filling out the form (or sending the relevant link).


- remembers user info entered, making it more useful over time (cause it remembers all the info entered)
- two main uses:
  - answers questions, like what scholarships are available, nearby migrant relevant centers, etc etc
  - fills out forms, starting with school forms (then medicare, centrelink, whatever could be useful…)

More advanced:

- use google translate to ask questions in the users native language, and then translate back the answers to fill out forms in english


## plan

[x] get prototype up and running
[ ] setup python/flask powered API endpoint which takes in data and returns answers, forms etc
[ ] TALK TO THE RIGHT PPPL then
[ ] make a top ten list of useful qs the bot can answer and put info in airtable/gsheets
  - scholarships, schools, nearby services
  - list of useful free apps for migrants and what they can do

## Tools

- https://manychat.com to do all the chat stuff
- https://glitch.com to run the backend to take in input, parse it and return a answer
- Google Sheets - API
- https://airtable.com - database backend
- consider using rasa stack for the chatbot - its an opensource AI bot framework which makes it easy to customize & plugin other services like translation, answers, wikipedia, everything
- [flask-restplus](https://flask-restplus.readthedocs.io/en/stable/quickstart.html) - build apis using flask

## look at

- https://refugeetalent.com/ - conencting refugees to jobs
- onestepapp - connects ppl for walks
- [donotpay bots](https://motherboard.vice.com/en_us/article/bj43y8/donotpay-app-lets-you-sue-anyone-by-pressing-a-button)

# Pitches

## the belong program

- supplement existing migrant programs
- provide confidence to refugees
- connects refugees to others, volunteers
- judges loved it, special mention

## help migrant children integrate in schools

- refugee children drop out of school at 5x
- build profiles for kids so teachers can understand them better and how to help in class
- provide customized lesson plans for refugees
- cultural context, sourced from multiple ngo's
- optional: migrant's personal story

## firstpath

- school is tough for new migrants - simple things like selecting subjects is impossible
- don't know where to get help, end up choosing the wrong subjects for them, lots of regret
- solution: provide user friendly content, scrape in real time from sources
- make content for younger kids, not enough help content
- first prize winners

## Amplify/Unify techfugees website & outreach

- fixing/updating techfugees website and social presence
- unify all their challanges
- much needed work which needed to happen

## recruit refugees from where they are

- works with partner companies to find refugees
- recruit refugees remotely
- six visas lodged, couple in the pipeline

## sheila caceres

- http://sheilacaceres.com
- teach language immersively by using AR glasses to project names on objects
- objects are labelled in your language, you can hear too

## young h4ck3rs

- pair ppl with relevant others using a chatbot
- help refugees connect, build community
- #findmyself
- third place

## elavate

- match migrants to internships, opportunities
- database of opportnities, tailors to ppl, translates to their language
- already got one refugee an internship in the field she wanted - IT
- uses a website which asks questions to narrow down the universe of internships/jobs, and presents a list along with adivce videos tailored to help apply for that kind of job
- second place

# wrapup

- its not about winning hackathons, its the long term effort. refugeetalent didn't win their hackathon, but was the most successful outcome from all the hackathons
- 3 yrs ago, [onestepapp](https://twitter.com/onestepapp) won third prize, but went on to setup an actual thing, came back to a meetup to present, still going on
- meetup in three months
- techfugees encourages hackathoners to think of themselves as part of their community and keep doing stuff
- thanks to all the sponsors:
  - Settlement Services Australia
  - STARTTS
  - Academy XI
  - Devpost
  - Microsoft for Startups
  - Chief Disrupter
  - Spark Festival
  - Blacktown Venue

