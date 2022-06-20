# aws-toolkit-etl

## Set up

1. Add AWS credentials to ~.aws/credentials (access key and secret access key) and ~.aws/config (region)
2. Create MySQL database (CloudFormation)
3. Create `.env` file and add credentials and parameters for Search query (see `.env_example` for format)
4. Run script that creates database tables: `database/create_table.py`
5. Run script that connects to the Twitter API and stores Tweet data: `main.py`
6. Configure BI dashboard (manual)

## File description

* `.env` is where the following information is expected: 
  * the credentials required to connect to the Twitter API (bearer token)
  * the credentials required to connect to the AWS RDS MySQL database
  * the parameters required to fetch data of interest from the Recent Search endpoint
* `database/create_table.py` creates initial DB tables to store Tweets and users data. This script must run once, after the creation of the MySQL DB and before the ETL process begins (`main.py`)
* `authentication.py` contains a class that handles authentication for the Twitter API
* `fetch_tweets.py` contains a class that connects to the Twitter API Recent Search endpoint and fetches data
* `main.py` is the main script that performs ETL steps: gets data from the Recent Search endpoint, parses the results, and sends them to the appropriate DB tables

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
