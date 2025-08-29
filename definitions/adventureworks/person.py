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

    definitions[f"{schema}_Address"] = f"""
        CREATE TABLE [{schema}].[Address](
               [AddressID] [INT] NOT NULL
               ,[AddressLine1] [NVARCHAR](60) NOT NULL
               ,[AddressLine2] [NVARCHAR](60) NULL
               ,[City] [NVARCHAR](30) NOT NULL
               ,[StateProvinceID] [INT] NOT NULL
               ,[PostalCode] [NVARCHAR](15) NOT NULL
               ,[SpatialLocation] [GEOGRAPHY] NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_AddressType"] = f"""
        CREATE TABLE [{schema}].[AddressType](
               [AddressTypeID] [INT] NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_BusinessEntity"] = f"""
        CREATE TABLE [{schema}].[BusinessEntity](
               [BusinessEntityID] [INT] NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_BusinessEntityAddress"] = f"""
        CREATE TABLE [{schema}].[BusinessEntityAddress](
               [BusinessEntityID] [INT] NOT NULL
               ,[AddressID] [INT] NOT NULL
               ,[AddressTypeID] [INT] NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_BusinessEntityContact"] = f"""
        CREATE TABLE [{schema}].[BusinessEntityContact](
               [BusinessEntityID] [INT] NOT NULL
               ,[PersonID] [INT] NOT NULL
               ,[ContactTypeID] [INT] NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_ContactType"] = f"""
        CREATE TABLE [{schema}].[ContactType](
               [ContactTypeID] [INT] NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_CountryRegion"] = f"""
        CREATE TABLE [{schema}].[CountryRegion](
               [CountryRegionCode] [NVARCHAR](3) NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_EmailAddress"] = f"""
        CREATE TABLE [{schema}].[EmailAddress](
               [BusinessEntityID] [INT] NOT NULL
               ,[EmailAddressID] [INT] NOT NULL
               ,[EmailAddress] [NVARCHAR](50) NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_Password"] = f"""
        CREATE TABLE [{schema}].[Password](
               [BusinessEntityID] [INT] NOT NULL
               ,[PasswordHash] [VARCHAR](128) NOT NULL
               ,[PasswordSalt] [VARCHAR](10) NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_Person"] = f"""
        CREATE TABLE [{schema}].[Person](
               [BusinessEntityID] [INT] NOT NULL
               ,[PersonType] [NCHAR](2) NOT NULL
               ,[NameStyle] [INT] NOT NULL
               ,[Title] [NVARCHAR](8) NULL
               ,[FirstName] [CHAR](256) NOT NULL
               ,[MiddleName] [CHAR](256) NULL
               ,[LastName] [CHAR](256) NOT NULL
               ,[Suffix] [NVARCHAR](10) NULL
               ,[EmailPromotion] [INT] NOT NULL
               ,[AdditionalContactInfo] [XML] NULL
               ,[Demographics] [XML] NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_PersonPhone"] = f"""
        CREATE TABLE [{schema}].[PersonPhone](
               [BusinessEntityID] [INT] NOT NULL
               ,[PhoneNumber] [CHAR](20) NOT NULL
               ,[PhoneNumberTypeID] [INT] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_PhoneNumberType"] = f"""
        CREATE TABLE [{schema}].[PhoneNumberType](
               [PhoneNumberTypeID] [INT] NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    definitions[f"{schema}_StateProvince"] = f"""
        CREATE TABLE [{schema}].[StateProvince](
               [StateProvinceID] [INT] NOT NULL
               ,[StateProvinceCode] [NCHAR](3) NOT NULL
               ,[CountryRegionCode] [NVARCHAR](3) NOT NULL
               ,[IsOnlyStateProvinceFlag] [BIT] NOT NULL
               ,[Name] [CHAR](256) NOT NULL
               ,[TerritoryID] [INT] NOT NULL
               ,[rowguid] [UNIQUEIDENTIFIER] NOT NULL
               ,[ModifiedDate] [DATETIME] NOT NULL
               ,[ingest_datetime] [DATETIME] NOT NULL
               ,[current_record] [BIT] NOT NULL
        );"""

    return definitions
