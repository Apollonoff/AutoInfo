
def check_number(car):
    k = 0

    first_litter = car[0]
    second_litter = car[4]
    third_litter = car[5]

    first_number = car[1]
    second_number = car[2]
    third_number = car[3]

    if len(car) == 9:
        region = car[6] + car[7] + car[8]
    else:
        region = car[6] + car[7]


    kirill = set('авекмнорстух')
    numbers = set('0123456789')
    regions = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
               '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '102', '113',
               '116', '121', '122', '123', '124', '126', '134', '136', '138', '142', '147', '150', '152', '154', '155',
               '156', '159', '161', '163', '164', '173', '174', '177', '178', '186', '190', '193', '196', '197', '198',
               '199', '702', '750', '716', '761', '763', '774', '777', '790', '797', '799']
    for i in range(33, 100):
        regions.append(str(i))

    if len(car) == 9 or len(car) == 8:
        k += 1
    if not kirill.isdisjoint(first_litter.lower()) and not kirill.isdisjoint(second_litter.lower()) and not kirill.isdisjoint(third_litter.lower()):
        k += 1
    if not numbers.isdisjoint(first_number) and not numbers.isdisjoint(second_number) and not numbers.isdisjoint(third_number):
        k += 1
    if region in regions:
        k += 1
    if k == 4:
        return True
    else:
        return False

if __name__ == '__main__':
    car ='У932НР116'
    print(check_number(car))