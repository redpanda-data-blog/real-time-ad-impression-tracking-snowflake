# real-time-ad-impression-tracking-snowflake
Real-time ad impression tracking with Redpanda and Snowflake

To test the application, follow the below steps:

### Step 1: Setup Redpanda self-managed cluster
Download docker-compose.yml using [this link](https://docs.redpanda.com/current/get-started/_attachments/single-broker/docker-compose.yml) to set up a single-node Redpanda cluster. 

To start the containers, execute the below command from your terminal.
```bash
docker compose up -d
```

This will start your Redpanda cluster, and you can browse the console using [this link](https://localhost:8080/overview)


### Step 2: Setup Redpanda Connect, Snowflake, and the Snowflake Streamlit App
Perform the required Redpanda Connect and Snwflake configurations as mentioned in the tutorial.

### Step 3: Start receiving the data from the HTTP server using Redpanda Connect
In your terminal, open the container's bash shell by executing the below command:
```bat
docker exec -it redpanda-0 /bin/bash
```

Start Redpanda Connect in stream mode using the below command
```bash
cd /tmp/campaign_analytics
rpk connect streams http_sf_stream.yaml
```

### Step 4: Start the producer script to post messages to the HTTP server
Open another terminal window and open the container's bash shell by executing the below command: 

```bash
docker exec -it redpanda-0 /bin/bash
```

Execute the producer script that POSTs ad impressions and clicks for 5 different ads every 5 seconds. 
The script will stop after sending a total of 500 messages.
```bash
cd /tmp/campaign_analytics
sh produce_messages.sh
```
>You can edit this script to add more test records or just copy these `curl` commands to post individual messages as per your requirements.

### Step 5: View real-time dashboards in Snowflake
Open the Snowflake Streamlit dashboard and view the dashboards in real-time. You can refresh it to see the updates as they change every 5 seconds.
Once the producer script is completed, you will see the final visualizations in the dashboard.


