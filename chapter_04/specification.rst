======================================
 ABQ data entry program specification
======================================

Description
-----------
The program is created to minimize data entry errors for lab measurements.

Functionality Required
--------------------------

The program must:

* allow all relevant, valid data to be entered, as per the field chart.
* append entered data to a csv file.
  - the csv file must have a filename
    of abq_data_record_CURRENTDATE.csv, where
    CURRENTDATE is the date of the checks in
    ISO format i.e. year-month-day.
  - the csv file must have all the fields as per the chart.
* enforce correct datatypes per field.
* have inputs that:
  - ignore meaningless keystrokes
  - require a value for all fields, except Notes
  - get marked with an error if the value is invalid on focusout
* prevent saving the record when errors are present

The program should try, whenever possible, to :

* enforce reasonable limits on data entered.
* pre-fill data.
* suggest possible correct values.
* provide a smooth and efficient workflow.

Functionality not Required
--------------------------

The program does not need to:

* allow editing of data. This can be done in appropriate editing software if necessary.
* allow deletion of data.

Limitations
-----------

The program must:

* be efficiently operable by keyboard-only users.
* be accessible to color blind users.
* run on debian linux.
* run acceptably on a low-end pc.

+------------+----------+------+--------------+---------------------+
|Field       | Datatype | Units| Range        |Descripton           |
+============+==========+======+==============+=====================+
|Date        |Date      |      |              |date of record in iso|
+------------+----------+------+--------------+---------------------+
|Time        |Time      |      |8, 12, 16, 20 |Time period          |
+------------+----------+------+--------------+---------------------+
|Lab         |String    |      | A - E        |lab id               |
+------------+----------+------+--------------+---------------------+
|Technician  |String    |      |              |technician name      |
+------------+----------+------+--------------+---------------------+
|Plot        |Int       |      | 1 - 20       |plot id              |
+------------+----------+------+--------------+---------------------+
|seed sample |String    |      |              |seed sample id       |
+------------+----------+------+--------------+---------------------+
|Fault       |Bool      |      |              |fault on sensor      |
+------------+----------+------+--------------+---------------------+
|Light       |Decimanl  |klx   | 0 - 100      |light at plot        |
+------------+----------+------+--------------+---------------------+
|Humidity    |Decimal   |g/m³  | 0.5 - 52.0   |abs humidity at plot |
+------------+----------+------+--------------+---------------------+
|Temperature |Decimal   |°C    | 4 - 40       |temperature at plot  |
+------------+----------+------+--------------+---------------------+
|Blossoms    |Int       |      | 0 - 1000     |# blossons in plot   |
+------------+----------+------+--------------+---------------------+
|Fruit       |Int       |      | 0 - 1000     |# fruits in plot     |
+------------+----------+------+--------------+---------------------+
|Plants      |Int       |      | 0 - 20       |# plants in plot     |
+------------+----------+------+--------------+---------------------+
|Max height  |Decimal   |cm    | 0 - 1000     |Ht of tallest plant  |
+------------+----------+------+--------------+---------------------+
|Min height  |Decimal   |cm    | 0 - 1000     |Ht of shortest plant |
+------------+----------+------+--------------+---------------------+
|Median ht   |Decimal   |cm    | 0 - 1000     |Median ht of plants  |
+------------+----------+------+--------------+---------------------+
|Notes       |String    |      |              |Miscellaneous notes  |
+------------+----------+------+--------------+---------------------+