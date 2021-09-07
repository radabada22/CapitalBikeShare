

TotalBF = {
    'HX': 334.443, #holiday
    'HY': 3157.61, #holiday
    'NHTX': 224.382, #nonholiday w thunder
    'NHTY': 5399.47, #nonholiday w thunder
    'NHGX': 172.139, #nonholiday wo thunder w glaze
    'NHGY': 3943.29, #nonholiday wo thunder w glaze
    'NHNGX': 279.392, #nonholiday wo thunder wo glaze
    'NHNGY': 5372.5 #nonholiday wo thunder wo glaze
}
RegisteredBF = {
    'HX': 168.35, #holiday
    'HY': 2743.14, #holiday
    'NHGX': 144.165, #nonholiday w glaze
    'NHGY': 3644.86, #nonholiday w glaze
    'NHNGX': 150.661, #nonholiday wo glaze
    'NHNGY': 4955.98 #nonholiday wo glaze
}

CasualBF = {
    'HFX': 171.377, #holiday w fog
    'HFY': 152.297, #holiday w fog
    'HNFX': 174.224, #holiday wo fog
    'HNFY': 559.953, #holiday wo fog
    'NHFX': 102.549, #nonholiday w fog
    'NHFY': 258.046, #nonholiday w fog
    'NHNFX': 101.761, #nonholiday wo fog
    'NHNFY': 794.04 #nonholiday wo fog
}

import math


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def main_menu():
    print('\n')
    print('Demand Forecasting\n')
    print(' 1. Total Customers\n',
          '2. Casual Customers\n',
          '3. Registered Customers\n',
          '4. Maintenance\n' 
          ' 0. Exit\n')

    selection = input('Select option:')
    if selection == '1':
        total_demand()
    elif selection == '2':
        casual_demand()
    elif selection == '3':
        registered_demand()
    elif selection == '4':
        selection = input('Please Enter Password:')
        if selection == 'Password':
            maintenance()
        else:
            print('Incorrect, please try again')
            main_menu()
    elif selection == '0':
        sys.exit()
    else:
        print('Invalid selection. Select New Option:')
        main_menu()


def total_demand():
    print('\n')
    print('Demand Forecasting - Total Customer')
    print('Is it a Holiday?')
    print(' 1. Yes\n',
          '2. No\n',
          '0. Return to Demand Forecasting Menu\n')
    selection = input('Select Option:')

    if selection == '1':
        try:
            val = int(input('Average Temperature in Celsius:'))
            ATT = TotalBF['HY'] + (TotalBF['HX'] * val)
            ATT = round_up(ATT)
            print('Predicted Total Customers:', ATT)
            i = input('Press Any Key to Continue')
            main_menu()
        except ValueError:
            val = int(input('Please input valid integer:'))
            ATT = TotalBF['HY'] + (TotalBF['HX'] * val)
            ATT = round_up(ATT)
            print('Predicted Total Customers:', ATT)
            i = input('Press Any Key to Continue')
            main_menu()
    elif selection == '2':
        print('Is there Thunder?')
        print(' 1. Yes\n',
              '2. No\n',
              '0. Return to Demand Forecasting Menu\n')
        selection = input('Select Option:')
        if selection == '1':
            try:
                val = int(input('Average Temperature in Celsius:'))
                ATT = TotalBF['NHTY'] + (TotalBF['NHTX'] * val)
                ATT = round_up(ATT)
                print('Predicted Total Customers:', ATT)
                i = input('Press Any Key to Continue')
                main_menu()
            except ValueError:
                val = int(input('Please input valid integer:'))
                ATT = TotalBF['NHTY'] + (TotalBF['NHTX'] * val)
                ATT = round_up(ATT)
                print('Predicted Total Customers:', ATT)
                i = input('Press Any Key to Continue')
                main_menu()
        elif selection == '2':
            print('Is there Glaze?')
            print(' 1. Yes\n',
                  '2. No\n',
                  '0. Return to Demand Forecasting Menu\n')
            selection = input('Select Option:')
            if selection == '1':
                try:
                    val = int(input('Average Temperature in Celsius:'))
                    ATT = TotalBF['NHGY'] + (TotalBF['NHGX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
                except ValueError:
                    val = int(input('Please input valid integer:'))
                    ATT = TotalBF['NHGY'] + (TotalBF['NHGX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
            elif selection == '2':
                try:
                    val = int(input('Average Temperature in Celsius:'))
                    ATT = TotalBF['NHNGY'] + (TotalBF['NHNGX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
                except ValueError:
                    val = int(input('Please input valid integer:'))
                    ATT = TotalBF['NHNGY'] + (TotalBF['NHNGX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
            elif selection == '0':
                main_menu()
            else:
                print('Invalid selection. Select New Option:')
                total_demand()
        elif selection == '0':
            main_menu()
        else:
            print('Invalid selection. Select New Option:')
            total_demand()

    elif selection == '0':
        main_menu()
    else:
        print('Invalid selection. Select New Option:')
        main_menu()

def registered_demand():
    print('\n')
    print('Demand Forecasting - Registered Customer')
    print('Is it a Holiday?')
    print(' 1. Yes\n',
          '2. No\n',
          '0. Return to Demand Forecasting Menu\n')
    selection = input('Select Option:')

    if selection == '1':
        try:
            val = int(input('Average Temperature in Celsius:'))
            ATT = RegisteredBF['HY'] + (RegisteredBF['HX'] * val)
            ATT = round_up(ATT)
            print('Predicted Total Customers:', ATT)
            i = input('Press Any Key to Continue')
            main_menu()
        except ValueError:
            val = int(input('Please input valid integer:'))
            ATT = RegisteredBF['HY'] + (RegisteredBF['HX'] * val)
            ATT = round_up(ATT)
            print('Predicted Total Customers:', ATT)
            i = input('Press Any Key to Continue')
            main_menu()
    elif selection == '2':
        print('Is there Glaze?')
        print(' 1. Yes\n',
            '2. No\n',
            '0. Return to Demand Forecasting Menu\n')
        selection = input('Select Option:')
        if selection == '1':
                try:
                    val = int(input('Average Temperature in Celsius:'))
                    ATT = RegisteredBF['NHGY'] + (RegisteredBF['NHGX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
                except ValueError:
                    val = int(input('Please input valid integer:'))
                    ATT = RegisteredBF['NHGY'] + (RegisteredBF['NHGX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
        elif selection == '2':
                try:
                    val = int(input('Average Temperature in Celsius:'))
                    ATT = RegisteredBF['NHNGY'] + (RegisteredBF['NHNGX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
                except ValueError:
                    val = int(input('Please input valid integer:'))
                    ATT = RegisteredBF['NHNGY'] + (RegisteredBF['NHNGX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
        elif selection == '0':
                main_menu()
        else:
                print('Invalid selection. Select New Option:')
                casual_demand()

    elif selection == '0':
        main_menu()
    else:
        print('Invalid selection. Select New Option:')
        main_menu()

def casual_demand():
    print('\n')
    print('Demand Forecasting - Casual Customer')
    print('Is it a Holiday?')
    print(' 1. Yes\n',
          '2. No\n',
          '0. Return to Demand Forecasting Menu\n')
    selection = input('Select Option:')
    if selection == '1':
            print('Is there Fog?')
            print(' 1. Yes\n',
                  '2. No\n',
                  '0. Return to Demand Forecasting Menu\n')
            selection = input('Select Option:')
            if selection == '1':
                try:
                    val = int(input('Average Temperature in Celsius:'))
                    ATT = CasualBF['HFY'] + (CasualBF['HFX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
                except ValueError:
                    val = int(input('Please input valid integer:'))
                    ATT = CasualBF['HFY'] + (CasualBF['HFX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
            elif selection == '2':
                try:
                    val = int(input('Average Temperature in Celsius:'))
                    ATT = CasualBF['HNFY'] + (CasualBF['HNFX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
                except ValueError:
                    val = int(input('Please input valid integer:'))
                    ATT = CasualBF['HNFY'] + (CasualBF['HNFX'] * val)
                    ATT = round_up(ATT)
                    print('Predicted Total Customers:', ATT)
                    i = input('Press Any Key to Continue')
                    main_menu()
            elif selection == '0':
                main_menu()
            else:
                print('Invalid selection. Select New Option:')
                registered_demand()
    elif selection == '2':
                print('Is there Fog?')
                print(' 1. Yes\n',
                  '2. No\n',
                  '0. Return to Demand Forecasting Menu\n')
                selection = input('Select Option:')
                if selection == '1':
                    try:
                        val = int(input('Average Temperature in Celsius:'))
                        ATT = CasualBF['NHFY'] + (CasualBF['NHFX'] * val)
                        ATT = round_up(ATT)
                        print('Predicted Total Customers:', ATT)
                        i = input('Press Any Key to Continue')
                        main_menu()
                    except ValueError:
                        val = int(input('Please input valid integer:'))
                        ATT = CasualBF['NHFY'] + (CasualBF['NHFX'] * val)
                        ATT = round_up(ATT)
                        print('Predicted Total Customers:', ATT)
                        i = input('Press Any Key to Continue')
                        main_menu()
                elif selection == '2':
                    try:
                        val = int(input('Average Temperature in Celsius:'))
                        ATT = CasualBF['NHNFY'] + (CasualBF['NHNFX'] * val)
                        ATT = round_up(ATT)
                        print('Predicted Total Customers:', ATT)
                        i = input('Press Any Key to Continue')
                        main_menu()
                    except ValueError:
                        val = int(input('Please input valid integer:'))
                        ATT = CasualBF['NHNFY'] + (CasualBF['NHNFX'] * val)
                        ATT = round_up(ATT)
                        print('Predicted Total Customers:', ATT)
                        i = input('Press Any Key to Continue')
                        main_menu()
                elif selection == '0':
                    main_menu()
                else:
                    print('Invalid selection. Select New Option:')
                    registered_demand()
    elif selection == '0':
        main_menu()
    else:
                print('Invalid selection. Select New Option:')
                main_menu()
def maintenance():
    print('\n')
    print('Demand Forecasting - Maintenance\n')
    print(' 1. Total Customers\n',
          '2. Casual Customers\n',
          '3. Registered Customers\n',
          '0. Return to Main Menu\n')

    selection = input('Select option:')
    if selection == '1':
        total_maint()
    elif selection == '2':
        casual_maint()
    elif selection == '3':
        registered_maint()
    elif selection == '0':
        main_menu()
    else:
        print('Invalid selection. Select New Option:')
        maintenance()
def total_maint():
    print('\n')
    print('Make a selection\n')
    print(' 1. Holiday\n',
          '2. Non Holiday with Thunder\n',
          '3. Non Holiday without Thunder and with Glaze\n',
          '4. Non Holiday without Thunder and without Glaze\n',
          '0. Return to Maintenance Menu\n')
    selection = input('Select option:')
    if selection == '1':
        print('Holiday Trend\n',
            'Current Intercept:',TotalBF['HY'],'\n',
            'Current X Value:',TotalBF['HX'],'\n',
            '1. Change Intercept\n',
            '2. Change X Value\n',
            '3. Return to Previous Menu')
        selection = input('Select option:')
        if selection == '1':
                print('Current Intercept:', TotalBF['HY'],'\n')
                try:
                    TotalBF['HY']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    TotalBF['HY']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '2':
                print('Current X Value:', TotalBF['HX'],'\n')
                try:
                    TotalBF['HX']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    TotalBF['HX']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '3':
            total_maint()
        else:
            print('Invalid selection. Select New Option:')
            total_maint()
    elif selection == '2':
        print('Non Holiday with Thunder\n',
            'Current Intercept:',TotalBF['NHTY'],'\n',
            'Current X Value:',TotalBF['NHTX'],'\n',
            '1. Change Intercept\n',
            '2. Change X Value\n',
            '3. Return to Previous Menu')
        selection = input('Select option:')
        if selection == '1':
                print('Current Intercept:', TotalBF['NHTY'],'\n')
                try:
                    TotalBF['NHTY']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    TotalBF['NHTY']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '2':
                print('Current X Value:', TotalBF['NHTX'],'\n')
                try:
                    TotalBF['NHTX']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    TotalBF['NHTX']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '3':
            total_maint()
        else:
            print('Invalid selection. Select New Option:')
            total_maint()
    elif selection == '3':
        print('Non Holiday without Thunder and with Glaze\n',
            'Current Intercept:',TotalBF['NHGY'],'\n',
            'Current X Value:',TotalBF['NHGX'],'\n',
            '1. Change Intercept\n',
            '2. Change X Value\n',
            '3. Return to Previous Menu')
        selection = input('Select option:')
        if selection == '1':
                print('Current Intercept:', TotalBF['NHGY'],'\n')
                try:
                    TotalBF['NHGY']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    TotalBF['NHGY']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '2':
                print('Current X Value:', TotalBF['NHGX'],'\n')
                try:
                    TotalBF['NHGX']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    TotalBF['NHGX']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '3':
            total_maint()
        else:
            print('Invalid selection. Select New Option:')
            total_maint()
    elif selection == '4':
        print('Non Holiday without Thunder and without Glaze\n',
            'Current Intercept:',TotalBF['NHNGY'],'\n',
            'Current X Value:',TotalBF['NHNGX'],'\n',
            '1. Change Intercept\n',
            '2. Change X Value\n',
            '3. Return to Previous Menu')
        selection = input('Select option:')
        if selection == '1':
                print('Current Intercept:', TotalBF['NHNGY'],'\n')
                try:
                    TotalBF['NHNGY']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    TotalBF['NHNGY']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '2':
                print('Current X Value:', TotalBF['NHNGX'],'\n')
                try:
                    TotalBF['NHNGX']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    TotalBF['NHNGX']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '3':
            total_maint()
        else:
            print('Invalid selection. Select New Option:')
            total_maint()
    elif selection == '0':
        maintenance()
    else:
        print('Invalid selection. Select New Option:')
        total_maint()

def registered_maint():
    print('\n')
    print('Make a selection\n')
    print(' 1. Holiday\n',
          '2. Non Holiday with Glaze\n',
          '3. Non Holiday without Glaze\n',
          '0. Return to Maintenance Menu\n')
    selection = input('Select option:')
    if selection == '1':
        print('Holiday Trend\n',
            'Current Intercept:',RegisteredBF['HY'],'\n',
            'Current X Value:',RegisteredBF['HX'],'\n',
            '1. Change Intercept\n',
            '2. Change X Value\n',
            '3. Return to Previous Menu')
        selection = input('Select option:')
        if selection == '1':
                print('Current Intercept:', RegisteredBF['HY'],'\n')
                try:
                    RegisteredBF['HY']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    RegisteredBF['HY']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '2':
                print('Current X Value:', RegisteredBF['HX'],'\n')
                try:
                    RegisteredBF['HX']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    RegisteredBF['HX']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '3':
            total_maint()
        else:
            print('Invalid selection. Select New Option:')
            total_maint()
    elif selection == '2':
        print('Non Holiday with Glaze\n',
            'Current Intercept:',RegisteredBF['NHGY'],'\n',
            'Current X Value:',RegisteredBF['NHGX'],'\n',
            '1. Change Intercept\n',
            '2. Change X Value\n',
            '3. Return to Previous Menu')
        selection = input('Select option:')
        if selection == '1':
                print('Current Intercept:', RegisteredBF['NHGY'],'\n')
                try:
                    RegisteredBF['NHGY']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    RegisteredBF['NHGY']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '2':
                print('Current X Value:', RegisteredBF['NHGX'],'\n')
                try:
                    RegisteredBF['NHGX']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    RegisteredBF['NHGX']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '3':
            total_maint()
        else:
            print('Invalid selection. Select New Option:')
            total_maint()
    elif selection == '3':
        print('Non Holiday without Glaze\n',
            'Current Intercept:',RegisteredBF['NHNGY'],'\n',
            'Current X Value:',RegisteredBF['NHNGX'],'\n',
            '1. Change Intercept\n',
            '2. Change X Value\n',
            '3. Return to Previous Menu')
        selection = input('Select option:')
        if selection == '1':
                print('Current Intercept:', RegisteredBF['NHNGY'],'\n')
                try:
                    RegisteredBF['NHNGY']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    RegisteredBF['NHNGY']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '2':
                print('Current X Value:', RegisteredBF['NHNGX'],'\n')
                try:
                    RegisteredBF['NHNGX']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    RegisteredBF['NHNGX']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '3':
            total_maint()
        else:
            print('Invalid selection. Select New Option:')
            total_maint()
    elif selection == '0':
        maintenance()
    else:
        print('Invalid selection. Select New Option:')
        total_maint()

def casual_maint():
    print('\n')
    print('Make a selection\n')
    print(' 1. Holiday with Fog\n',
          '2. Holiday without Fog\n',
          '3. Non Holiday with Fog\n',
          '4. Non Holiday without Fog\n',
          '0. Return to Maintenance Menu\n')
    selection = input('Select option:')
    if selection == '1':
        print('Holiday with Fog\n',
            'Current Intercept:',CasualBF['HFY'],'\n',
            'Current X Value:',CasualBF['HFX'],'\n',
            '1. Change Intercept\n',
            '2. Change X Value\n',
            '3. Return to Previous Menu')
        selection = input('Select option:')
        if selection == '1':
                print('Current Intercept:', CasualBF['HFY'],'\n')
                try:
                    CasualBF['HFY']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    CasualBF['HFY']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '2':
                print('Current X Value:', CasualBF['HFX'],'\n')
                try:
                    CasualBF['HFX']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    CasualBF['HFX']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '3':
            total_maint()
        else:
            print('Invalid selection. Select New Option:')
            total_maint()
    elif selection == '2':
        print('Holiday without Fog \n',
            'Current Intercept:',CasualBF['HNFY'],'\n',
            'Current X Value:',CasualBF['HNFX'],'\n',
            '1. Change Intercept\n',
            '2. Change X Value\n',
            '3. Return to Previous Menu')
        selection = input('Select option:')
        if selection == '1':
                print('Current Intercept:', CasualBF['HNFY'],'\n')
                try:
                    CasualBF['HNFY']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    CasualBF['HNFY']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '2':
                print('Current X Value:', CasualBF['HNFX'],'\n')
                try:
                    CasualBF['HNFX']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    CasualBF['HNFX']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '3':
            total_maint()
        else:
            print('Invalid selection. Select New Option:')
            total_maint()
    elif selection == '3':
        print('Non Holiday with Fog\n',
            'Current Intercept:',CasualBF['NHFY'],'\n',
            'Current X Value:',CasualBF['NHFX'],'\n',
            '1. Change Intercept\n',
            '2. Change X Value\n',
            '3. Return to Previous Menu')
        selection = input('Select option:')
        if selection == '1':
                print('Current Intercept:', CasualBF['NHFY'],'\n')
                try:
                    CasualBF['NHFY']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    CasualBF['NHFY']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '2':
                print('Current X Value:', CasualBF['NHFX'],'\n')
                try:
                    CasualBF['NHFX']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    CasualBF['NHFX']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '3':
            total_maint()
        else:
            print('Invalid selection. Select New Option:')
            total_maint()
    elif selection == '4':
        print('Non Holiday without Fog\n',
            'Current Intercept:',CasualBF['NHNFY'],'\n',
            'Current X Value:',CasualBF['NHNFX'],'\n',
            '1. Change Intercept\n',
            '2. Change X Value\n',
            '3. Return to Previous Menu')
        selection = input('Select option:')
        if selection == '1':
                print('Current Intercept:', CasualBF['NHNFY'],'\n')
                try:
                    CasualBF['NHNFY']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    CasualBF['NHNFY']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '2':
                print('Current X Value:', CasualBF['NHNFX'],'\n')
                try:
                    CasualBF['NHNFX']=float(input('New Intercept:'))
                    print('Processed')
                    total_maint()
                except ValueError:
                    CasualBF['NHNFX']=float(input('Please input valid integer:'))
                    total_maint()
        elif selection == '3':
            total_maint()
        else:
            print('Invalid selection. Select New Option:')
            total_maint()
    elif selection == '0':
        maintenance()
    else:
        print('Invalid selection. Select New Option:')
        total_maint()


main_menu()
