import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 
              'new york city': 'new_york_city.csv', 
              'washington': 'washington.csv' } 

#Let's grab the cities, months, and days.
the_cities = ['chicago', 'new york city', 'washington'] 
the_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
the_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

#Create get_filters function here
def get_filters(): 
    """ 
    Asks user to specify a city, month, and day to analyze. 
    Returns: 
        (str) city - name of the city to analyze 
        (str) month - name of the month to filter by, or "all" to apply no month filter 
        (str) day - name of the day of week to filter by, or "all" to apply no day filter 
    """ 
    print('Hello! Let\'s explore some US bikeshare data!') 
#Grabbing the user input for the city to get data from
    print('Alright then. Let\'s get this show on the road.\nFirst, tell us what city you want to see data from. \nChoose from either: Chicago, New York City, or Washington.') 
    def name_of_city(): 
        #Get the name of the city
        city = str(input('What\'s the name of the city that has data you want to explore? :')).lower()
        if city not in the_cities: 
            print('Sorry chief.....You can only select Chicago, New York City, or Washington. Try again...') 
            city = name_of_city() 
        return city 
    city = name_of_city() 
#Grabbing the user input for the month they want to see data on 
    print('Select a month january, february, march, april, may, june or all ?') 
    def name_of_month(): 
        #Get the name of the month
        month = str(input('Now that we have the month, which day are your trying to retreive data from? :')).lower()
        if month not in the_months: 
            print('Please try again.....Tell us the month you\'d like to retrieve data from :') 
            month = name_of_month() 
        return month 
    month = name_of_month()
#Grabbing the user input for the day they want to see data on 
    print('Select a day monday, tuesday, wednesday, thursday, friday, saturday, sunday or all ?') 
    def name_of_day(): 
        #Get the name of the day
        day = str(input('Which day are your trying to retreive data from? :')).lower() 
        if day not in the_days: 
            print('Please try again.....Tell us the day you\'d like to retrieve data from :') 
            day = name_of_day() 
        return day 
    day = name_of_day()      
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
    #This is where we put the data into the dataframe
    df = pd.read_csv(CITY_DATA[city])

    #Converting the start time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Taking the month, day, and hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #Filter by the month and then by the day if it's needed
    if month != 'all':
        month = the_months.index(month)
        df = df.loc[df['month'] == month]

    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df

#Getting the time stats here
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Showing the most common month
    most_common_month = df['month'].mode()[0]
    print("Judging from the filtered data, the most common month is: " + the_months[most_common_month].title())

    #Showing the most common day of week
    most_common_weekday = df['day_of_week'].mode()[0]
    print("Judging from the filtered data, the most common day of the week is: " + most_common_weekday)

    #Showing the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print("Judging from the filtered data, the most common starting hour is: " + str(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Getting the station stats here
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Showing the most popular start station
    popular_start_station = df['Start Station'].mode()[0]
    print("According to the filtered data, the most popular start station is: " + popular_start_station)

    #Showing the most popular end station
    popular_end_station = df['End Station'].mode()[0]
    print("According to the filtered data, the most popular end station is: " + popular_end_station)

    #Showing the most popular frequented combo of starting and ending stations
    popular_frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("According to the filtered data, the most popular frequent combination of starting and ending stations is : " + str(popular_frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Getting the trip duration stats here
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    #Updating the Calculations of the Trip Duration script
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Showing total travel time
    total_travel = df['Trip Duration'].sum()
    print("According to the filtered data, the total travel time is: " + str(total_travel))

    #Showing mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("According to the filtered data, the mean travel time is: " + str(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Showing counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types according to the fitered data is: \n" + str(user_types))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        #Showing counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user genders according to the fitered data is: \n" + str(gender))

        #Showing the earliest, most recent, and most common YOB (year of birth)
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('The earliest birth according to the fitered data: {}\n'.format(earliest))
        print('The most recent birth according to the fitered data: {}\n'.format(most_recent))
        print('The most common birth according to the fitered data: {}\n'.format(most_common) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#Showing the raw data
def show_raw_data(df):
    """Displays raw data on bikeshare users."""
    print(df.head())
    next = 0
    while True:
        get_raw_data = input('\nHello, would you like to see the first five rows of raw data? Type yes or no.\n')
        if get_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            get_raw_data = input('\nHello, would you like to see the first five rows of raw data? Type yes or no.\n')
            if get_raw_data.lower() != 'yes':
                break
            show_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()