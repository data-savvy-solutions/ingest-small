def get_ddl() -> dict:
    """
    Returns a dictionary of data types.

    Returns a dictionary of dictionaries. Each nested dictionary represents a
    table, with the key representing a column header and the value a data type.

    Args:
        None

    Returns:
        Dictionary: a dictionary of dictionaries representing tables and their
            data types.
    """

    schema = "ods_adventureworks"

    definitions = {}

    definitions[f"{schema}_CountryRegionCurrency"] = f"""
        CREATE TABLE [{schema}].[CountryRegionCurrency](
               [CountryRegionCode] [NVARCHAR](3) NOT NULL
               ,[CurrencyCode] [NCHAR](3) NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_CreditCard"] = f"""
        CREATE TABLE [{schema}].[CreditCard](
               [CreditCardID] [INT] NOT NULL
               ,[CardType] [NVARCHAR](50) NOT NULL
               ,[CardNumber] [NVARCHAR](25) NOT NULL
               ,[ExpMonth] [TINYINT] NOT NULL
               ,[ExpYear] [SMALLINT] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_Currency"] = f"""
        CREATE TABLE [{schema}].[Currency](
               [CurrencyCode] [NCHAR](3) NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_CurrencyRate"] = f"""
        CREATE TABLE [{schema}].[CurrencyRate](
               [CurrencyRateID] [INT] NOT NULL
               ,[CurrencyRateDate] [DATETIME] NOT NULL
               ,[FromCurrencyCode] [NCHAR](3) NOT NULL
               ,[ToCurrencyCode] [NCHAR](3) NOT NULL
               ,[AverageRate] [MONEY] NOT NULL
               ,[EndOfDayRate] [MONEY] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_Customer"] = f"""
        CREATE TABLE [{schema}].[Customer](
               [CustomerID] [INT] NOT NULL
               ,[PersonID] [INT] NULL
               ,[StoreID] [INT] NULL
               ,[TerritoryID] [INT] NULL
               ,[AccountNumber] [CHAR](256) NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_PersonCreditCard"] = f"""
        CREATE TABLE [{schema}].[PersonCreditCard](
               [BusinessEntityID] [INT] NOT NULL
               ,[CreditCardID] [INT] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_SalesOrderDetail"] = f"""
        CREATE TABLE [{schema}].[SalesOrderDetail](
               [SalesOrderID] [INT] NOT NULL
               ,[SalesOrderDetailID] [INT] NOT NULL
               ,[CarrierTrackingNumber] [NVARCHAR](25) NULL
               ,[OrderQty] [SMALLINT] NOT NULL
               ,[ProductID] [INT] NOT NULL
               ,[SpecialOfferID] [INT] NOT NULL
               ,[UnitPrice] [MONEY] NOT NULL
               ,[UnitPriceDiscount] [MONEY] NOT NULL
               ,[LineTotal] [MONEY] NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_SalesOrderHeader"] = f"""
        CREATE TABLE [{schema}].[SalesOrderHeader](
               [SalesOrderID] [INT] NOT NULL
               ,[RevisionNumber] [TINYINT] NOT NULL
               ,[OrderDate] [DATETIME] NOT NULL
               ,[DueDate] [DATETIME] NOT NULL
               ,[ShipDate] [DATETIME] NULL
               ,[Status] [TINYINT] NOT NULL
               ,[OnlineOrderFlag] [BIT] NOT NULL
               ,[SalesOrderNumber] [NVARCHAR](256) NOT NULL
               ,[PurchaseOrderNumber] [NVARCHAR](256) NULL
               ,[AccountNumber] [NVARCHAR](256) NULL
               ,[CustomerID] [INT] NOT NULL
               ,[SalesPersonID] [INT] NULL
               ,[TerritoryID] [INT] NULL
               ,[BillToAddressID] [INT] NOT NULL
               ,[ShipToAddressID] [INT] NOT NULL
               ,[ShipMethodID] [INT] NOT NULL
               ,[CreditCardID] [INT] NULL
               ,[CreditCardApprovalCode] [VARCHAR](15) NULL
               ,[CurrencyRateID] [INT] NULL
               ,[SubTotal] [MONEY] NOT NULL
               ,[TaxAmt] [MONEY] NOT NULL
               ,[Freight] [MONEY] NOT NULL
               ,[TotalDue] [money] NOT NULL
               ,[Comment] [NVARCHAR](128) NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_SalesOrderHeaderSalesReason"] = f"""
        CREATE TABLE [{schema}].[SalesOrderHeaderSalesReason](
               [SalesOrderID] [INT] NOT NULL
               ,[SalesReasonID] [INT] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_SalesPerson"] = f"""
        CREATE TABLE [{schema}].[SalesPerson](
               [BusinessEntityID] [int] NOT NULL
               ,[TerritoryID] [INT] NULL
               ,[SalesQuota] [MONEY] NULL
               ,[Bonus] [MONEY] NOT NULL
               ,[CommissionPct] [SMALLMONEY] NOT NULL
               ,[SalesYTD] [MONEY] NOT NULL
               ,[SalesLastYear] [MONEY] NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_SalesPersonQuotaHistory"] = f"""
        CREATE TABLE [{schema}].[SalesPersonQuotaHistory](
               [BusinessEntityID] [INT] NOT NULL
               ,[QuotaDate] [DATETIME] NOT NULL
               ,[SalesQuota] [MONEY] NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_SalesReason"] = f"""
        CREATE TABLE [{schema}].[SalesReason](
               [SalesReasonID] [INT] NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[ReasonType] [CHAR](256) NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_SalesTaxRate"] = f"""
        CREATE TABLE [{schema}].[SalesTaxRate](
               [SalesTaxRateID] [INT] NOT NULL
               ,[StateProvinceID] [INT] NOT NULL
               ,[TaxType] [TINYINT] NOT NULL
               ,[TaxRate] [SMALLMONEY] NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_SalesTerritory"] = f"""
        CREATE TABLE [{schema}].[SalesTerritory](
               [territoryid] [INT] not null
               ,[name] [CHAR](256) not null
               ,[countryregioncode] [NVARCHAR](3) not null
               ,[Group] [NVARCHAR](50) NOT NULL
               ,[SalesYTD] [MONEY] NOT NULL
               ,[SalesLastYear] [MONEY] NOT NULL
               ,[CostYTD] [MONEY] NOT NULL
               ,[CostLastYear] [MONEY] NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_SalesTerritoryHistory"] = f"""
        CREATE TABLE [{schema}].[SalesTerritoryHistory](
               [BusinessEntityID] [INT] NOT NULL
               ,[TerritoryID] [INT] NOT NULL
               ,[StartDate] [DATETIME] NOT NULL
               ,[EndDate] [DATETIME] NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_ShoppingCartItem"] = f"""
        CREATE TABLE [{schema}].[ShoppingCartItem](
               [ShoppingCartItemID] [INT] NOT NULL
               ,[ShoppingCartID] [NVARCHAR](50) NOT NULL
               ,[Quantity] [INT] NOT NULL
               ,[ProductID] [INT] NOT NULL
               ,[DateCreated] [DATETIME] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_SpecialOffer"] = f"""
        CREATE TABLE [{schema}].[SpecialOffer](
               [SpecialOfferID] [INT] NOT NULL
               ,[Description] [NVARCHAR](255) NOT NULL
               ,[DiscountPct] [SMALLMONEY] NOT NULL
               ,[Type] [NVARCHAR](50) NOT NULL
               ,[Category] [NVARCHAR](50) NOT NULL
               ,[StartDate] [DATETIME] NOT NULL
               ,[EndDate] [DATETIME] NOT NULL
               ,[MinQty] [INT] NOT NULL
               ,[MaxQty] [INT] NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_SpecialOfferProduct"] = f"""
        CREATE TABLE [{schema}].[SpecialOfferProduct](
               [SpecialOfferID] [INT] NOT NULL
               ,[ProductID] [INT] NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    definitions[f"{schema}_Store"] = f"""
        CREATE TABLE [{schema}].[Store](
               [BusinessEntityID] [INT] NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[SalesPersonID] [INT] NULL
               ,[Demographics] [XML] NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
    );"""

    return definitions
