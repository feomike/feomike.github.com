---
layout: posts
title: FAA Airport Closures
desc: Working on a previous conclusion that perhaps PDFs are not a great way to release data, and that indeed information like this is a) easy to produce and b) very cheap to publish and host as rich interactive content, I took the short time to open this data and make it releasable.  Below is the dynamic map which is the result.
shortdesc: Working on a previous conclusion that perhaps PDFs are not a great way to release data.
permalink: /post/faa-airport-closures.html
--- 
On Friday, March 22, 2013, the Federal Aviation Administration released this [press release](http://www.faa.gov/news/press_releases/news_story.cfm?newsId=14414) describing a "decision that 149 federal contract towers will close beginning April 7 as part of the agency’s sequestration implementation plan." 

In addition to the release was a [document](http://www.faa.gov/news/media/fct_closed.pdf) listing the individual name, city, state and airport identification signs of those towers to be closed.

Working on a previous [conclusion](http://feomike.github.com/posts/2013/state_seq) that perhaps PDFs are not a great way to release data, and that indeed information like this is a) easy to produce and b) very cheap to publish and host as rich interactive content, I took the short time to open this data and make it releasable.  Below is the dynamic map which is the result.

##How I Did It
I first copied the data from the pdf above, into this [text](../../data/faa_closed_20130322.csv).  This 'data file' is essentially one row per newly proposed closed airport by the FAA.  I saved that document to an excel file, and uploaded that file to [this google document sheet](https://docs.google.com/spreadsheet/ccc?key=0Aooxb2GcQ9ifdDRWOVBLUU1ocHRuNFRSUjNwVUZjYmc&usp=sharing).  I edited the columns slightly, to concatenate the columns (see column F) into a more readible place name; one that was more likely to be found by a geocoder.  I then used [this process](http://mapbox.com/blog/mapping-google-doc-spreadsheet/) to associate each row (e.g. airport) with its latitude and longitude.

The same [tool](http://mapbox.com/blog/mapping-google-doc-spreadsheet/) described above, contains a way to export this newly geocoded file to a geoJson file.  I performed that export, which is [this file](../../data/FAA_closed_20130322.geojson).

I then used [TileMill](http://mapbox.com/tilemill/) to create a simple map of these locations.

For all intents and purposes, this process was essentally free and took little time to produce.

## Results

<iframe width='100%' height='400' frameBorder='0' src='http://a.tiles.mapbox.com/v3/feomike.map-vl7gh805.html#4/38/-96.60'></iframe>
[View full map](http://a.tiles.mapbox.com/v3/feomike.map-vl7gh805.html#4/38/-96.60)

####Data
The new data files can be found below and so can a brief description of how I did this.

- [Data File - geojson](/data/FAA_closed_20130322.geojson)
- [TileMill Map Project Fle](/maps/faa_20130322.mml)

##Notes
The process is simple repeatable, but more importantly, the impact of the news item is much more clearly represented.  In my (our) previous experiment, independent [new applications](http://chelm.github.com/state_seq/examples/states.html) sprung up.  I expect the same might be true here.