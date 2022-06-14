import os
import shutil
import winreg
import datetime as tm
import time as Time
import pandas as pd
from Bio import Phylo
from splinter import Browser

print('PAReTT: Python Automated Retrieval from Time Tree (1.0.1)')
print('Copyright (C) 2022 University of the Free State')
print('This is free software.  There is NO warranty; not even for',
      'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.')
print()

def menu_choice():
    """ Find out what the user wants to do next. """
    print("MAIN MENU:")
    print("----------------------------------------")
    print("Choose one of the following options?")
    print("   *) Check data availability")
    print("   a) Get Divergence Times (pair)")
    print("   b) Get Divergence Times (batch)")
    print("   c) Get Evolutionary Timeline")
    print("   d) Build a Time Tree")
    print("   e) Print citation")
    print("   f) Validate datafile")
    print("   q) Quit")
    print("----------------------------------------")
    choice = input("Choice: ")
    print()
    if choice.lower() in ['*','a','b','c','d','e','f','q']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        print()
        Time.sleep(3)
        return None

def check_avail_menu():
    """Menu options for checking data availability function"""
    print('AVAILABILITY MENU:')
    print("----------------------------------------")
    print("Choose one of the following options?")
    print("     i) Individual")
    print("     l) List")
    print("     m) Main menu")
    print("----------------------------------------")
    choice = input("Choice: ")
    print()
    if choice.lower() in ['i','l','m']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        Time.sleep(3)
        return None

def check_available():
    """Checks the time tree website to confirm if data is available for a species"""
    choice = check_avail_menu()
    if choice == "i":
        name = input("Name: ")
        with Browser('firefox', headless=True) as browser:
            browser.visit('http://timetree.org')
            browser.fill('timeline_taxon', name)
            browser.find_by_id('timeline-search-button1').click()
            check = browser.is_text_present('Evolutionary Timeline for', wait_time=15)
            if check is True:
                value = 'Available'
                time = tm.datetime.now()
                print('{:<25}'.format(name), end="")
                print('{:<25}'.format(value), end="")
                print(time)
            elif check is False:
                value = 'Not Available'
                time = tm.datetime.now()
                print('{:<25}'.format(name), end="")
                print('{:<25}'.format(value), end="")
                print(time)
            print("Done!")
            print()
    elif choice == 'l':
        data = pd.DataFrame(columns = ['Species', 'TimeTree.Data'])
        infile = input("Input file in .txt format: ")
        if infile.endswith('.txt') is True:
            pass
        elif infile.endswith('.txt') is False:
            infile = infile + '.txt'
        try:
            my_file = open(infile, "r")
        except FileNotFoundError:
            print("File not found")
            return
        else:
            my_file = open(infile, "r")
        content = my_file.read()
        content_list = content.split("\n")
        my_file.close()
        converted_list =[]
        for element in content_list:
            converted_list.append(element.strip())
        species = tuple(converted_list)
        for i in range(0,len(species)):
            name = species[i]
            with Browser('firefox', headless=True) as browser:
                browser.visit('http://timetree.org')
                browser.fill('timeline_taxon', name)
                browser.find_by_id('timeline-search-button1').click()
                browser.is_text_present('Evolutionary Timeline for', wait_time=120)
                check = browser.is_text_present('Evolutionary Timeline for', wait_time=15)
                if check is True:
                    value = 'Available'
                    time = tm.datetime.now()
                    print('{:<25}'.format(name), end="")
                    print('{:<25}'.format(value), end="")
                    print(time)
                    data = data.append({'Species': name, 'TimeTree.Data': 'Available'},
                                       ignore_index=True)
                elif check is False:
                    value = 'Not Available'
                    time = tm.datetime.now()
                    print('{:<25}'.format(name), end="")
                    print('{:<25}'.format(value), end="")
                    print(time)
                    print("Done!")
                    data = data.append({'Species': name, 'TimeTree.Data': 'Not Available'},
                                       ignore_index=True)
        output_name = input("File name (.csv): ")
        if output_name.endswith('.csv') is True:
            pass
        elif output_name.endswith('.csv') is False:
            output_name = output_name + '.csv'
        data.to_csv(output_name, index=False)
        print("Done!")
        print()

def div_times_sing():
    """Get the times for a single pair specified as input"""
    taxon_a = input("Taxon a: ")
    taxon_b = input("Taxon b: ")
    with Browser('firefox', headless=True) as browser:
        browser.visit('http://timetree.org')
        browser.fill('taxon_a', taxon_a)
        browser.fill('taxon_b', taxon_b)
        browser.find_by_id('pairwise-search-button1').click()
        browser.is_text_present('Median Time', wait_time=320)
        var_y = '#pairwise-results > text:nth-child(11)'
        divtime = browser.find_by_css(var_y).first.value
        divtime_2 = divtime.replace(' MYA', '')
        time = tm.datetime.now()
        print('{:<25}'.format(taxon_a), end="")
        print('{:<25}'.format(taxon_b), end="")
        print('{:<5}'.format(divtime_2), end="")
        print(time)
        print()

def div_times_batch():
    """Get the divergence times for a list of species and stores it as a data-
    frame which gets exported as a .csv with 3 columns"""
    data = pd.DataFrame(columns = ['Taxa1', 'Taxa2', 'Div.Time'])
    infile = input("Input file in .txt format: ")
    if infile.endswith('.txt') is True:
        pass
    elif infile.endswith('.txt') is False:
        infile = infile + '.txt'
    try:
        my_file = open(infile, "r")
    except FileNotFoundError:
        print("File not found")
        return
    else:
        my_file = open(infile, "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    converted_list =[]
    for element in content_list:
        converted_list.append(element.strip())
    species = tuple(converted_list)
    length = len(species)
    for variable_x in range(0,length):
        for i in range(0,length):
            taxon_a = species[variable_x]
            taxon_b = species[i]
            if taxon_b == species[-1]:
                if taxon_a == taxon_b:
                    time = tm.datetime.now()
                    print('{:<25}'.format(taxon_a), end="")
                    print('{:<25}'.format(taxon_b), end="")
                    print('{:<5}'.format('0'), end="")
                    print(time)
                    data = data.append({'Taxa1' : taxon_a, 'Taxa2' : taxon_b, 'Div.Time' : '0'},
                    ignore_index = True)
                else:
                    with Browser('firefox', headless=True) as browser:
                        try:
                            browser.visit('http://timetree.org')
                            browser.fill('taxon_a', taxon_a)
                            browser.fill('taxon_b', taxon_b)
                            browser.find_by_id('pairwise-search-button1').click()
                        except:
                            Time.sleep(600)
                            browser.visit('http://timetree.org')
                            browser.fill('taxon_a', taxon_a)
                            browser.fill('taxon_b', taxon_b)
                            browser.find_by_id('pairwise-search-button1').click()
                        browser.is_text_present('Median Time', wait_time=320)
                        var_y = '#pairwise-results > text:nth-child(11)'
                        try:
                            divtime = browser.find_by_css(var_y).first.value
                        except:
                            divtime = 'NA MYA'
                        else:
                            divtime = browser.find_by_css(var_y).first.value
                        divtime_2 = divtime.replace(' MYA', '')
                        time = tm.datetime.now()
                        print('{:<25}'.format(taxon_a), end="")
                        print('{:<25}'.format(taxon_b), end="")
                        print('{:<5}'.format(divtime_2), end="")
                        print(time)
                        data = data.append({'Taxa1' : taxon_a, 'Taxa2' : taxon_b,
                                        'Div.Time' : divtime_2}, ignore_index = True)
                print(taxon_a,'DONE!')
            else:
                if taxon_a == taxon_b:
                    time = tm.datetime.now()
                    print('{:<25}'.format(taxon_a), end="")
                    print('{:<25}'.format(taxon_b), end="")
                    print('{:<5}'.format('0'), end="")
                    print(time)
                    data = data.append({'Taxa1' : taxon_a, 'Taxa2' : taxon_b, 'Div.Time' : '0'},
                    ignore_index = True)
                else:
                    with Browser('firefox', headless=True) as browser:
                        try:
                            browser.visit('http://timetree.org')
                            browser.fill('taxon_a', taxon_a)
                            browser.fill('taxon_b', taxon_b)
                            browser.find_by_id('pairwise-search-button1').click()
                        except:
                            Time.sleep(600)
                            browser.visit('http://timetree.org')
                            browser.fill('taxon_a', taxon_a)
                            browser.fill('taxon_b', taxon_b)
                            browser.find_by_id('pairwise-search-button1').click()
                        browser.is_text_present('Median Time', wait_time=320)
                        var_y = '#pairwise-results > text:nth-child(11)'
                        try:
                            divtime = browser.find_by_css(var_y).first.value
                        except:
                            divtime = 'NA MYA'
                        else:
                            divtime = browser.find_by_css(var_y).first.value
                        divtime_2 = divtime.replace(' MYA', '')
                        time = tm.datetime.now()
                        print('{:<25}'.format(taxon_a), end="")
                        print('{:<25}'.format(taxon_b), end="")
                        print('{:<5}'.format(divtime_2), end="")
                        print(time)
                        data = data.append({'Taxa1' : taxon_a, 'Taxa2' : taxon_b,
                                        'Div.Time' : divtime_2}, ignore_index = True)
    if i == len(species):
        print(taxon_a," DONE!")
    data.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)
    print()
    print(data)
    print()
    output_name = input("File name (.csv): ")
    if output_name.endswith('.csv') is True:
        pass
    elif output_name.endswith('.csv') is False:
        output_name = output_name + '.csv'
    data.to_csv(output_name, index=False)
    print("Done!")
    print()

def timeline_menu():
    """Menu options for timeline function"""
    print('TIMELINE MENU:')
    print("----------------------------------------")
    print("Choose one of the following options?")
    print("     i) Individual")
    print("     l) List")
    print("     m) Main menu")
    print("----------------------------------------")
    choice = input("Choice: ")
    print()
    if choice.lower() in ['i','l','m']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        Time.sleep(3)
        return None

def evol_timeline():
    """Gets the evolutionary timeline for a species or taxa given a single
    name or a list"""
    choice = timeline_menu()
    if choice == "i":
        name = input("Name: ")
        with Browser('firefox', headless=True) as browser:
            browser.visit('http://timetree.org')
            browser.fill('timeline_taxon', name)
            browser.find_by_id('timeline-search-button1').click()
            browser.is_text_present('Evolutionary Timeline for', wait_time=15)
            browser.find_by_id('timeline-timeline-svg-export-btn').click()
            downloads = get_download_path()
            current = os.getcwd()
            file = name + '_' + 'timeline.jpg'
            indir = str(downloads) + '\\' + file
            outdir = str(current) + '\\' + file
            shutil.move(indir, outdir)
            print("Done!")
            print()
    elif choice == 'l':
        infile = input("Input file in .txt format: ")
        if infile.endswith('.txt') is True:
            pass
        elif infile.endswith('.txt') is False:
            infile = infile + '.txt'
        try:
            my_file = open(infile, "r")
        except FileNotFoundError:
            print("File not found")
            return
        else:
            my_file = open(infile, "r")
        content = my_file.read()
        content_list = content.split("\n")
        my_file.close()
        converted_list =[]
        for element in content_list:
            converted_list.append(element.strip())
        species = tuple(converted_list)
        for i in range(0,len(species)):
            name = species[i]
            with Browser('firefox', headless=True) as browser:
                browser.visit('http://timetree.org')
                browser.fill('timeline_taxon', name)
                browser.find_by_id('timeline-search-button1').click()
                browser.is_text_present('Evolutionary Timeline for', wait_time=120)
                browser.find_by_id('timeline-timeline-svg-export-btn').click()
                time = tm.datetime.now()
                print('{:<25}'.format(name), end="")
                print(time)
                downloads = get_download_path()
                current = os.getcwd()
                file = name + '_' + 'timeline.jpg'
                indir = str(downloads) + '\\' + file
                outdir = str(current) + '\\' + file
                shutil.move(indir, outdir)
        print("Done!")
        print()
    elif choice == 'm':
        main_loop()

def time_tree_menu():
    """Menu options for time tree function"""
    print('TIME TREE MENU:')
    print("----------------------------------------")
    print("Choose one of the following options?")
    print("     t) Taxon")
    print("     s) Species list")
    print("     m) Main menu")
    print("----------------------------------------")
    choice = input("Choice: ")
    if choice.lower() in ['t','s','m']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        Time.sleep(3)
        return None

def time_tree():
    """Takes a species list as input and returns a time tree in one of the specified
    formats"""
    choice = time_tree_menu()
    if choice == 't':
        name = input("Name: ")
        with Browser('firefox', headless=True) as browser:
            browser.visit('http://timetree.org')
            browser.fill('timetree_taxon', name)
            browser.find_by_id('timetree-search-button1').click()
            browser.find_by_id('generate-download-button').click()
            downloads = get_download_path()
            current = os.getcwd()
            file = name + '_' + 'species.nwk'
            indir = str(downloads) + '\\' + file
            outdir = str(current) + '\\' + file
            shutil.move(indir, outdir)
            print("Done!")
        print()
    elif choice == 's':
        infile_name = input("Input file in .txt format: ")
        if infile_name.endswith('.txt') is True:
            pass
        elif infile_name.endswith('.txt') is False:
            infile_name = infile_name + '.txt'
        try:
            open(infile_name, "r")
        except FileNotFoundError:
            print("File not found")
            return
        if os.path.isfile(infile_name) is True:
            pass
        elif os.path.isfile(infile_name) is False:
            print("No such file!")
            return
        path = os.getcwd()
        infile_path = path + "\\" + infile_name
        print(infile_path)
        with Browser('firefox', headless=True) as browser:
            browser.visit('http://timetree.org')
            browser.attach_file("prunetree_upload", infile_path)
            browser.find_by_id('prunetree-upload-button1').click()
            browser.is_text_present('Geologic Timescale', wait_time=320)
            browser.find_by_id('prunetree-msg-btn').click()
            try:
                replaced = browser.find_by_id('unresolved-names').value
            except BaseException:
                pass
            else:
                replaced = browser.find_by_id('unresolved-names').value
                file = open('Unresolved names.txt','w')
                file.write(replaced)
                file.close()
            browser.find_by_id('prunetree-newick-export-btn').click()
            downloads = get_download_path()
            current = os.getcwd()
            file = infile_name.replace('.txt', '.nwk')
            indir = str(downloads) + '\\' + file
            outdir = str(current) + '\\' + file
            shutil.move(indir, outdir)
            print("Done!")
            print()
    elif choice == 'm':
        main_loop()

def citation():
    """Prints the citation for the timetree resource"""
    print()
    print("CITE THE TIME TREE RESOURCE AS:")
    print("S. Kumar, G. Stecher, M. Suleski, and S.B. Hedges, 2017.",
          " TimeTree: a resource for timelines, timetrees, and divergence times.",
          " Molecular Biology and Evolution 34: 1812-1819,",
          " DOI: 10.1093/molbev/msx116")
    print()

def validate_menu():
    """Menu options for validate function"""
    print("VALIDATE MENU:")
    print("----------------------------------------")
    print("      a) Check missing")
    print("      b) Replace missing")
    print("      c) View tree")
    print("      m) Main menu")
    print("----------------------------------------")
    choice = input("Choice: ")
    if choice.lower() in ['a','b','c','m']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        Time.sleep(3)
        return None

def validate():
    """Checks output file for missing values"""
    choice = validate_menu()
    if choice == 'a':
        infile = input("File to check (.csv): ")
        if infile.endswith('.csv') is True:
            pass
        elif infile.endswith('.csv') is False:
            infile = infile + '.csv'
        data = pd.read_csv(infile)
        length = len(data.index)
        indices = data.loc[pd.isna(data).any(1), :].index
        check = len(indices)
        if check >= 1:
            missing = pd.DataFrame(columns = ['Taxa1', 'Taxa2', 'Div.Time'])
            for i in range (0, length):
                if i in indices:
                    taxon_a = data.iloc[i]['Taxa1']
                    taxon_b = data.iloc[i]['Taxa2']
                    with Browser('firefox', headless=True) as browser:
                        try:
                            browser.visit('http://timetree.org')
                            browser.fill('taxon_a', taxon_a)
                            browser.fill('taxon_b', taxon_b)
                            browser.find_by_id('pairwise-search-button1').click()
                        except KeyboardInterrupt as error:
                            print('An exception occurred: {}'.format(error))
                            return
                        else:
                            browser.visit('http://timetree.org')
                            browser.fill('taxon_a', taxon_a)
                            browser.fill('taxon_b', taxon_b)
                            browser.find_by_id('pairwise-search-button1').click()
                        browser.is_text_present('Median Time', wait_time=320)
                        var_y = '#pairwise-results > text:nth-child(11)'
                        divtime = browser.find_by_css(var_y).first.value
                        divtime_2 = divtime.replace(' MYA', '')
                        missing = missing.append({'Taxa1' : taxon_a, 'Taxa2' : taxon_b,
                                                'Div.Time' : divtime_2}, ignore_index = True)
                    time = tm.datetime.now()
                    print('{:<25}'.format(taxon_a), end="")
                    print('{:<25}'.format(taxon_b), end="")
                    print('{:<5}'.format(divtime_2), end="")
                    print(time)
            output_name = input("File name (.csv) for missing values: ")
            if output_name.endswith(".csv") is True:
                pass
            elif output_name.endswith('.csv') is False:
                output_name = output_name + '.csv'
            missing.to_csv(output_name, index=False)
        else:
            print("No missing values detected!")
    elif choice == 'b':
        infile_1 = input("File to check (.csv): ")
        if infile_1.endswith('.csv') is True:
            pass
        elif infile_1.endswith('.csv') is False:
            infile_1 = infile_1 + '.csv'
        data = pd.read_csv(infile_1)
        infile_2 = input("Missing value file (.csv): ")
        if infile_2.endswith('.csv') is True:
            pass
        elif infile_2.endswith('.csv') is False:
            infile_2 = infile_2 + '.csv'
        missing = pd.read_csv(infile_2)
        length = len(missing.index)
        for i in range(0, length):
            new_value = missing.iloc[i]['Div.Time']
            data['Div.Time'].fillna(new_value,inplace=True, limit=1)
        output_name = input("File name (.csv) for replaced values: ")
        if output_name.endswith('.csv') is True:
            pass
        elif output_name.endswith('.csv') is False:
            output_name = output_name + '.csv'
        data.to_csv(output_name, index=False)
        print('Done!')
        print()
    elif choice == 'c':
        infile_1 = input("Input tree file in .nwk format: ")
        tree = Phylo.read(infile_1, "newick")
        Phylo.draw_ascii(tree)
    elif choice == 'm':
        main_loop()

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def main_loop():
    """The main loop of the script"""
    while True:
        choice = menu_choice()
        if choice is None:
            continue
        elif choice == 'q':
            print( "Exiting...")
            break     # jump out of while loop
        elif choice == '*':
            check_available()
        elif choice == 'a':
            div_times_sing()
        elif choice == 'b':
            div_times_batch()
        elif choice == 'c':
            evol_timeline()
        elif choice == 'd':
            time_tree()
        elif choice == 'e':
            citation()
        elif choice == 'f':
            validate()
        else:
            print("Invalid choice.")

# The following makes this program start running at main_loop()
# when executed as a stand-alone program.
if __name__ == '__main__':
    main_loop()
