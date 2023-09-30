# los-angeles-crime-data
###Import crime csv data into Elasticsearch using Logstash

This example ingests a CSV file of crimes in Los Angelas into Elasticsearch using Logstash

### Version

Example has been tested on the following version

- Elasticsearch 6.2.3
- Logstash 6.2.3

### Using

Edit the "crime-logstash.conf" file so that a full path us used to reference the data and template

A small example file is included. The full file can be downloaded at"
https://data.lacity.org/A-Safe-City/Crime-Data-from-2010-to-Present/y8tr-7khq

Make sure Elasticsearch is running on localhost:9200

From the Logstash directory, start logstash and reference the "crime-logstash.conf"

```shell
{logstash directory}/bin/logstash -f {path to conf}/crime-logstash.conf    

``` 


