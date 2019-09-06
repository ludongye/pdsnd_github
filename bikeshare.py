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
    city = input('Which city do you want to analyze? Chicago? New York city? Washington? Enter the name of the city\n')
    while city.lower() not in CITY_DATA.keys():
        city = input('Plese input a valid city name as shown in the question\n')
    print('City chosen: {}'.format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month do you want to analyze? january? february? march? april? may? june? or all months? if all months, enter all\n')
    while month.lower() not in ['all','january','february','march','april','may','june']:
        month = input('Please enter a valid month\n')
    print('Month chosen: {}'.format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ('which day? all? monday? tuesday? wednesday? thursday? friday? saturday? sunday?\n')
    while day.lower() not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day = input ('Please enter valid day\n')
    print('Day chosen: {}'.format(day))
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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january','february','march','april','may','june']
    popular_month = months[df['month'].mode()[0]-1].title()
    print('The most common month is {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of weeks is {}'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is {}'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    popular_combo_station = df['combination'].mode()[0]
    print('The most frequent combination is {}'.format(popular_combo_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: ', tot_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Here are the counts of user types: \n',user_types)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('Here are the counts of gender: \n', gender_counts)
    except:
        print('Sorry. No data on gender.')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print ('The earliest year of birth is {}, the most recent year of birth is {}, and the most common year of birth is {}'.format(earliest_year, most_recent_year, most_common_year))
    except:
        print ('Sorry. No data on birth year.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
        """Ask user if he/she wants to view raw data."""
    ans = input('Would you like to see some raw data? Please type "Yes" or "No"\n')
    i = 0
    while True:
        if ans.title() not in ['Yes','No']:
            ans = input('Sorry, please type "Yes" or "No"\n')
        elif ans.title() == 'Yes':
            print(df.iloc[i:i+5,0:9])
            i += 5
            ans = input('Would you like to see some raw data? Please type "Yes" or "No"\n')
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
