# CricketersSearchEngineTamil


Directory Structure
---
```
 ├── analyzers : Custom filters (Stemmers,synonyms)
 ├── cricketersNew.xlsx : scrapped data
 ├── scraping.py : script used to data collection.
 ├── dataUpload.py : Python file that converts xlsx file to a bulkdata and uploads to ElasticSearch Bulk API (configurations for indexing)
```

Demo
---
* Install ElasticSearch and kibana
* copy analysis folder from project directory to config of Elasticsaeach
* Run ElasticSearch and kibana
* Run 'dataUpload.py' to add index and add data
* Go to http://localhost:5601/app/dev_tools#/console
* Search the following sample queries

SampleQueries
---
* Can search with generic query in all the fields.
```
{
  "_source": ["முழு பெயர்" ,"பங்கு","நாட்டு அணி","அறிமுகம்"],
  "size": 5,
  "query": {
    "query_string": {
      "query":"முத்தையா"
    }
  }
}
```
* Can search specifying the field.
```
{
     "_source": ["முழு பெயர்" ,"பங்கு","நாட்டு அணி","அறிமுகம்"],
     "size": 5,
     "query" : {
      	"match" : {
            "பங்கு":"பந்து வீச்சாளர்"
         }
     }
 }
```
* Can search with WildCard queries.
 ```{
     "query" : {
          "match" : {
             "பங்கு":"பந்து*"
         }
     }
 }
 ```
* Can search one term might  in multiple fields
```
{
      "query" : {
         "multi_match" : {
             "query" : "பந்து வீச்சாளர்",
             "fields": [""பங்கு","அறிமுகம்"]
         }
     }
}
```
* Can search for the phrase query
```
{
  "_source": ["முழு பெயர்" ,"பங்கு","நாட்டு அணி","அறிமுகம்"],
  "size": 20,
  "query": {
    "match_phrase": {
      "முழு பெயர்" : "முத்தையா முரளிதரன்"
    }
  }
}
```
etc.......
