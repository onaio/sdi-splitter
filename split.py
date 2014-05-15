"""
Split on Informal Settlement Profile into different countries based on uuids
of the files with filenames same name as the countries.

- picked the uuids for each country from the exported xls file
- pulled data from odk aggregate server with odk briefcase
- python split.py, to split the submission into country specifci odk briefcase
storage folder
- use briefcase to upload the country specific data into own country
"""
import os
import shutil

CWD = 'REPLACE_WITH_DIR_CONTAINING_ODK_BRIEFCASE_FOLDER'
form_name = 'Informal Settlement Profile'
form_folder = os.path.join(
    CWD,
    'ODK Briefcase Storage',
    'forms', form_name
)
form_xml = os.path.join(form_folder, '%s.xml' % form_name)
countries = [
    u'kenya', u'malawi', u'namibia', u'southafrica', u'uganda', 'ghana']

uuid_dict = {}
for country in countries:
    uuids = []
    with open(country) as f:
        for uuid in f.readlines():
            uuids.append(uuid.strip().replace(':', ''))
    uuid_dict[country] = uuids

for country in countries:
    country_folder = os.path.join(
        CWD, 'deploy', country,
        'ODK Briefcase Storage',
        'forms', form_name
    )
    if not os.path.exists(country_folder):
        os.makedirs(country_folder)
    country_instances_folder = os.path.join(country_folder, 'instances')
    shutil.copy(form_xml, country_folder)
    if not os.path.exists(country_instances_folder):
        os.mkdir(country_instances_folder)
    for instance in uuid_dict[country]:
        path = os.path.join(form_folder, 'instances', instance)
        dst = os.path.join(country_instances_folder, instance)
        shutil.copytree(path, dst)
