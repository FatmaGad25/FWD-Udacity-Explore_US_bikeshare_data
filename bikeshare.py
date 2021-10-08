import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ""
    month=""
    day=""
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    days=['all', 'sunday', 'monday', 'tuesday', 'wednesday','thursday','friday','saturday' ]
    while city not in CITY_DATA:
        city = input('Please choose the city you want to explore! Choose between (Chicago - New York city - Washington)\n').lower()

        if city not in CITY_DATA:

            print ("Sorry! We don't have this city's data, choose only between (Chicago - New York city - Washington)\nThe program will restart now")
            print('-'*40)

    while month not in months:

        month = input("Please choose the month you want to explore or choose all if you want all months' data\n").lower()

        if month not in months:
            print('Sorry! We only have the data of months from january to june.\nPlease choose an available month')
            print('-'*40)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in days:

        day = input("Please choose the day of the week you want to explore or choose all if you want all the days data\n").lower()
        if day not in days:
            ('You entered an unaccepted input, please choose again!\n')
            print('-'*40)

    print('-'*40)
    print("You chose to explore {} city's data on {} days of {} month".format(city, day, month))
    print('-'*40)

    return city, month, day

######################################################################################################################################################

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
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # df['day_of_week'] = df['Start Time'].dt.day_name()


    try: df['day_of_week'] = df['Start Time'].dt.weekday_name
    except: df['day_of_week'] = df['Start Time'].dt.day_name()
    else: df['day_of_week'] = df['Start Time'].dt.weekday
    
    
    
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = int(months.index(month)) + 1
    
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]
    
    return df

#######################################################################################################################################################

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("\nThe most common month of travel is {}".format(months[df['month'].mode()[0]-1]))

    # TO DO: display the most common day of week
    print("\nThe most common day of travel is {}".format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    print("\nThe most common hour of travel is {}".format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nThe most commonly used start station is: ",df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("\nThe most commonly used End station is: ",df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = "\nFrom " + df['Start Station'] + "\nTo " + df['End Station']
    print("\nThe most frequent combination of start station and end station trip is: ",df['Station Combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # travel_time= df['Trip Duration'].sum()
    # result = datetime.timedelta(seconds = df['Trip Duration'].sum())
    print("\nTotal Travel time =", datetime.timedelta(seconds = int(df['Trip Duration'].sum())))


    # TO DO: display mean travel time
    print("\nMean Travel time =", datetime.timedelta(seconds = df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    try:


        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        print('\nTypes and counts of available users types:\n',df['User Type'].value_counts())

        # TO DO: Display counts of gender
        print('\nCount of each gender:\n',df['Gender'].value_counts())


        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nThe earliest year of birth: \n',df['Birth Year'].min())
        print('\nThe most recent year of birth: \n',df['Birth Year'].max())
        print('\nThe most common year of birth: \n',df['Birth Year'].mode()[0])


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    except: 
        print("Sorry, the gender and ages of users aren't available for this city")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # print (df.head())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
