{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello! Let's explore some US bikeshare data!\n",
      "Alright then. Let's get this show on the road.\n",
      "First, tell us what city you want to see data from. \n",
      "Choose from either: Chicago, New York City, or Washington.\n",
      "What's the name of the city that has data you want to explore? :Washington\n",
      "Select a month january, february, march, april, may, june or all ?\n",
      "Now that we have the month, which day are your trying to retreive data from? :march\n",
      "Select a day monday, tuesday, wednesday, thursday, friday, saturday, sunday or all ?\n",
      "Which day are your trying to retreive data from? :friday\n",
      "----------------------------------------\n",
      "\n",
      "Calculating The Most Frequent Times of Travel...\n",
      "\n",
      "Judging from the filtered data, the most common month is: March\n",
      "Judging from the filtered data, the most common day of the week is: Friday\n",
      "Judging from the filtered data, the most common starting hour is: 17\n",
      "\n",
      "This took 0.004986286163330078 seconds.\n",
      "----------------------------------------\n",
      "\n",
      "Calculating The Most Popular Stations and Trip...\n",
      "\n",
      "According to the filtered data, the most popular start station is: Columbus Circle / Union Station\n",
      "According to the filtered data, the most popular end station is: Columbus Circle / Union Station\n",
      "According to the filtered data, the most popular frequent combination of starting and ending stations is : ['8th & F St NE', 'Columbus Circle / Union Station']\n",
      "\n",
      "This took 0.465162992477417 seconds.\n",
      "----------------------------------------\n",
      "\n",
      "Calculating Trip Duration...\n",
      "\n",
      "According to the filtered data, the total travel time is: 5268936.102\n",
      "According to the filtered data, the mean travel time is: 944.0845909335253\n",
      "\n",
      "This took 0.0009975433349609375 seconds.\n",
      "----------------------------------------\n",
      "\n",
      "Calculating User Stats...\n",
      "\n",
      "The count of user types according to the fitered data is: \n",
      "Subscriber    4748\n",
      "Customer       833\n",
      "Name: User Type, dtype: int64\n",
      "\n",
      "This took 0.007976055145263672 seconds.\n",
      "----------------------------------------\n",
      "\n",
      "Hello, would you like to see the first five rows of raw data? Type yes or no.\n",
      "yes\n",
      "     Unnamed: 0          Start Time             End Time  Trip Duration  \\\n",
      "48       368705 2017-02-24 19:02:00  2017-02-24 19:09:00        447.748   \n",
      "72       290641 2017-02-17 15:10:00  2017-02-17 15:15:00        324.328   \n",
      "76       241950 2017-02-10 07:03:00  2017-02-10 07:09:00        343.030   \n",
      "163      364761 2017-02-24 16:00:00  2017-02-24 16:23:00       1373.852   \n",
      "267      363928 2017-02-24 15:09:00  2017-02-24 15:13:00        278.058   \n",
      "\n",
      "                   Start Station  \\\n",
      "48                21st & M St NW   \n",
      "72                1st & N St  SE   \n",
      "76   Adams Mill & Columbia Rd NW   \n",
      "163               15th & K St NW   \n",
      "267   17th & Rhode Island Ave NW   \n",
      "\n",
      "                                           End Station   User Type  month  \\\n",
      "48                      C & O Canal & Wisconsin Ave NW  Subscriber      2   \n",
      "72   Eastern Market Metro / Pennsylvania Ave & 7th ...  Subscriber      2   \n",
      "76                                 14th & Irving St NW  Subscriber      2   \n",
      "163                John McCormack Dr & Michigan Ave NE  Subscriber      2   \n",
      "267               Massachusetts Ave & Dupont Circle NW  Subscriber      2   \n",
      "\n",
      "    day_of_week  hour  \n",
      "48       Friday    19  \n",
      "72       Friday    15  \n",
      "76       Friday     7  \n",
      "163      Friday    16  \n",
      "267      Friday    15  \n",
      "\n",
      "Hello, would you like to see the first five rows of raw data? Type yes or no.\n",
      "yes\n",
      "     Unnamed: 0          Start Time             End Time  Trip Duration  \\\n",
      "325      288547 2017-02-17 09:04:00  2017-02-17 09:25:00       1270.063   \n",
      "341      369827 2017-02-24 21:21:00  2017-02-24 21:41:00       1231.747   \n",
      "388      196534 2017-02-03 19:14:00  2017-02-03 19:18:00        283.917   \n",
      "485      370206 2017-02-24 22:42:00  2017-02-24 22:52:00        614.757   \n",
      "551      288235 2017-02-17 08:40:00  2017-02-17 08:54:00        798.217   \n",
      "\n",
      "                   Start Station                 End Station   User Type  \\\n",
      "325                3rd & G St SE   New York Ave & 15th St NW    Customer   \n",
      "341               14th & G St NW  North Capitol St & F St NW    Customer   \n",
      "388   Calvert St & Woodley Pl NW    18th St & Wyoming Ave NW  Subscriber   \n",
      "485                7th & T St NW               8th & H St NW  Subscriber   \n",
      "551  Adams Mill & Columbia Rd NW              21st & I St NW  Subscriber   \n",
      "\n",
      "     month day_of_week  hour  \n",
      "325      2      Friday     9  \n",
      "341      2      Friday    21  \n",
      "388      2      Friday    19  \n",
      "485      2      Friday    22  \n",
      "551      2      Friday     8  \n",
      "\n",
      "Hello, would you like to see the first five rows of raw data? Type yes or no.\n",
      "yes\n",
      "     Unnamed: 0          Start Time             End Time  Trip Duration  \\\n",
      "753      364131 2017-02-24 15:21:00  2017-02-24 15:50:00       1771.423   \n",
      "786      360535 2017-02-24 09:48:00  2017-02-24 10:12:00       1433.972   \n",
      "833      287741 2017-02-17 08:10:00  2017-02-17 08:14:00        236.957   \n",
      "917      191504 2017-02-03 07:58:00  2017-02-03 08:08:00        617.483   \n",
      "938      361899 2017-02-24 12:26:00  2017-02-24 12:53:00       1603.707   \n",
      "\n",
      "                                         Start Station  \\\n",
      "753        Henry Bacon Dr & Lincoln Memorial Circle NW   \n",
      "786  Smithsonian-National Mall / Jefferson Dr & 12t...   \n",
      "833                             14th St & Spring Rd NW   \n",
      "917                     15th St & Massachusetts Ave SE   \n",
      "938                                River Rd & Landy Ln   \n",
      "\n",
      "                                           End Station   User Type  month  \\\n",
      "753              Iwo Jima Memorial/N Meade & 14th St N    Customer      2   \n",
      "786  Smithsonian-National Mall / Jefferson Dr & 12t...    Customer      2   \n",
      "833                                14th & Irving St NW  Subscriber      2   \n",
      "917                                 3rd & Tingey St SE  Subscriber      2   \n",
      "938                                River Rd & Landy Ln  Subscriber      2   \n",
      "\n",
      "    day_of_week  hour  \n",
      "753      Friday    15  \n",
      "786      Friday     9  \n",
      "833      Friday     8  \n",
      "917      Friday     7  \n",
      "938      Friday    12  \n",
      "\n",
      "Hello, would you like to see the first five rows of raw data? Type yes or no.\n",
      "yes\n",
      "      Unnamed: 0          Start Time             End Time  Trip Duration  \\\n",
      "956       193715 2017-02-03 13:01:00  2017-02-03 13:07:00        379.955   \n",
      "1010      290119 2017-02-17 13:50:00  2017-02-17 14:01:00        628.597   \n",
      "1072      245402 2017-02-10 16:35:00  2017-02-10 16:39:00        237.095   \n",
      "1082      293530 2017-02-17 19:47:00  2017-02-17 19:55:00        467.797   \n",
      "1140      289919 2017-02-17 13:18:00  2017-02-17 13:32:00        818.195   \n",
      "\n",
      "                                          Start Station  \\\n",
      "956                                14th & Belmont St NW   \n",
      "1010                             Maryland Ave & E St NE   \n",
      "1072                         Carroll & Westmoreland Ave   \n",
      "1082                                     20th & E St NW   \n",
      "1140  Smithsonian-National Mall / Jefferson Dr & 12t...   \n",
      "\n",
      "                       End Station   User Type  month day_of_week  hour  \n",
      "956                 15th & P St NW  Subscriber      2      Friday    13  \n",
      "1010        Oklahoma Ave & D St NE  Subscriber      2      Friday    13  \n",
      "1072      Philadelphia & Maple Ave  Subscriber      2      Friday    16  \n",
      "1082     14th St & New York Ave NW  Subscriber      2      Friday    19  \n",
      "1140  7th & R St NW / Shaw Library  Subscriber      2      Friday    13  \n",
      "\n",
      "Hello, would you like to see the first five rows of raw data? Type yes or no.\n",
      "no\n",
      "\n",
      "Would you like to restart? Enter yes or no.\n",
      "yes\n",
      "Hello! Let's explore some US bikeshare data!\n",
      "Alright then. Let's get this show on the road.\n",
      "First, tell us what city you want to see data from. \n",
      "Choose from either: Chicago, New York City, or Washington.\n",
      "What's the name of the city that has data you want to explore? :Chicago\n",
      "Select a month january, february, march, april, may, june or all ?\n",
      "Now that we have the month, which day are your trying to retreive data from? :april\n",
      "Select a day monday, tuesday, wednesday, thursday, friday, saturday, sunday or all ?\n",
      "Which day are your trying to retreive data from? :friday\n",
      "----------------------------------------\n",
      "\n",
      "Calculating The Most Frequent Times of Travel...\n",
      "\n",
      "Judging from the filtered data, the most common month is: April\n",
      "Judging from the filtered data, the most common day of the week is: Friday\n",
      "Judging from the filtered data, the most common starting hour is: 17\n",
      "\n",
      "This took 0.005983591079711914 seconds.\n",
      "----------------------------------------\n",
      "\n",
      "Calculating The Most Popular Stations and Trip...\n",
      "\n",
      "According to the filtered data, the most popular start station is: Clinton St & Washington Blvd\n",
      "According to the filtered data, the most popular end station is: Clinton St & Washington Blvd\n",
      "According to the filtered data, the most popular frequent combination of starting and ending stations is : ['Streeter Dr & Grand Ave', 'Streeter Dr & Grand Ave']\n",
      "\n",
      "This took 0.0109710693359375 seconds.\n",
      "----------------------------------------\n",
      "\n",
      "Calculating Trip Duration...\n",
      "\n",
      "According to the filtered data, the total travel time is: 4344099\n",
      "According to the filtered data, the mean travel time is: 747.3075864441769\n",
      "\n",
      "This took 0.001992940902709961 seconds.\n",
      "----------------------------------------\n",
      "\n",
      "Calculating User Stats...\n",
      "\n",
      "The count of user types according to the fitered data is: \n",
      "Subscriber    5243\n",
      "Customer       570\n",
      "Name: User Type, dtype: int64\n",
      "\n",
      "This took 0.003988981246948242 seconds.\n",
      "----------------------------------------\n"
     ]
    }
   ],
   "source": [
    "CITY_DATA = { 'chicago': 'chicago.csv', \n",
    "              'new york city': 'new_york_city.csv', \n",
    "              'washington': 'washington.csv' } \n",
    "\n",
    "#Let's grab the cities, months, and days.\n",
    "the_cities = ['chicago', 'new york city', 'washington'] \n",
    "the_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']\n",
    "the_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']\n",
    "\n",
    "def get_filters(): \n",
    "    \"\"\" \n",
    "    Asks user to specify a city, month, and day to analyze. \n",
    "    Returns: \n",
    "        (str) city - name of the city to analyze \n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter \n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter \n",
    "    \"\"\" \n",
    "    print('Hello! Let\\'s explore some US bikeshare data!') \n",
    "#Grabbing the user input for the city to get data from\n",
    "    print('Alright then. Let\\'s get this show on the road.\\nFirst, tell us what city you want to see data from. \\nChoose from either: Chicago, New York City, or Washington.') \n",
    "    def name_of_city(): \n",
    "        #Get the name of the city\n",
    "        city = str(input('What\\'s the name of the city that has data you want to explore? :')).lower()\n",
    "        if city not in the_cities: \n",
    "            print('Sorry chief.....You can only select Chicago, New York City, or Washington. Try again...') \n",
    "            city = name_of_city() \n",
    "        return city \n",
    "    city = name_of_city() \n",
    "#Grabbing the user input for the month they want to see data on \n",
    "    print('Select a month january, february, march, april, may, june or all ?') \n",
    "    def name_of_month(): \n",
    "        #Get the name of the month\n",
    "        month = str(input('Now that we have the month, which day are your trying to retreive data from? :')).lower()\n",
    "        if month not in the_months: \n",
    "            print('Please try again.....Tell us the month you\\'d like to retrieve data from :') \n",
    "            month = name_of_month() \n",
    "        return month \n",
    "    month = name_of_month()\n",
    "#Grabbing the user input for the day they want to see data on \n",
    "    print('Select a day monday, tuesday, wednesday, thursday, friday, saturday, sunday or all ?') \n",
    "    def name_of_day(): \n",
    "        #Get the name of the day\n",
    "        day = str(input('Which day are your trying to retreive data from? :')).lower() \n",
    "        if day not in the_days: \n",
    "            print('Please try again.....Tell us the day you\\'d like to retrieve data from :') \n",
    "            day = name_of_day() \n",
    "        return day \n",
    "    day = name_of_day()      \n",
    "    print('-'*40) \n",
    "    return city, month, day\n",
    "\n",
    "def load_data(city, month, day):\n",
    "    \"\"\"\n",
    "    Loads data for the specified city and filters by month and day if applicable.\n",
    "    Args:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    Returns:\n",
    "        df - Pandas DataFrame containing city data filtered by month and day\n",
    "    \"\"\"\n",
    "    #This is where we put the data into the dataframe\n",
    "    df = pd.read_csv(CITY_DATA[city])\n",
    "\n",
    "    #Converting the start time to datetime\n",
    "    df['Start Time'] = pd.to_datetime(df['Start Time'])\n",
    "\n",
    "    #Taking the month, day, and hour\n",
    "    df['month'] = df['Start Time'].dt.month\n",
    "    df['day_of_week'] = df['Start Time'].dt.day_name()\n",
    "    df['hour'] = df['Start Time'].dt.hour\n",
    "\n",
    "    #Filter by the month and then by the day if it's needed\n",
    "    if month != 'all':\n",
    "        month = the_months.index(month)\n",
    "        df = df.loc[df['month'] == month]\n",
    "\n",
    "    if day != 'all':\n",
    "        df = df.loc[df['day_of_week'] == day.title()]\n",
    "\n",
    "    return df\n",
    "\n",
    "def time_stats(df):\n",
    "    \"\"\"Displays statistics on the most frequent times of travel.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Frequent Times of Travel...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    #Showing the most common month\n",
    "    most_common_month = df['month'].mode()[0]\n",
    "    print(\"Judging from the filtered data, the most common month is: \" + the_months[most_common_month].title())\n",
    "\n",
    "    #Showing the most common day of week\n",
    "    most_common_weekday = df['day_of_week'].mode()[0]\n",
    "    print(\"Judging from the filtered data, the most common day of the week is: \" + most_common_weekday)\n",
    "\n",
    "    #Showing the most common start hour\n",
    "    most_common_start_hour = df['hour'].mode()[0]\n",
    "    print(\"Judging from the filtered data, the most common starting hour is: \" + str(most_common_start_hour))\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "def station_stats(df):\n",
    "    \"\"\"Displays statistics on the most popular stations and trip.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Popular Stations and Trip...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    #Showing the most popular start station\n",
    "    popular_start_station = df['Start Station'].mode()[0]\n",
    "    print(\"According to the filtered data, the most popular start station is: \" + popular_start_station)\n",
    "\n",
    "    #Showing the most popular end station\n",
    "    popular_end_station = df['End Station'].mode()[0]\n",
    "    print(\"According to the filtered data, the most popular end station is: \" + popular_end_station)\n",
    "\n",
    "    #Showing the most popular frequented combo of starting and ending stations\n",
    "    popular_frequent_combination = (df['Start Station'] + \"||\" + df['End Station']).mode()[0]\n",
    "    print(\"According to the filtered data, the most popular frequent combination of starting and ending stations is : \" + str(popular_frequent_combination.split(\"||\")))\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "def trip_duration_stats(df):\n",
    "    \"\"\"Displays statistics on the total and average trip duration.\"\"\"\n",
    "\n",
    "    print('\\nCalculating Trip Duration...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    #Showing total travel time\n",
    "    total_travel = df['Trip Duration'].sum()\n",
    "    print(\"According to the filtered data, the total travel time is: \" + str(total_travel))\n",
    "\n",
    "    #Showing mean travel time\n",
    "    mean_travel = df['Trip Duration'].mean()\n",
    "    print(\"According to the filtered data, the mean travel time is: \" + str(mean_travel))\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def user_stats(df, city):\n",
    "    \"\"\"Displays statistics on bikeshare users.\"\"\"\n",
    "\n",
    "    print('\\nCalculating User Stats...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    #Showing counts of user types\n",
    "    user_types = df['User Type'].value_counts()\n",
    "    print(\"The count of user types according to the fitered data is: \\n\" + str(user_types))\n",
    "\n",
    "    if city == 'chicago.csv' or city == 'new_york_city.csv':\n",
    "        #Showing counts of gender\n",
    "        gender = df['Gender'].value_counts()\n",
    "        print(\"The count of user genders according to the fitered data is: \\n\" + str(gender))\n",
    "\n",
    "        #Showing the earliest, most recent, and most common YOB (year of birth)\n",
    "        earliest = df['Birth Year'].min()\n",
    "        most_recent = df['Birth Year'].max()\n",
    "        most_common = df['Birth Year'].mode()[0]\n",
    "        print('The earliest birth according to the fitered data: {}\\n'.format(earliest))\n",
    "        print('The most recent birth according to the fitered data: {}\\n'.format(most_recent))\n",
    "        print('The most common birth according to the fitered data: {}\\n'.format(most_common) )\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def show_raw_data(df):\n",
    "    \"\"\"Displays raw data on bikeshare users.\"\"\"\n",
    "    print(df.head())\n",
    "    next = 0\n",
    "    while True:\n",
    "        get_raw_data = input('\\nHello, would you like to see the first five rows of raw data? Type yes or no.\\n')\n",
    "        if get_raw_data.lower() != 'yes':\n",
    "            return\n",
    "        next = next + 5\n",
    "        print(df.iloc[next:next+5])\n",
    "\n",
    "\n",
    "def main():\n",
    "    while True:\n",
    "        city, month, day = get_filters()\n",
    "        df = load_data(city, month, day)\n",
    "\n",
    "        time_stats(df)\n",
    "        station_stats(df)\n",
    "        trip_duration_stats(df)\n",
    "        user_stats(df, city)\n",
    "        while True:\n",
    "            get_raw_data = input('\\nHello, would you like to see the first five rows of raw data? Type yes or no.\\n')\n",
    "            if get_raw_data.lower() != 'yes':\n",
    "                break\n",
    "            show_raw_data(df)\n",
    "            break\n",
    "\n",
    "        restart = input('\\nWould you like to restart? Enter yes or no.\\n')\n",
    "        if restart.lower() != 'yes':\n",
    "            break\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}