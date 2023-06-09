#  __Project__ 🚧
For this case study, we suggest that you put yourselves in our shoes, and run an analysis we made back in 2017 🔮 🪄

When using Getaround, drivers book cars for a specific time period, from an hour to a few days long. They are supposed to bring back the car on time, but it happens from time to time that drivers are late for the checkout.

Late returns at checkout can generate high friction for the next driver if the car was supposed to be rented again on the same day : Customer service often reports users unsatisfied because they had to wait for the car to come back from the previous rental or users that even had to cancel their rental because the car wasn’t returned on time.

----------------

# __Goals__ 🎯

In order to mitigate those issues we’ve decided to implement a minimum delay between two rentals. A car won’t be displayed in the search results if the requested checkin or checkout times are too close from an already booked rental.

It solves the late checkout issue but also potentially hurts Getaround/owners revenues: we need to find the right trade off.

Our Product Manager still needs to decide:

* threshold: how long should the minimum delay be?
* scope: should we enable the feature for all cars?, only Connect cars?

In order to help them make the right decision, they are asking you for some data insights. Here are the first analyses they could think of, to kickstart the discussion. Don’t hesitate to perform additional analysis that you find relevant.

* Which share of our owner’s revenue would potentially be affected by the feature How many rentals would be affected by the feature depending on the threshold and scope we choose?
* How often are drivers late for the next check-in? How does it impact the next driver?
* How many problematic cases will it solve depending on the chosen threshold and scope?

----------------

# __Deliverables__ 🗃

* Two notebooks one for the Data Analysis and the second for the Machine Learning
* A dashboard in production accessible via the following link: https://dashboard-getaround.herokuapp.com/
* A docker file for the dashboard
* An documented online API on Heroku server containing one /predict endpoint accessible via the following link: https://fastapi-getaround.herokuapp.com/docs
* A docker file for the online API
* A notebook to test the API
* The machine learning models in .joblib
* A notebook to test the API
----------------

# __Project Video Presentation__ 📷

On Vidyard: https://share.vidyard.com/watch/J8rgzFHRQVgkMLxUnbTyhc?
