# Airline Passenger Satisfaction Dashboard Specification

## Objective
A high-level BI dashboard for executives to monitor passenger satisfaction trends and key service quality drivers.

## 1. Executive Summary (Page 1)
- **KPIs**:
  - **Overall Satisfaction Rate**: % of satisfied passengers (Neutral or Dissatisfied vs Satisfied).
  - **Average Satisfaction Score**: 1-5 scale across all service features.
  - **Average Delay**: Combined Departure and Arrival delay.
  - **Passenger Volume**: Total passengers analyzed.
- **Charts**:
  - **Donut Chart**: Satisfaction distribution.
  - **Bar Chart**: Satisfaction by Travel Class (Business vs Economy).
  - **Grouped Bar Chart**: Satisfaction by Type of Travel (Business vs Personal).
  - **Line Chart**: Satisfaction trends over Age groups.

## 2. Service Quality Drivers (Page 2)
- **Objective**: Identify which service areas need the most improvement.
- **KPIs**:
  - **Top 3 Drivers**: Top features from the Random Forest model.
  - **Bottom 3 Ratings**: Features with the lowest average rating from passengers.
- **Charts**:
  - **Horizontal Bar Chart**: Feature Importance (from the Random Forest model).
  - **Radar Chart**: Average ratings for key categories (Digital, On-board, Comfort).
  - **Heatmap**: Correlation between service features and overall satisfaction.

## 3. Operations & Delays (Page 3)
- **Objective**: Analyze the impact of delays on satisfaction.
- **KPIs**:
  - **% Delayed Flights**: Flights with >15 min delay.
  - **Satisfaction in Delayed vs On-time Flights**: Comparison of satisfaction rates.
- **Charts**:
  - **Scatter Plot**: Departure vs Arrival delay with Satisfaction as color coding.
  - **Bar Chart**: Satisfaction rate grouped by Delay Duration (0-15m, 15-60m, 60m+).
  - **Bubble Chart**: Flight distance vs Delay impact on satisfaction.

## 4. Design Guidelines
- **Color Palette**: 
  - Satisfied: #4CAF50 (Green)
  - Dissatisfied: #F44336 (Red)
  - Neutral: #FFC107 (Yellow)
- **Interactivity**: 
  - Slicers for: Travel Class, Customer Type, Gender, and Type of Travel.
  - Drill-down: Click on a service category to see detailed rating distributions.
