# Multitrack Testbed Scraper
Python utility that scrapes the [Multitrack Testbed database](http://multitrack.eecs.qmul.ac.uk/) to get a variety of detailed information about each of the available titles.

## Install
Clone the repo:
```
git clone https://github.com/BrianMargolis/MultitrackTestbedScraper.git
```
Install the prerequisites (into a virtual environment, probably):
```
> pip install -r requirements.txt
```

## Operation
```
> python scrape.py
```
The script creates a file, `track_information.json`, that contains detailed information on each of the tracks in the database. The full list of fields is:
* licenseType
* songType
* numberOfTracks
* numberOfStems
* composer
* mirrorLink
* issues
* title
* totalSize
* licenseType_uri
* comments
* numberOfMixes
* songType_uri
* recordingEngineer_uri
* song
* licenseFile
* recordingLocation
* artist
* artist_uri
* composer_uri
* recordingEngineer
* recordingDate
* link