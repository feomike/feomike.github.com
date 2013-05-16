---
layout: posts
title: DevEx Days
desc: Recently at the FCC, we held an unusual day.  We call it D(f)evEx (pronounced as either devex or fedex) Days, and this was our first ever.  The idea stems from fedEx, where something needs to be delivered (as in 'to production') in 24 hours; combined with a developer day. We took the opportunity to take a time out for our day to day grind, and promise to each other that we would produce working product in the next 24 hours; in essence a focused day of learning new skills, or honing existing ones, NOT part of our regular duties.
shortdesc: Recently at the FCC, we held an unusual day.  We call it D(f)evEx (pronounced as either devex or fedex) Days, and this was our first ever.
permalink: /post/devex-days.html
---
Recently at the FCC, we held an unusual day.  We call it D(f)evEx (pronounced either as devex or fedex) Days, and this was our first ever.  The idea stems from fedEx, where something needs to be delivered (as in production) in 24 hours; combined with a developer day. We took the opportunity to take a time out for our day to day grind, and promise to each other that we would produce working product in the next 24 hours; in essence a focused day of learning new skills, or honing existing ones, NOT part of our regular duties.

We wanted to test this out as an institutional innovation development kind of thing.  How could we spur some innovation, have some fun, and produce some product?  Rather than a forming a subcommittee to plan a meeting date to decide if we could bring in some facilitators and flesh out some objective learning, we said, lets just try a focused day of developing; developing whatever we want. The results are fascinating.  

Here were the rules. 

1. Say what you were planning on doing.  We all gathered for a morning meeting at 8:30 am.  At that meeting each person had 2 minutes to describe what we were going to work on for the next day.  For your 2 minutes you needed to say what your intent was, what you wanted to deliver, and what was the outcome.  The reason we did it this way was to institute peers holding to peers.  If you promise to your peers you were going to do something, you had better deliver.  

2. Work on that for the next 24 hours; phone off, email off, calendar blocked out, no distractions, just code.  The work product you were planning shouldn't be part of your normal work activities.

3. Present results.  At 2 pm the next day, come back together.  Everyone has 10 minutes to present their product, followed by 5 minutes of questions, critiques and the like.  The presentations generally followed, this is what I set out to do, this is what I ended up doing, this is what I learned, and this is why its important.  The questions were generally things like why didn't you do it this way, thats cool, what would you do next.

##Results

Every single participant presented working results mostly on github.

####Participant: **Greg Elin**

Greg worked with Vagrant.  He wanted to see if he could use Vagrant to build a machine that would be an ideal development box for open data.  His results were spectacular[Greg's Vagrant Project](https://github.com/gregelin/vagrant_php-pgsql).  How might this be something bigger than just some side project, well watch here to see if it keeps building.

####Participant: **Don Harris** 

Don worked with a Python library called matplotlib.  He wanted to see if he could use a new to the FCC Python library to create simple charts out of resulting geospatial analysis.  His example data was travel times to work.  His [full project](https://github.com/geodon7399/FedEx) describes how he did it and everything, including [code](https://github.com/geodon7399/FedEx/blob/master/md_travel_times.py) and [results](https://github.com/geodon7399/FedEx/blob/master/md_travel_times.png).

####Participant: **Santosh Moghulla**

Santosh wanted to work with elastic search.  What was really impressive to me on this project, what the speed with which the returns came from the example datasets, with seamingly little tuning.  Santosh's [full code](https://github.com/smoghull/elasticsearch-demo) is a little deep because it works on data we here are all familiar with, but take a look; elastic search is a great tool.

####Participant: **Michelle Morawski**

Shelley wanted to work with a geospatial application we don't currently employ here at the FCC.  So she worked with [MapStory](http://mapstory.org/).  She had some great content working with Shark Attacks in Florida (we still haven't discussed why), and had some interesting challenges with geocoding and spatial aggregation.  Her [example](http://mapstory.org/maps/526/) shows a great opportunity for simple maps.  

####Participant: **Paul Salaznyk**

Paul wanted to focus on data.  He took data from the National Quality Assessment of the National Broadband Map.  This [data](http://www.broadbandmap.gov/about/technical-overview/data-review) is a comprehensive comparison of each and every record published by the national broadband map to as many as 4 third party dataset for the most intensive quality assessment that can be done.  Pauls [results](http://psalaz.github.io/bbmap-quality/) are a great look at the largest nationwide providers and the quality of the NBM compared to other sources.  The data for Pauls project are from [the wireline](http://www.broadbandmap.gov/developer/api/wireline-broadband-api) and [wireless](http://www.broadbandmap.gov/developer/api/wireless-broadband-api) apis.

####Participant:  **Anne Levine**

Anne is a policy analyst who has never written code.  She decided to challenge herself to write a web form which accepts input and writes output to a csv file on a web server.  _HOW COOL IS THAT!_ She has never written code before.  Anne's example is working on an internal server at FCC, so we can't share it here.  But you can follow her on [github](https://github.com/alevinefcc).

####Participant:  **Nathaniel Guieb**

Nathaniel, a UI developer, recognized our future direction on dynamic charting wanted to compare two tools for charting.  He choose [highstock](http://www.highcharts.com/products/highstock) and [rickshaw](http://code.shutterstock.com/rickshaw/).  His comparison used the same stock data and these different libraries illustrating pros and cons for future use.  His results are; (1) [Compare multiple stocks built with HighStock](http://vizui.github.com/ts-demo/hs-compare-multi-co.html), (2) [Compare open, high, low, close prices of one stock built with HighStock](http://vizui.github.com/ts-demo/hs-compare-multi.html) and (3) [Compare open, high, low, close prices of one stock built with Rickshaw](http://vizui.github.com/ts-demo/rs-line.html).

####Participant:  **Xiaoming Qin**

Xiaoming wanted to play geospatial data (in this case data from the Washington D.C. Capital Bike Share) and see if he could connect two geospatial libraries in a single web page environment.  His example uses leaflet in a dynamic query to talk to D3 in the same page.  We think there are great opportunities to use this in future applications.  His [code](https://github.com/xqin1/bikeshare) and [live demo](http://xqin1.github.com/bikeshare/bike1.html) are of course pubicly available

####Participant: **Eric Spry**

Eric was gung ho to look at the [SDK](http://mapbox.com/mobile/) for MapBox on the iOS.  His intent was to explore what it would take for us to make our own FCC mobile mapping application.  Eric didn't publish his work on git, but you can check out his other killer work like FCCs [time series demo](http://fcc.github.io/lpfmpoints/lpfmpoint.html) of low power FM stations coming on line.

_Particpant:_  **Mike Byrne**

I wanted to play with how to get files into the geoJson format.  Seeing that many organizations only have ESRI sofware, particularly in government, and that ESRI doesn't give you good alternatives to create open formats for their data, I created the project [esri2open](https://github.com/project-open-data/esri2open).  I also made this [presentation](https://docs.google.com/presentation/d/1Ixsw344VvUEznYD2E4rO9yoBo4LoeU7vW7rEGeXoHGY/edit?usp=sharing) to describe the project.

####Participant:  **Chris Gao**

Chris, a specialist in our Engineering Office wanted to work on how to find broadcast stations better.  You can search by call sign, facility id, and city/state now. His demo was only on a subset of data, but showed a fully scaleable project.  Check out his [code](https://github.com/gaochris1/tvstudy/) and [demo](http://gaochris1.github.io/tvstudy/index.html#)

##Notes
We pulled off 11 products in 24 hours.  None of these products required procurement!  Not one.  Just about all of them had production on the www, without having to buy a server, software or licenses.  I am pretty sure this is what innovation is all about.  I am excited about the results and look forward to doing this again.  

To us, the big idea is that we turn the normal process of bringing new skillsets in house on its ear; The government doesn't write a requirement to include "new widget x", we instead say to developers, bring us what you think is interesting and something you want to learn. Not only does that change the dynamic of standard top-down style, but it empowers developers (and all of us) to bring their energy and passion to something entirely new. 

Continuous learning and growth also makes us a more nimble agency, moving away from monolithic system architectures to portable, changeable, flexible; largely based on open source tools. This not only makes us capable of utilizing the cutting edge in development, but allows us to be a contributor back to the larger community of open government.

In speaking with all of the participants, they have all said they were super excited about the opportunity to participate and the results.  We got to learn from each other and really take some of our results and turn them into new production products.  
