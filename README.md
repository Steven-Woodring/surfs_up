# Surfs Up with SQLAlchemy
### An analysis of weather data for Oahu, Hawaii to project the success of a surfboard and ice cream shop

## Overview
Starting a hypothetical business in Hawaii, Surf n’ Shake, that sells surfboards and ice cream to tourists and locals alike. After a positive meeting with a prospective investor, a concern arises. The investor had previously funded a surf shop without considering the weather, and rain negatively impacted the business so much that it eventually had to close. This analysis will look at weather on the island of Oahu to ensure that Surf n’ Shake has the opportunity to be successful.

## Results
### Temperature Trends
- The differences in temperature observations between June and December are relatively insignificant. Both the mean and median temperatures were only 4 degrees lower in December, and still in the 70s.
- While the minimum observed temperature in December was 8 degrees lower than June’s minimum temperature, the maximum temperatures are extremely similar. For December’s hottest days, tourists and locals can expect the temperature to be only 2 degrees cooler than June’s hottest days.
- In our dataset, there are 1700 temperature observations for June and 1517 for December, spanning multiple years. This is representative of nearly 57 and 49 full months of observations, respectively. This is a valid sample size for statistical analysis, meaning the surfboard and ice cream shop’s potential investors can trust the results.

## Summary
Overall, the temperature observations in both June and December show mostly favorable weather, and thus do not present an obstacle for the Surf n’ Shake venture. Both the mean and median temperatures in June and December are above 70 degrees, meaning there should be plenty of demand for surfboard and ice cream no matter the season.

### Days Below 70 Degrees
Demand for surfboards and ice cream will most likely decrease on days where the temperature dips under 70 degrees. The following queries, after being placed in a DataFrame and analyzed, found that 0.83% and 27.65% of days had average observed temperatures (between all the weather stations) of below 70 degrees in June and December, respectively.

<img width="602" alt="Screen Shot 2022-02-21 at 12 00 53 AM" src="https://user-images.githubusercontent.com/95303422/154892317-ed0db7c3-d823-4af3-b950-6625c9dec3ce.png">
<img width="602" alt="Screen Shot 2022-02-21 at 12 01 02 AM" src="https://user-images.githubusercontent.com/95303422/154892323-03184b42-accb-4d19-9be6-55bbbcb38fc9.png">
