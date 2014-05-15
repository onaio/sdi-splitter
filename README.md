Split a form downloaded by ODK Briefcase into various ODK Briefcase folders per country according to a csv list of uuids.

- picked the uuids for each country from the exported xls file, apply a filter on the country field in order to get the country specific uuid and save as a csv file with the country name.
- pulled data from odk aggregate server with odk briefcase
- python split.py, to split the submission into country specific odk briefcase
- use briefcase to upload the country specific data into own country
