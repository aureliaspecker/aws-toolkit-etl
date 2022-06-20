# aws-toolkit-etl

## Set up

1. Create MySQL database (CloudFormation)
2. Create `.env` file and add credentials and parameters for Search query (see `.env_example` for format)
3. Run script that creates database tables: `database/create_table.py`
4. Run script that connects to the Twitter API and stores Tweet data: `main.py`
5. Configure BI dashboard (manual)

## Note

This toolkit in intended as an example framework that quickly fetches, parses, and analyzes Twitter data. 

The following [data objects](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction) are extracted and persisted:

* Tweets (including hastags, cashtags, annotations, mentions, urls)
* Users

The following data objects will not be persisted:

* Media
* Polls
* Places
* Spaces
* Lists
