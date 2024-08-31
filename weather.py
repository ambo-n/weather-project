import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_object = datetime.fromisoformat(iso_string)
    return date_object.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

    temp_in_celcius = (float(temp_in_fahrenheit)-32)*(5/9) 
    return round(temp_in_celcius,1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    new_weather_data =[float(data) for data in weather_data]
    return sum(new_weather_data)/len(new_weather_data)

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file) as file:
        csv_dictReader = csv.DictReader(file)
        return [[row["date"], float(row["min"]), float(row["max"])]for row in csv_dictReader if row]

def find_last_occurance(templist, value):
    """ Finds the index of the last occurance for the value of interest

    Args: 
        temp_list: a list of numbers
        value: value in which the index of the last occurance needs to be identified

    Returns:
        The index of the last occurance for the value of interest
    """
    return len(templist) - 1 - templist[::-1].index(value)

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    else:
        temps = [float(temp) for temp in weather_data]
        return min(temps), find_last_occurance(temps, min(temps))

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    else:
        temps = [float(temp) for temp in weather_data]
        return max(temps), find_last_occurance(temps, max(temps))

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    number_of_days= len(weather_data)
    min_temp_list =[float(sublist[1]) for sublist in weather_data]
    min_temp_in_week = find_min(min_temp_list)
    max_temp_list =[float(sublist[2]) for sublist in weather_data]
    max_temp_in_week = find_max(max_temp_list)

    return (
        f"{number_of_days} Day Overview\n"
        f"  The lowest temperature will be {convert_f_to_c(min_temp_in_week[0])}°C,"
        f" and will occur on {convert_date(weather_data [min_temp_in_week[1]][0])}.\n"
        f"  The highest temperature will be {convert_f_to_c(max_temp_in_week[0])}°C,"
        f" and will occur on {convert_date(weather_data [max_temp_in_week[1]][0])}.\n"
        f"  The average low this week is {convert_f_to_c(calculate_mean(min_temp_list))}°C.\n"
        f"  The average high this week is {convert_f_to_c(calculate_mean(max_temp_list))}°C.\n"
    )

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary_string = f""
    for sublist in weather_data:
        iso_string = sublist[0]
        min_temp = sublist[1]
        max_temp = sublist[2]
        summary_string += (
            f"---- {convert_date(iso_string)} ----\n"
            f"  Minimum Temperature: {convert_f_to_c(min_temp)}°C\n"
            f"  Maximum Temperature: {convert_f_to_c(max_temp)}°C\n\n"
        )
    return summary_string
    