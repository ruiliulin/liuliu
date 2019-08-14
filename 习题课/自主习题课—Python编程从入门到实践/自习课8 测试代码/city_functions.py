# 11-1 城市和国家

def city_country_name(city_name, country_name, population=''):
    if population:
        cname = city_name.title() + ", " + country_name.title() + \
                ' -population ' + str(population)
    else:
        cname = city_name.title() + ", " + country_name.title()
    return cname

