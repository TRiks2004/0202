import random

from mimesis import Person, Datetime, Address, Text
from mimesis.locales import Locale
from mimesis.enums import Gender

from datetime import datetime, timedelta

from TypedDictTable import PeopleDict, CollaborationDict, ComponentsDict, StorageTermsDict, ProductionProcessesDict, ProductionDepartmentsDict, \
    EquipmentDict, AssemblyDict, StatusWarehousesDict, PostsDict, EmployeesDict, ProductsDict, WarehouseManagersDict, SalesManagersDict, WarehousesDict,\
    RowsDict, StellagesDict, StatusOrdersDict, OrdersDict, TermsUseDict, SecurityTechniquesDict, TechnicalPassportDict




local = Locale.RU

def generate_nonzero_n_digit_number(n):
    if n <= 0:
        raise ValueError("n должно быть положительным числом")
    
    first_digit = random.randint(1, 9)  # Генерация первой цифры от 1 до 9
    rest_of_digits = [random.randint(0, 9) for _ in range(n-1)]  # Генерация оставшихся (n-1) цифр
    number = ''.join(map(str, [first_digit] + rest_of_digits))  # Преобразование в число
    return number

def generate_float(n, k):
    if n <= k:
        raise ValueError("Length of the number should be greater than the number of decimal places.")
    
    integer_part_length = n - k - 1  # One position reserved for the decimal point
    
    # Generate the integer part
    integer_part = ''.join(str(random.randint(0, 9)) for _ in range(integer_part_length))
    
    # Generate the decimal part
    decimal_part = ''.join(str(random.randint(0, 9)) for _ in range(k))
    
    # Combine integer and decimal parts with a decimal point
    result = f"{integer_part}.{decimal_part}"
    
    return float(result)



class People():
    def __init__(self, ):
        ...

    def get_gender(self):
        return random.choice([Gender.FEMALE, Gender.MALE])
    
    def get_telephone(self):
        return Person().telephone(mask="##########")
    
    def get_patronymic(self, gender: Gender):
        if gender == Gender.FEMALE:
            return random.choice(['Владиславовна', 'Геннадьевна', 'Матвеевна', 'Вадимовна', 'Борисовна', 'Никитовна', 'Данииловна', 'Викторовна', 'Егоровна', 'Георгиевна', 'Степановна', 'Семёновна', 'Ивановна', 'Сергеевна', 'Алексеевна', 'Семёновна', 'Вадимовна', 'Олеговна', 'Геннадьевна', 'Степановна', 'Антоновна', 'Евгеньевна', 'Викторовна', 'Петровна', 'Арсениевна', 'Евгеньевна', 'Владиславовна', 'Петровна', 'Фёдоровна', 'Станиславовна',])
        elif gender == Gender.MALE:
            return random.choice(['Романович', 'Геннадьевич', 'Геннадьевич', 'Леонидович', 'Владиславович', 'Витальевич', 'Константинович', 'Никитович', 'Антонович', 'Владимирович', 'Аркадиевич', 'Дмитриевич', 'Матвеевич', 'Ильич', 'Дмитриевич', 'Васильевич', 'Степанович', 'Антонович', 'Семёнович', 'Георгиевич', 'Леонидович', 'Васильевич', 'Максимович', 'Васильевич', 'Максимович', 'Иванович', 'Никитович', 'Викторович', 'Фёдорович', 'Денисович',])
    
    def get_person(self, n: int = 1) -> PeopleDict:
    
        person = Person(local)

        gender = self.get_gender()

        first_name = person.name(gender=gender)
        surname = person.surname(gender=gender)
        patronymic = self.get_patronymic(gender=gender)

        mainPhoneNumber = self.get_telephone()
        AdditionalPhoneNumber = self.get_telephone()

        return PeopleDict(
            {
                'IndexHuman': n+1,
                'Name': first_name, 
                'Surname': surname, 
                'MiddleName': patronymic, 
                'MainPhoneNumber': mainPhoneNumber, 
                'AdditionalPhoneNumber': AdditionalPhoneNumber
            }
        )

    def get_data_frame(self, n: int = None):
        return [self.get_person(i) for i in range(n)]

class Collaboration():
    def __init__(self, peopleDict: list[PeopleDict]) -> None:
        self.peopleDict = peopleDict
    
    def get_bank(self):
        return random.choice(['ПАО Сбербанк', 'АО Россельхозбанк', 'ПAO Промсвязьбанк', 'ПАО АК БАРС БАНК', 'Банк ВТБ (ПАО)', 'ПАО Банк ЗЕНИТ', 'ООО КБЭР Банк Казани', 'АО МСП Банк', 'ПАО Банк ФК Открытие', 'РНКБ Банк (ПАО)', 'АО АЛЬФА-БАНК', 'ТКБ БАНК ПАО', 'АО Банк Интеза', 'АО АКБ НОВИКОМБАНК', 'АО СМП Банк', 'АО Райффайзенбанк', 'ПАО CКБ Приморья Примсоцбанк', 'ПАО Совкомбанк', 'АО КОШЕЛЕВ-БАНК', 'АО «БАНК СГБ»', 'АО Углеметбанк', 'АО Датабанк', 'КБ ЭНЕРГОТРАНСБАНК (АО)', 'Банк Левобережный (ПАО)', 'ПАО РосДорБанк', 'АО ГЕНБАНК', 'Банк ГПБ (АО)', 'ПАО НБД-Банк', 'ПАО МОСКОВСКИЙ КРЕДИТНЫЙ БАНК', 'ПАО ЧЕЛИНДБАНК', 'ООО КБ Алтайкапиталбанк', 'ПАО Банк Кузнецкий', 'СИБСОЦБАНК ООО', 'АО Банк ДОМ.РФ', 'Азиатско-Тихоокеанский Банк (АО)', 'АО Экспобанк', 'ПАО БАНК УРАЛСИБ', 'АО БАНК ОРЕНБУРГ', 'ПАО НИКО-БАНК', 'АО Банк Акцепт', 'ПАО КБ Центр-инвест', 'АКБ Ланта-Банк (АО)', 'ПАО КБ САММИТ БАНК', 'ПАО БАНК СИАБ', 'ПАО Банк Санкт-Петербург', 'КБ Кубань Кредит ООО', 'ПАО АКИБАНК', 'СДМ-Банк (ПАО)', 'ПАО МЕТКОМБАНК', 'АО «Дальневосточный банк»', 'АО КБ РУСНАРБАНК', 'АО КБ Хлынов', 'АКБ Алмазэргиэнбанк АО', 'АО Солид Банк', 'АО Ингосстрах Банк', 'ЮГ-Инвестбанк (ПАО)', 'Банк ИТУРУП (ООО)', 'ООО КБ «Кетовский»'])

    def get_collaboration(self, n: int = 1):
        index_human = random.choice(self.peopleDict)['IndexHuman']
        account_humber = generate_nonzero_n_digit_number(20)    
        
        bank_creceiver = self.get_bank()
        corporate_account = generate_nonzero_n_digit_number(10)

        TIN = generate_nonzero_n_digit_number(12)
        CRP = generate_nonzero_n_digit_number(12)


        return CollaborationDict(
            {
                "IndexCustomer": n+1,
                "IndexHuman": index_human, 
                "AccountNumber": account_humber, 
                "BankCreceiver": bank_creceiver, 
                "CorporateAccount": corporate_account, 
                "TIN": TIN, 
                "CRP": CRP
                }
            )

    def get_data_frame(self, n: int = None):
        return [self.get_collaboration(i) for i in range(n)]

class Components():
    
    def __init__(self) -> None:
        pass

    def get_data_frame(self, n: int = None):
        components = []

        title_list = ['Микро-турбо двигатель', 'Лазерный фокусировщик с переменной длиной волны', 'Нанороботический манипулятор', 'Графеновый интегральный микросхемный чип', 'Полимерный аккумулятор с увеличенным сроком службы', 'Био-композитный материал с антимикробными свойствами', 'Импульсный плазменный реактор', 'Многоосевой магнитный подшипник', 'Гравитационно-компенсированный гироскоп', 'Квантовый криптографический процессор', 'Беспилотный авиационный комплекс нового поколения', 'Электростатический манипулятор для чистых комнат', 'Термоактивируемый формоизменяющийся полимер', 'Солнечная ячейка с двойным слоем квантовых точек', 'Магнитный резонансный сканер супервысокого разрешения', 'Наночастицы для лечения заболеваний', 'Кинетический генератор энергии из движения воздуха', 'Ионно-проводящий композит для энергосберегающих батарей', 'Лазерный уровень точности с автоматической коррекцией', 'Разборный магнитный мотор для электротранспорта', 'Биоразлагаемая пищевая упаковка с встроенным датчиком свежести', 'Адаптивный материал с памятью формы для одежды', 'Гибридный алгоритм для квантового компьютера', 'Экологически чистый катализатор для автомобильных выхлопных газов', 'Сверхлегкий материал для авиационной промышленности', 'Биосенсор для мониторинга здоровья в реальном времени', 'Гибкий OLED-дисплей высокого разрешения', 'Реверсивный магнитный конденсатор', 'Беспроводная система передачи энергии на основе резонанса', 'Умный домашний робот с искусственным интеллектом',]

        if n == None or len(title_list) < n:
            light = len(title_list)
        else:
            light = n

        for title in range(light):
            weight = generate_float(6, 3)
            height = generate_float(5, 3)
            length = generate_float(5, 3)
            width = generate_float(5, 3)

            components.append(
                ComponentsDict(
                    {
                        "IndexComponent": title+1,
                        'Title': title_list[title], 
                        'Weight': weight, 
                        'Height': height, 
                        'Length': length, 
                        'Width': width
                    }
                )
            )
        
        return components

class StorageTerms():
    def __init__(self) -> None:
        pass
    
    def get_data_frame(self, n: int = None):
        
        storage_terms = ['Погружено в масло', 'Масляная ванна', 'Масляная пропитка', 'Хранение под брезентом', 'Упаковка в брезентовые мешки', 'Защита от солнца и влаги', 'Брезентовый тент', 'Масляная эмульсия', 'Масляная камера']

        if n == None or len(storage_terms) < n:
            light = len(storage_terms)
        else:
            light = n

        return [
            StorageTermsDict(
                {
                    'IndexStorageTerms' : i+1, 
                    'Title': storage_terms[i]
                }
            ) for i in range(light)]

class ProductionProcesses():
    def __init__(self) -> None:
        pass

    def get_production_processes(self, n: int = 1):
        path = 'Production/Scheme/' + ''.join(str(random.randint(0, 9)) for _ in range(10)) + '.pdf'
        return ProductionProcessesDict(
            {
                'IndexProductionProcess': n+1,
                'ProductionScheme': path
            }
        )

    def get_data_frame(self, n: int = None):
        return [self.get_production_processes(i) for i in range(n)]


class ProductionDepartments():
    def __init__(self) -> None:
        pass
    
    def get_data_frame(self, n: int = None):
        
        storage_terms = ['Автоматизированное производство', 'Технологическое проектирование', 'Линия сборки и монтажа', 'Управление оборудованием и техникой', 'Энергетика и обеспечение',]

        if n == None or len(storage_terms) < n:
            light = len(storage_terms)
        else:
            light = n

        return [
            ProductionDepartmentsDict(
                {
                    'IndexProductionDepartments' : i+1, 
                    'Title': storage_terms[i]
                }
            ) for i in range(light)]

class Equipment():

    def __init__(self) -> None:
        pass
    
    def get_data_frame(self, n: int = None):
        
        storage_terms = ['Токарный станок', 'Фрезерный станок', 'Пресс', 'Ленточнопильный станок', 'Сварочный аппарат', 'Промышленная машина с чпу', 'Гидравлический пресс', 'Лазерная резка', 'Экструдер', 'Роботизированная система сборки']

        if n == None or len(storage_terms) < n:
            light = len(storage_terms)
        else:
            light = n

        return [
            EquipmentDict(
                {
                    'IndexEquipment' : i+1, 
                    'Title': storage_terms[i],
                    'Cost': generate_float(8, 2)
                }
            ) for i in range(light)]

class Assembly():
    def __init__(self, ):
        ...


    def get_assembly(self, n: int = 1):
        datetime_provider = Datetime(locale=local)

        # Generate random date for DateStarted and EndDate
        date = datetime_provider.date(start=2022, end=2023)

        # Generate random time for DateStarted
        date_started = datetime_provider.time()

        # Generate random time for EndDate, ensuring it is greater than DateStarted
        while True:
            end_date = datetime_provider.time()

            if end_date > date_started:
                break

        # Create the Assembly TypedDict
        return AssemblyDict(
            {
                'IndexBuild': n+1,
                'DateStarted': datetime.combine(date, date_started),
                'EndDate': datetime.combine(date, end_date) + timedelta(days=random.choice([0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 3, 4])),
                'IndexBuildStatus': 1
            }   
        )
    
    def get_data_frame(self, n: int = None):
        return [self.get_assembly(i) for i in range(n)]

class StatusWarehouses():
    def __init__(self) -> None:
        pass
    
    def get_data_frame(self, n: int = None):
        
        storage_terms = ['Ожидает поступления товара', 'В процессе приемки товаров', 'Полностью заполнен и ожидает отгрузки', 'Находится в стадии оптимизации пространства', 'Товар в процессе сортировки', 'Склад временно закрыт для инвентаризации', 'В процессе упаковки товаров для отгрузки', 'Осуществляется проверка качества товаров', 'Склад в стадии реконструкции', 'Временное хранение товаров для специального заказа', 'Склад в режиме обслуживания и ремонта оборудования', 'Товар отправлен на возврат от клиента', 'Ожидает инспекции со стороны регулирующих органов', 'Зарезервированное место для будущей поставки', 'Складские ресурсы перераспределяются', 'Проходит аудит состояния инвентаря', 'Товар в ожидании окончательного утверждения заказа', 'Закрыт для временного хранения на период кризиса', 'Внутренний перевод товаров между складами', 'Склад выделен для экспресс-доставки важных заказов']

        if n == None or len(storage_terms) < n:
            light = len(storage_terms)
        else:
            light = n

        return [
            StatusWarehousesDict(
                {
                    'IndexEquipment' : i+1, 
                    'Title': storage_terms[i]
                }
            ) for i in range(light)]

class Posts():
    def __init__(self) -> None:
        pass
    
    def get_data_frame(self, n: int = None):
        
        storage_terms = ['Инженер-конструктор машин и оборудования', 'Технолог по изготовлению деталей машин', 'Специалист по автоматизации производства', 'Механик по ремонту металлорежущих станков', 'Производственный инженер в автомобильной отрасли', 'Слесарь-сборщик машин и оборудования', 'Инженер по качеству в машиностроении', 'Токарь-фрезеровщик', 'Лазерный оператор по резке металла', 'Электросварщик металлоконструкций',]

        if n == None or len(storage_terms) < n:
            light = len(storage_terms)
        else:
            light = n

        return [
            PostsDict(
                {
                    'IndexPosition' : i+1, 
                    'Title': storage_terms[i],
                    'Bet': generate_float(6, 2)
                }
            ) for i in range(light)]

class Employees():
    def __init__(self, peopleDict: PeopleDict, postsDict: PostsDict) -> None:
        self.peopleDict = peopleDict
        self.postsDict = postsDict

    def get_employees(self, n: int = 1):
        
        address_provider = Address(locale=local)

        ActualPlaceResidence = address_provider.address()

        if random.randint(0, 5) == 0:
            LocationResidence = address_provider.address()
        else:
            LocationResidence = ActualPlaceResidence

        DateOfBirth = Datetime(locale=local).date(start=1960, end=2000)


        while True:
            DateAdmissionWork = Datetime(locale=local).date(start=DateOfBirth.year, end=2023)

            age_difference = DateAdmissionWork - DateOfBirth

            if age_difference.days >= 20 * 365:
                break

        

        return EmployeesDict(
            {
                'IndexEmployee': n+1,
                'IndexHuman': random.choice(self.peopleDict)['IndexHuman'],
                'IndexPosition': random.choice(self.postsDict)['IndexPosition'],
                'DateOfBirth': DateOfBirth,
                'ActualPlaceResidence': ActualPlaceResidence,
                'LocationResidence': LocationResidence,
                'DateAdmissionWork': DateAdmissionWork,
                'Number': generate_nonzero_n_digit_number(4),
                'Series': generate_nonzero_n_digit_number(6),
                'NumberShifts': random.randint(20, 40)
            }
        ) 

    def get_data_frame(self, n: int = None): 
        return [self.get_employees(i) for i in range(n)]
    

class Products:
    def __init__(self, productionProcessesDict: ProductionProcessesDict, storageTermsDict: PostsDict) -> None:
        self.productionProcessesDict = productionProcessesDict
        self.storageTermsDict = storageTermsDict
    
    def get_products(self, n: int = 1):
        generic = Text(locale=local)
        
        return ProductsDict(
            {
               'IndexProduct': n+1,
               'IndexProductionProcess': random.choice(self.productionProcessesDict)['IndexProductionProcess'],
               'Title': "Продукт " + generic.word(),
               'IndexStorageTerms': random.choice(self.storageTermsDict)['IndexStorageTerms'],
               'Pricing': random.randint(100, 1000)
            }
        ) 
    
    def get_data_frame(self, n: int = None): 
        return [self.get_products(i) for i in range(n)]
    
class WarehouseManagers:
    def __init__(self, employeesDict: EmployeesDict) -> None:
        self.employeesDict = employeesDict
    
    def get_warehouse_managers(self, n: int = 1):
        return WarehouseManagersDict(
            {
                'IndexWarehouseManager': n+1,
                'IndexEmployee': random.choice(self.employeesDict)['IndexEmployee']
            }
        ) 
    
    def get_data_frame(self, n: int = None): 
        return [self.get_warehouse_managers(i) for i in range(n)]
    
class SalesManagers:
    def __init__(self, employeesDict: EmployeesDict) -> None:
        self.employeesDict = employeesDict
    
    def get_sales_managers(self, n: int = 1):
        return SalesManagersDict(
            {
                'IndexSalesManager': n+1,
                'IndexEmployee': random.choice(self.employeesDict)['IndexEmployee']
            }
        ) 
    
    def get_data_frame(self, n: int = None): 
        return [self.get_sales_managers(i) for i in range(n)]
    
class Warehouses:
    def __init__(self, warehouseManagersDict: WarehouseManagersDict, salesManagersDict: SalesManagersDict) -> None:
        self.warehouseManagersDict = warehouseManagersDict
        self.salesManagersDict = salesManagersDict
    
    def get_warehouses(self, n: int = 1, address: str = None):
        
        
        
        return WarehousesDict(
            {
                'IndexWarehouse': n+1,
                'IndexWarehouseManager': random.choice(self.warehouseManagersDict)['IndexWarehouseManager'],
                'IndexSalesManager': random.choice(self.salesManagersDict)['IndexSalesManager'],
                'Address': address,
                'Title': "Склад " + generate_nonzero_n_digit_number(6),

            }
        ) 
    
    def get_data_frame(self, n: int = None): 

        address_provider = Address(locale=local)

        address = address_provider.address()

        return [self.get_warehouses(i, address) for i in range(n)]
    

class Rows:
    def __init__(self, warehousesDict: WarehousesDict) -> None:
        self.warehousesDict = warehousesDict
    
    def get_rows(self, n: int = 1):
        return RowsDict(
            {
                'IndexRope': n+1,
                'IndexWarehouse': random.choice(self.warehousesDict)['IndexWarehouse']
            }
        ) 
    
    def get_data_frame(self, n: int = None): 
        return [self.get_rows(i) for i in range(n)]
    
class Stellages:
    def __init__(self, rowsDict: RowsDict) -> None:
        self.rowsDict = rowsDict
    
    def get_stellages(self, n: int = 1):
        return StellagesDict(
            {
                'IndexStellage': n+1,
                'IndexRope': random.choice(self.rowsDict)['IndexRope'],
                'MaximumWight': generate_float(8, 3),
                'Height': generate_float(6, 3),
                'Width': generate_float(6, 3),
                'Depth': generate_float(7, 3)
            }
        ) 
    
    def get_data_frame(self, n: int = None): 
        return [self.get_stellages(i) for i in range(n)]

class StatusOrders():
    def __init__(self) -> None:
        pass
    
    def get_data_frame(self, n: int = None):
        
        storage_terms = ['В обработке', 'Ожидает подтверждения', 'Доставка в пути', 'Завершен', 'Отменен клиентом', 'В обработке у поставщика', 'На складе', 'Отправлен', 'Возвращен', 'Ожидает оплаты', 'В производстве', 'В пути к клиенту', 'На проверке качества', 'Неудачная попытка доставки', 'Отложен', 'Возвращено на доработку', 'Ожидает подписи', 'В ожидании запасных частей', 'Неопределенный статус', 'Возвращен из-за повреждения']

        if n == None or len(storage_terms) < n:
            light = len(storage_terms)
        else:
            light = n

        return [
            StatusOrdersDict(
                {
                    'IndexStorageTerms' : i+1, 
                    'Title': storage_terms[i]
                }
            ) for i in range(light)]

class Orders():
    def __init__(self, statusOrdersDict: StatusOrdersDict, salesManagersDict: SalesManagersDict) -> None:
        self.statusOrdersDict = statusOrdersDict
        self.salesManagersDict = salesManagersDict

    def get_orders(self, n: int = 1):

        DateOfBirth = Datetime(locale=local).datetime(start=2020, end=2023)


        return OrdersDict(
            {
                'IndexOrder': n+1,
                'IndexSM': random.choice(self.salesManagersDict)['IndexSalesManager'],
                'DateOrder': DateOfBirth,
                'DatePayment': DateOfBirth + timedelta(hours=random.choice([0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 3, 4])),
                'IndexOrderStatus': random.choice(self.statusOrdersDict)['IndexStorageTerms'], 
            }
        ) 

    def get_data_frame(self, n: int = None): 
        return [self.get_orders(i) for i in range(n)]


class TermsUse():
    def get_production_processes(self, n: int = 1):
            
            name = ''.join(str(random.randint(0, 9)) for _ in range(10))
            path = 'TermsUse/' + name + '.pdf'
            return TermsUseDict(
                {
                    'IndexTermsUse': n+1,
                    'Title': name,
                    'StorageLocation': path
                }
            )

    def get_data_frame(self, n: int = None):
        return [self.get_production_processes(i) for i in range(n)]
    
class SecurityTechniquesUse():
    def get_production_processes(self, n: int = 1):
            
            name = ''.join(str(random.randint(0, 9)) for _ in range(10))
            path = 'SecurityTechniquesUse/' + name + '.pdf'
            return SecurityTechniquesDict(
                {
                    'IndexSecurityTechnique': n+1,
                    'Title': name,
                    'StorageLocation': path,
                    'Hazardlevel': random.randint(0, 10)
                }
            )

    def get_data_frame(self, n: int = None):
        return [self.get_production_processes(i) for i in range(n)]
    

class TechnicalPassport():
    def get_production_processes(self, n: int = 1):
            
            name = ''.join(str(random.randint(0, 9)) for _ in range(10))
            path = 'TechnicalPassport/' + name + '.pdf'
            return TechnicalPassportDict(
                {
                    'IndexTermsUse': n+1,
                    'Title': name,
                    'StorageLocation': path
                }
            )

    def get_data_frame(self, n: int = None):
        return [self.get_production_processes(i) for i in range(n)]