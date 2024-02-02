def calculate_days_and_seconds_final(start_str, end_str):
    """Функция для вычисления количества дней с начала года до даты"""
    def days_before_date(year, month, day):
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days_per_month[:month - 1]) + day

    """Парсинг входных строк"""
    year1, month1, day1, hour1, min1, sec1 = [int(x) for x in start_str.split(', ')]
    year2, month2, day2, hour2, min2, sec2 = [int(x) for x in end_str.split(', ')]

    """Расчет количества дней до начальной и конечной даты от начала года"""
    days_start_year = days_before_date(year1, month1, day1)
    days_end_year = days_before_date(year2, month2, day2)

    """Расчет полных дней между годами"""
    full_years_days = (year2 - year1) * 365

    """Общее количество дней"""
    total_days = full_years_days - days_start_year + days_end_year

    """Расчет секунд в неполном дне"""
    start_seconds = hour1 * 3600 + min1 * 60 + sec1
    end_seconds = hour2 * 3600 + min2 * 60 + sec2
    remaining_seconds = end_seconds - start_seconds
    if remaining_seconds < 0:
        remaining_seconds += 24 * 3600
        total_days -= 1

    if year1 == year2 and month1 == month2 and day1 == day2:
        total_days -= 1

    return total_days, remaining_seconds
