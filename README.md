Confluence export XML converter
===============================

Python3 script convert.py converts Atlassian Confluence 5.7.1 XML exports to become compliant with Confluence 7.6.2 connected to a PostgreSQL 9.6 DBMS.

### Instructions

1. Export all data from Confluence 5.7.1 to a .zip file by navigating to [Confluence URL]/admin/backup.action .

2. Extract entities.xml part of the exported .zip and place it within toplevel of this repository.

3. Run the Python 3 script: `$ python3 convert.py`

4. As soon as the script has completed, find file entities_converted.xml in the repo's directory. Rename or delete entities.xml and use this as the new name of file entities_converted.xml.

5. Create a new .zip file containing the original export zip's content but now with the converted entities.xml.

6. Upload the new .zip to Confluence 7.6.2 during the Backup Restore process.
