# FireWatch - HackTX 2019

![Firewatch Screenshot](https://raw.githubusercontent.com/SyedAbutalib/FireWatch/master/Firewatch-screenshot.png)

## Inspiration
In a disaster, the most important piece of information that doesn't reach the masses is how little time they have to get out safely. We are unable to pool in information from the affected communities and this often underestimates the gravity of the situation. We wanted to build a tool to support the most vulnerable, connect affected parts and increase the accessibility of emergency services to areas at risk.

## What it does
Firewatch picks up real-time information about wildfires from tweets to track the movement of the blaze. We then run a combination of predictive models to elucidate the areas that are at risk from the fire and what time they are most likely to run into grave danger.

## How we built it
We developed a tool to pull tweets in real time from Twitter that were geo-tagged and relevant to the wildfire we're tracking. Using this, we triangulate the location of the fire at a given point of time and chart a path of the fire. Using our time-series and random walk models, we then find the areas that are mostly likely to be caught up in the blaze.

## Challenges we ran into
The direction of the blaze tends to be affected by many factors such as wind velocity, presence of environmental factors like coastline/forests/residential areas, etc. Hence it's very difficult to isolate possible regions that could be affected. Additionally, a lot of tweets such as those from news agencies and/or emergency services are broadcast from the headquarters, hence using them as base-points for ground zero is unreliable.

## Accomplishments that we're proud of
We were able to find tweets in a 50 mile radius of disaster struck areas and find the most relevant, useful and geo-tagged tweets from the same set. Additionally, we generated a heat map of at-risk locations apart from the specific locations that are likely to be hit.

## What we learned
We learned the importance of community efforts in tracking disasters, because the greater number of tweets we could find, the more accurate our prediction was. We were also exposed to cleaning up unstructured data, and how social media data not only connects us as well as protects us.

## What's next for Firewatch
We will use our website to help evacuated people find housing through partnership with Airbnb and other housing platforms. Second, we will provide the Fire Department with information. Lastly, we will connect donation services for victims and have partnership with UBER and other ride-share platforms to help in evacuation efforts.

### How to install/run

#### Linux/Mac
export FLASK_APP=flaskr

export FLASK_ENV=development

flask run

#### Windows
set FLASK_APP=flaskr

set FLASK_ENV=development

flask run

#### Site
Then go to http://127.0.0.1:5000
