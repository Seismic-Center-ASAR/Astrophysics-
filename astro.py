import ephem
logo = """

░█████╗░░██████╗████████╗██████╗░░█████╗░██████╗░░█████╗░██████╗░████████╗
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║██████╔╝██║░░██║██████╔╝░░░██║░░░
██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░░░░░╚█████╔╝██║░░██║░░░██║░░░V1
╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
                   by Seismic Center ASAR
         ,MMM8&&&.
    _...MMMMM88&&&&..._
 .::'''MMMMM88&&&&&&'''::.
::     MMMMM88&&&&&&     ::
'::....MMMMM88&&&&&&....::'
   `''''MMMMM88&&&&''''`
         'MMM8&&&'
"This software will return smallest separation between azimuth of multiple celestial objects and smallest altitude / elevation"
"""

print(logo)


# Define the planets and observer location
sun = ephem.Sun()
mercury= ephem.Mercury()
#sun = ephem.Sun()
observer = ephem.Observer()
#observer.date = "2023/4/21"
#observer.lat = '45.26'
#observer.lon = '27.26'
observer.elevation = 0
#stop_date = ephem.Date("2023/4/31")


observer_lat = input("Enter observer latitude (def.: 45.26): ")
observer_lon = input("Enter observer longitude (def.: 27.26): ")

observer.lat = observer_lat
observer.lon = observer_lon

#start_date = input("Enter start date (yyyy/mm/dd): ")
#observer.date = start_date

stop_date_str = input("Enter stop date (yyyy/mm/dd - Eg.:2023/4/30): ")
stop_date = ephem.Date(stop_date_str)

separation_degree = float(input("Enter the desired separation degree (def.:0.2): "))

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    sun.compute(observer)
    mercury.compute(observer)
  #  sun.compute(observer)
    azimuths = [sun.az, mercury.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "sun mercury")
        results = (str(observer.date), "azimuth sun mercury")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
    elevation = [sun.alt, mercury.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation sun mercury")
        results = (str(observer.date), "elevation sun mercury")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
sun = ephem.Sun()
venus= ephem.Venus()
#sun = ephem.Sun()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    sun.compute(observer)
    venus.compute(observer)
  #  sun.compute(observer)
    azimuths = [sun.az, venus.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "sun venus")
        results = (str(observer.date), "azimuth sun venus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
    elevation = [sun.alt, venus.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation  sun venus")
        results = (str(observer.date), "elevation sun venus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
sun = ephem.Sun()
moon= ephem.Moon()
#sun = ephem.Sun()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    sun.compute(observer)
    moon.compute(observer)
  #  sun.compute(observer)
    azimuths = [sun.az, moon.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "sun moon")
        results = (str(observer.date), "azimuth sun moon")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
    elevation = [sun.alt, moon.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation  sun moon")
        results = (str(observer.date), "elevation sun moon")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
sun = ephem.Sun()
mars= ephem.Mars()
#sun = ephem.Sun()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    sun.compute(observer)
    mars.compute(observer)
  #  sun.compute(observer)
    azimuths = [sun.az, mars.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "sun mars")
        results = (str(observer.date), "azimuth sun mars")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
    elevation = [sun.alt, mars.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation sun mars")
        results = (str(observer.date), "elevation sun mars")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
sun = ephem.Sun()
jupiter= ephem.Jupiter()
#sun = ephem.Sun()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    sun.compute(observer)
    jupiter.compute(observer)
  #  sun.compute(observer)
    azimuths = [sun.az, jupiter.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "sun jupiter")
        results = (str(observer.date), "azimuth sun jupiter")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [sun.alt, jupiter.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation sun jupiter")
        results = (str(observer.date), "elevation sun jupiter")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
sun = ephem.Sun()
saturn= ephem.Saturn()
#sun = ephem.Sun()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    sun.compute(observer)
    saturn.compute(observer)
  #  sun.compute(observer)
    azimuths = [sun.az, saturn.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "sun saturn")
        results = (str(observer.date), "azimuth sun saturn")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [sun.alt, saturn.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation sun saturn")
        results = (str(observer.date), "elevation sun saturn")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
sun = ephem.Sun()
uranus= ephem.Uranus()
#sun = ephem.Sun()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    sun.compute(observer)
    uranus.compute(observer)
  #  sun.compute(observer)
    azimuths = [sun.az, uranus.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "sun uranus")
        results = (str(observer.date), "azimuth sun uranus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [sun.alt, uranus.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation sun uranus")
        results = (str(observer.date), "elevation sun urnaus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
sun = ephem.Sun()
neptune= ephem.Neptune()
#sun = ephem.Sun()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    sun.compute(observer)
    neptune.compute(observer)
  #  sun.compute(observer)
    azimuths = [sun.az, neptune.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "sun neptune")
        results = (str(observer.date), "azimuth sun neptune" )
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [sun.alt, neptune.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation sun neptune")
        results = (str(observer.date), "elevation sun neptune")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
sun = ephem.Sun()
pluto= ephem.Pluto()
#sun = ephem.Sun()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    sun.compute(observer)
    pluto.compute(observer)
  #  sun.compute(observer)
    azimuths = [sun.az, pluto.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "sun pluto")
        results = (str(observer.date), "azimuth sun pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [sun.alt, pluto.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation sun pluto")
        results = (str(observer.date), "elevation sun pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		
#-----------------------------------------------------------------------------------
# Define the planets and observer location
mercury = ephem.Mercury()
venus= ephem.Venus()
#mercury = ephem.mercury()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mercury.compute(observer)
    venus.compute(observer)
  #  mercury.compute(observer)
    azimuths = [mercury.az, venus.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mercur venus")
        results = (str(observer.date), "azimuth mercury venus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mercury.alt, venus.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mercur venus")
        results = (str(observer.date), "elevation mer venus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mercury = ephem.Mercury()
moon= ephem.Moon()
#mercury = ephem.mercury()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mercury.compute(observer)
    moon.compute(observer)
  #  mercury.compute(observer)
    azimuths = [mercury.az, moon.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mercur moon")
        results = (str(observer.date), "azimuth mercury moon")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mercury.alt, moon.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mercur moon")
        results = (str(observer.date), "elevation merc moon")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mercury = ephem.Mercury()
mars= ephem.Mars()
#mercury = ephem.mercury()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mercury.compute(observer)
    mars.compute(observer)
  #  mercury.compute(observer)
    azimuths = [mercury.az, mars.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), " mercur mars")
        results = (str(observer.date), "azimuth merc mars")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mercury.alt, mars.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mercur mars")
        results = (str(observer.date), "elevation merc mars")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mercury = ephem.Mercury()
jupiter= ephem.Jupiter()
#mercury = ephem.mercury()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mercury.compute(observer)
    jupiter.compute(observer)
  #  mercury.compute(observer)
    azimuths = [mercury.az, jupiter.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mercur jupiter")
        results = (str(observer.date), "azimuth merc jupiter")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mercury.alt, jupiter.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mercur jupiter")
        results = (str(observer.date), "elevation merc jupiter")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mercury = ephem.Mercury()
saturn= ephem.Saturn()
#mercury = ephem.mercury()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mercury.compute(observer)
    saturn.compute(observer)
  #  mercury.compute(observer)
    azimuths = [mercury.az, saturn.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mercur saturn")
        results = (str(observer.date), "azimuth merc sat")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mercury.alt, saturn.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mercur saturn")
        results = (str(observer.date), "elevation merc sat")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mercury = ephem.Mercury()
uranus= ephem.Uranus()
#mercury = ephem.mercury()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mercury.compute(observer)
    uranus.compute(observer)
  #  mercury.compute(observer)
    azimuths = [mercury.az, uranus.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mercur uranus")
        results = (str(observer.date), "azimuth merc uransu")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mercury.alt, uranus.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mercur uranus")
        results = (str(observer.date), "elevation merc uranus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mercury = ephem.Mercury()
neptune= ephem.Neptune()
#mercury = ephem.mercury()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mercury.compute(observer)
    neptune.compute(observer)
  #  mercury.compute(observer)
    azimuths = [mercury.az, neptune.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mercur neptune")
        results = (str(observer.date), "azimuth merc nept")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mercury.alt, neptune.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mercur neptun")
        results = (str(observer.date), "elevation merc nept")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mercury = ephem.Mercury()
pluto= ephem.Pluto()
#mercury = ephem.mercury()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mercury.compute(observer)
    pluto.compute(observer)
  #  mercury.compute(observer)
    azimuths = [mercury.az, pluto.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mercur pluto")
        results = (str(observer.date), "azimuth merc pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mercury.alt, pluto.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mercur pluto")
        results = (str(observer.date), "elevation merc pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
venus = ephem.Venus()
moon= ephem.Moon()
#venus = ephem.venus()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    venus.compute(observer)
    moon.compute(observer)
  #  venus.compute(observer)
    azimuths = [venus.az, moon.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "venus moon")
        results = (str(observer.date), "azimuth venus moon")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [venus.alt, moon.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation venus moon")
        results = (str(observer.date), "elevation venus moon")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
venus = ephem.Venus()
mars= ephem.Mars()
#venus = ephem.venus()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    venus.compute(observer)
    mars.compute(observer)
  #  venus.compute(observer)
    azimuths = [venus.az, mars.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "venus mars")
        results = (str(observer.date), "azimuth venbus mars")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [venus.alt, mars.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation venus mars")
        results = (str(observer.date), "elevation venus mars")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
venus = ephem.Venus()
jupiter= ephem.Jupiter()
#venus = ephem.venus()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    venus.compute(observer)
    jupiter.compute(observer)
  #  venus.compute(observer)
    azimuths = [venus.az, jupiter.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "venus jupiter")
        results = (str(observer.date), "azimuth venus jupiter")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [venus.alt, jupiter.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation venus jupiter")
        results = (str(observer.date), "elevation venus jupiter")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
venus = ephem.Venus()
saturn= ephem.Saturn()
#venus = ephem.venus()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    venus.compute(observer)
    saturn.compute(observer)
  #  venus.compute(observer)
    azimuths = [venus.az, saturn.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "venus saturn")
        results = (str(observer.date), "azimuth venus saturn")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [venus.alt, saturn.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation venus saturn")
        results = (str(observer.date), "elevation venus saturn")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
venus = ephem.Venus()
uranus= ephem.Uranus()
#venus = ephem.venus()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    venus.compute(observer)
    uranus.compute(observer)
  #  venus.compute(observer)
    azimuths = [venus.az, uranus.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "venus uranus")
        results = (str(observer.date), "azimuth venus uranus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [venus.alt, uranus.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation venus uranus")
        results = (str(observer.date), "elevation venus uranus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
venus = ephem.Venus()
neptune= ephem.Neptune()
#venus = ephem.venus()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    venus.compute(observer)
    neptune.compute(observer)
  #  venus.compute(observer)
    azimuths = [venus.az, neptune.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "venus neptun")
        results = (str(observer.date), "azimuth venus neptune")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [venus.alt, neptune.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation venus neptun")
        results = (str(observer.date), "elevation venus neptune")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
venus = ephem.Venus()
pluto= ephem.Pluto()
#venus = ephem.venus()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    venus.compute(observer)
    pluto.compute(observer)
  #  venus.compute(observer)
    azimuths = [venus.az, pluto.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "venus pluto")
        results = (str(observer.date), "azimuth venus pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [venus.alt, pluto.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation venus pluto")
        results = (str(observer.date), "elevation venus pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
moon = ephem.Moon()
mars= ephem.Mars()
#moon = ephem.moon()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    moon.compute(observer)
    mars.compute(observer)
  #  moon.compute(observer)
    azimuths = [moon.az, mars.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "moon mars")
        results = (str(observer.date), "azimuth moon mars")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [moon.alt, mars.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation moon mars")
        results = (str(observer.date), "elevation moon mars")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
moon = ephem.Moon()
jupiter= ephem.Jupiter()
#moon = ephem.moon()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    moon.compute(observer)
    jupiter.compute(observer)
  #  moon.compute(observer)
    azimuths = [moon.az, jupiter.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), " moon jupiter")
        results = (str(observer.date), "azimuth moon jupiter")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [moon.alt, jupiter.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation moon jupiter")
        results = (str(observer.date), "elevation moon jupiter")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
moon = ephem.Moon()
saturn= ephem.Saturn()
#moon = ephem.moon()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    moon.compute(observer)
    saturn.compute(observer)
  #  moon.compute(observer)
    azimuths = [moon.az, saturn.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "moon saturn")
        results = (str(observer.date), "azimuth moon sat")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
    elevation = [moon.alt, saturn.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation moon saturn")
        results = (str(observer.date), "elevation moon sat")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
moon = ephem.Moon()
uranus= ephem.Uranus()
#moon = ephem.moon()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    moon.compute(observer)
    uranus.compute(observer)
  #  moon.compute(observer)
    azimuths = [moon.az, uranus.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "moon uranus")
        results = (str(observer.date), "azimuth moon ura")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [moon.alt, uranus.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation moon uranus")
        results = (str(observer.date), "elevation moon uranus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
		

# Define the planets and observer location
moon = ephem.Moon()
neptune= ephem.Neptune()
#moon = ephem.moon()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    moon.compute(observer)
    neptune.compute(observer)
  #  moon.compute(observer)
    azimuths = [moon.az, neptune.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "moon neptune")
        results = (str(observer.date), "azimuth moon neptune")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [moon.alt, neptune.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation moon neptune")
        results = (str(observer.date), "elevation moon neptune")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
moon = ephem.Moon()
pluto= ephem.Pluto()
#moon = ephem.moon()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    moon.compute(observer)
    pluto.compute(observer)
  #  moon.compute(observer)
    azimuths = [moon.az, pluto.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "moon pluto")
        results = (str(observer.date), "azimuth moon pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [moon.alt, pluto.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation moon pluto")
        results = (str(observer.date), "elevation moon pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mars = ephem.Mars()
jupiter= ephem.Jupiter()
#mars = ephem.mars()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mars.compute(observer)
    jupiter.compute(observer)
  #  mars.compute(observer)
    azimuths = [mars.az, jupiter.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mars jupiter")
        results = (str(observer.date), "azimuth mars jupiter")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mars.alt, jupiter.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mars jupiter")
        results = (str(observer.date), "elevation mars jupiter")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mars = ephem.Mars()
saturn= ephem.Saturn()
#mars = ephem.mars()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mars.compute(observer)
    saturn.compute(observer)
  #  mars.compute(observer)
    azimuths = [mars.az, saturn.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mars sat")
        results = (str(observer.date), "azimuth mars sat")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mars.alt, saturn.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mars sat")
        results = (str(observer.date), "elevation mars sat")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mars = ephem.Mars()
uranus= ephem.Uranus()
#mars = ephem.mars()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mars.compute(observer)
    uranus.compute(observer)
  #  mars.compute(observer)
    azimuths = [mars.az, uranus.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mars uranus")
        results = (str(observer.date), "azimuth mars ura")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mars.alt, uranus.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mars uranus")
        results = (str(observer.date), "elevation mars ura")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mars = ephem.Mars()
neptune= ephem.Neptune()
#mars = ephem.mars()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mars.compute(observer)
    neptune.compute(observer)
  #  mars.compute(observer)
    azimuths = [mars.az, neptune.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mars neptune")
        results = (str(observer.date), "azimuth mars neptune")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mars.alt, neptune.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mars neptune")
        results = (str(observer.date), "elevation mars neptune")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
mars = ephem.Mars()
pluto= ephem.Pluto()
#mars = ephem.mars()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    mars.compute(observer)
    pluto.compute(observer)
  #  mars.compute(observer)
    azimuths = [mars.az, pluto.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "mars pluto")
        results = (str(observer.date), "azimuth mars pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [mars.alt, pluto.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation mars pluto")
        results = (str(observer.date), "elevation mars pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
jupiter = ephem.Jupiter()
saturn= ephem.Saturn()
#jupiter = ephem.jupiter()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    jupiter.compute(observer)
    saturn.compute(observer)
  #  jupiter.compute(observer)
    azimuths = [jupiter.az, saturn.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "jupiter saturn")
        results = (str(observer.date), "azimuth jupiter saturn")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [jupiter.alt, saturn.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation jupiter saturn")
        results = (str(observer.date), "elevation jupiter saturn")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
jupiter = ephem.Jupiter()
uranus= ephem.Uranus()
#jupiter = ephem.jupiter()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    jupiter.compute(observer)
    uranus.compute(observer)
  #  jupiter.compute(observer)
    azimuths = [jupiter.az, uranus.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "jupiter uranus")
        results = (str(observer.date), "azimuth jupit uran")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [jupiter.alt, uranus.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation jupiter uranus")
        results = (str(observer.date), "elevation jupit uranus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
jupiter = ephem.Jupiter()
neptune= ephem.Neptune()
#jupiter = ephem.jupiter()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    jupiter.compute(observer)
    neptune.compute(observer)
  #  jupiter.compute(observer)
    azimuths = [jupiter.az, neptune.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "jupiter neptune")
        results = (str(observer.date), "azimuth jupiter neptune")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [jupiter.alt, neptune.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation jupiter neptune")
        results = (str(observer.date), "elevation jupiter neptune")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
jupiter = ephem.Jupiter()
pluto= ephem.Pluto()
#jupiter = ephem.jupiter()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    jupiter.compute(observer)
    pluto.compute(observer)
  #  jupiter.compute(observer)
    azimuths = [jupiter.az, pluto.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "jupiter pluto")
        results = (str(observer.date), "azimuth jupit pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [jupiter.alt, pluto.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation jupiter pluto")
        results = (str(observer.date), "elevation jupit pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
saturn = ephem.Saturn()
uranus= ephem.Uranus()
#saturn = ephem.saturn()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    saturn.compute(observer)
    uranus.compute(observer)
  #  saturn.compute(observer)
    azimuths = [saturn.az, uranus.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "saturn uranus")
        results = (str(observer.date), "azimuth saturn uranus")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [saturn.alt, uranus.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation saturn uranus")
        results = (str(observer.date), "elevation sat uran")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
saturn = ephem.Saturn()
neptune= ephem.Neptune()
#saturn = ephem.saturn()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    saturn.compute(observer)
    neptune.compute(observer)
  #  saturn.compute(observer)
    azimuths = [saturn.az, neptune.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "saturn neptune")
        results = (str(observer.date), "azimuth saturn neptune")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [saturn.alt, neptune.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation saturn neptune")
        results = (str(observer.date), "elevation saturn neptune")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
saturn = ephem.Saturn()
pluto= ephem.Pluto()
#saturn = ephem.saturn()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    saturn.compute(observer)
    pluto.compute(observer)
  #  saturn.compute(observer)
    azimuths = [saturn.az, pluto.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "saturn plutio")
        results = (str(observer.date), "azimuth saturn pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [saturn.alt, pluto.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation saturn pluto")
        results = (str(observer.date), "elevation saturn pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
uranus = ephem.Uranus()
neptune= ephem.Neptune()
#uranus = ephem.uranus()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    uranus.compute(observer)
    neptune.compute(observer)
  #  uranus.compute(observer)
    azimuths = [uranus.az, neptune.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "uranus neptune")
        results = (str(observer.date), "azimuth ura nept")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [uranus.alt, neptune.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation uranus neptun")
        results = (str(observer.date), "elevation ura neptu")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
uranus = ephem.Uranus()
pluto= ephem.Pluto()
#uranus = ephem.uranus()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    uranus.compute(observer)
    pluto.compute(observer)
  #  uranus.compute(observer)
    azimuths = [uranus.az, pluto.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "uranus pluto")
        results = (str(observer.date), "azimuth ura pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [uranus.alt, pluto.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation uranus pluto")
        results = (str(observer.date), "elevation ura pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
    
       
		

# Define the planets and observer location
neptune = ephem.Neptune()
pluto= ephem.Pluto()
#neptune = ephem.neptune()
observer = ephem.Observer()
#observer.date = "2023/4/21"
observer.lat = '45.26'
observer.lon = '27.26'
observer.elevation = 0

# Find the next time the azimuths of the three planets are similar
while True:
    observer.date += ephem.minute * 10  # Increase time by 10 minutes each iteration    # Check if the current date is greater than or equal to the stop date
    if observer.date >= stop_date:
        break
    neptune.compute(observer)
    pluto.compute(observer)
  #  neptune.compute(observer)
    azimuths = [neptune.az, pluto.az]
    max_az = max(azimuths)
    min_az = min(azimuths)
    if (max_az - min_az) < ephem.degrees('0.5'):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "neptune pluto")
        results = (str(observer.date), "azimuth nept pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()
        
        
    elevation = [neptune.alt, pluto.alt]
    max_alt = max(elevation)
    min_alt = min(elevation)
    if (max_alt - min_alt) < ephem.degrees(str(separation_degree)):  # Check if the difference in azimuths is less than 1 degree
        print('{:%Y/%m/%d %H:%M:%S}'.format(observer.date.datetime()), "elevation neptun pluto")
        results = (str(observer.date), "elevation nept pluto")
        f = open("demofile2.txt", "a")
        f.write(str(results))
        f.close()


        break

    
     
		
