from typing import TypedDict

from datetime import datetime, date

class PeopleDict(TypedDict):
    IndexHuman: int
    Name: str
    Surname: str
    MiddleName: str
    
    MainPhoneNumber: str
    AdditionalPhoneNumber: str

class CollaborationDict(TypedDict):
    IndexCustomer: int
    IndexHuman: int
    AccountNumber: str
    BankCreceiver: str
    CorporateAccount: str
    TIN: str
    CRP: str

class ComponentsDict(TypedDict):
    IndexComponent: int
    Title: str
    Weight: float
    Height: float
    Length: float
    Width: float

class StorageTermsDict(TypedDict):
    IndexStorageTerms: int
    Title: str

class ProductionProcessesDict(TypedDict):
    IndexProductionProcess: int
    ProductionScheme: str

class ProductionDepartmentsDict(TypedDict):
    IndexProductionDepartments: int
    title: str

class EquipmentDict(TypedDict):
    IndexEquipment: int
    Title: str
    Cost: float

class AssemblyDict(TypedDict):
    IndexBuild: int
    DateStarted: datetime
    EndDate: datetime
    IndexBuildStatus: int

class StatusWarehousesDict(TypedDict):
    IndexWarehouseStatus: int
    Title: str

class PostsDict(TypedDict):
    IndexPosition: int 
    Title: str
    Bet: float


class EmployeesDict(TypedDict):
    IndexEmployee: int 
    IndexHuman: int 
    IndexPosition: int
    DateOfBirth: date
    LocationResidence: str
    Series: str
    Number: str
    ActualPlaceResidence: str
    DateAdmissionWork: datetime
    NumberShifts: int

class ProductsDict(TypedDict):
    IndexProduct: int
    IndexProductionProcess: int
    Title: str
    IndexStorageTerms: int
    Pricing: int

class WarehouseManagersDict(TypedDict):
    IndexWarehouseManager: int
    IndexEmployee: int

class SalesManagersDict(TypedDict):
    IndexSalesManager: int
    IndexEmployee: int 

class WarehousesDict(TypedDict):
    IndexWarehouse: int
    Title: str
    Address: str
    IndexWM: int
    IndexWarehouseStatus: int

class RowsDict(TypedDict):
    IndexRope: int
    IndexWarehouse: int

class StellagesDict(TypedDict):
    IndexStellage: int
    IndexRope: int 
    MaximumWight: float
    Height: float
    Width: float
    Depth: float

class StatusOrdersDict(TypedDict):
    IndexOrderStatus: int
    Title: str

class OrdersDict(TypedDict):
    IndexOrder: int
    IndexSM: int
    DateOrder: datetime
    DatePayment: datetime
    IndexOrderStatus: int 


class TermsUseDict(TypedDict):
    IndexTermsUse: int
    Title: str
    StorageLocation: str


class SecurityTechniquesDict(TypedDict):
    IndexSecurityTechnique: int
    Title: str
    Hazardlevel: int
    StorageLocation: str


class TechnicalPassportDict(TypedDict):
    IndexTechnicalPassport: int 
    Title: str
    StorageLocation: str


import pandas as pd
class SaveList(TypedDict):
    name: str
    item: pd.DataFrame


