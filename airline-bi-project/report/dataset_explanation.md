# Detailed Dataset Explanation: Airline Passenger Satisfaction

## 1. Overview
The dataset contains **129,880 rows** and **24 columns**, representing a survey of airline passengers' satisfaction with various aspects of their flight experience. Each row corresponds to a unique passenger and includes their demographics, flight details, and ratings for 14 different service categories.

## 2. Demographic Information
- **ID**: A unique identifier for each passenger.
- **Gender**: Categorical (Female, Male). The dataset is fairly balanced with 65,899 females.
- **Age**: Numerical (7 to 85 years). The average passenger age is approximately **39 years**.
- **Customer Type**: Categorical (Returning, First-time). About **82%** (106,100) are returning customers.

## 3. Flight Details
- **Type of Travel**: Categorical (Business, Personal). Business travel accounts for ~69% of the dataset.
- **Class**: Categorical (Business, Eco, Eco Plus). Business class is the most common (62,160 passengers).
- **Flight Distance**: Numerical (31 to 4,983 miles). The average distance is **1,190 miles**.
- **Departure Delay**: Numerical (0 to 1,592 minutes). Average delay is ~14.7 minutes.
- **Arrival Delay**: Numerical (0 to 1,584 minutes). Average delay is ~15.1 minutes.
  - *Note*: This column has **393 missing values**, which were handled using median imputation during preprocessing.

## 4. Service Ratings (Ordinal 0-5)
Passengers rated 14 services on a scale from **1 (Lowest)** to **5 (Highest)**. A score of **0** indicates "Not Applicable".

### Digital & Booking
- **In-flight Wifi Service**: Average 2.73.
- **Ease of Online Booking**: Average 2.76.
- **Online Boarding**: Average 3.25.

### On-board Experience
- **Seat Comfort**: Average 3.44.
- **Leg Room Service**: Average 3.35.
- **Food and Drink**: Average 3.20.
- **In-flight Entertainment**: Average 3.36.
- **On-board Service**: Average 3.38.

### Logistics & Airport
- **Departure/Arrival Time Convenience**: Average 3.06.
- **Gate Location**: Average 2.98.
- **Baggage Handling**: Average 3.63.
- **Check-in Service**: Average 3.31.
- **In-flight Service**: Average 3.64.
- **Cleanliness**: Average 3.29.

## 5. Target Variable
- **Satisfaction**: Categorical (Satisfied, Neutral or Dissatisfied).
  - **Neutral or Dissatisfied**: 73,452 (56.6%)
  - **Satisfied**: 56,428 (43.4%)
  - *Interpretation*: The dataset is slightly imbalanced towards dissatisfaction, providing a rich set of examples for identifying pain points.
