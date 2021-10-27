Module database
===============

Sub-modules
-----------
* database.operations

Classes
-------

`License(**kwargs)`
:   License for storing alcohol licenses
    
    Attributes
    ----------
    id : object
        Table primary key
    name: object
        License place name
    
    Methods
    -------
    name():
        Returns object's name variable
    
    A simple constructor that allows initialization from kwargs.
    
    Sets attributes on the constructed instance using the names and
    values in ``kwargs``.
    
    Only keys that are present as
    attributes of the instance's class are allowed. These could be,
    for example, any mapped columns or relationships.

    ### Ancestors (in MRO)

    * sqlalchemy.orm.decl_api.Base

    ### Instance variables

    `address`
    :

    `business_id`
    :

    `city`
    :

    `created_at`
    :

    `id`
    :

    `license_granting_date`
    :

    `license_type`
    :

    `name`
    :

    `postcode`
    :

    ### Methods

    `get_name(self)`
    :