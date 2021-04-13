# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import os
#retval = os.getcwd()
#print (retval)

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
	
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ")
        city = city.lower()
        city_list = ['chicago','new york city','washington']
        if city not in city_list:
            print()
            print("Invalid entry. Please select 'Chicago', 'New York City', or 'Washington'")
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Can you provide month (all, january, february, ..., june)? ")
        month = month.lower()
        month_list = ['all','january','february','march','april','may','june']
        if month not in month_list:
            print()
            print("Invalid entry. Please select 'all', 'january', 'feburary', 'march', 'april', 'may', or 'june'?")
        else:
            break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Can you provide day of week (all, monday, tuesday, ... sunday)? ")
        day = day.lower()
        day_list = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        if day not in day_list:
            print()
            print("Invalid entry. Please select 'all', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Satruday', 'Sunday'")
        else:
            break
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour     

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Hour:', popular_month)

    # TO DO: display the most common day of week
    popular_dayofweek = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', popular_dayofweek) 

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', Total_travel_time)

    # TO DO: display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('Average duration:', Mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    start_time = time.time()

    # TO DO: Display counts of user types    
    user_types = pd.concat([df['User Type'].value_counts(),
                             df['User Type'].value_counts(normalize=True).mul(100)], axis=1, keys=('counts','percentage'))
    print(user_types)
    print()

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = pd.concat([df['Gender'].value_counts(),
                        df['Gender'].value_counts(normalize=True).mul(100)], axis=1, keys=('counts','percentage'))
        print(gender)
        print()
    else:
        print('Gender column does not exist, no calculation will be performed.')

    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:    
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])
        print("The earliest year of birth is:", earliest)
        print("The most recent year of birth is:", most_recent)
        print("The most common year of birth is:", most_common)
    else:
        print('Birth Year column does exist, no calculation will be performed.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def rawdata(df):
    i = 0
    user_input = input('Would you like to see the raw data? Enter Yes or No. ')
    user_input = user_input.lower()
    while user_input == 'yes' and i + 5 < df.shape[0]:
        print(df.iloc[i:i+5])
        i += 5
        user_input = input('Would you like to see more data? Enter Yes or No. ')
        user_input = user_input.lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you and have a good day!')
            break


if __name__ == "__main__":
	main()
    