from lib_custom.common.utils import MiscUtils
from lib_custom.common.utils import FileUtils
from lib_custom.common.logger import BaseLogger
from lib_custom.common.config_reader import ConfigReader
import os


MiscUtils.check_variables_specified(['TEST_TYPE', 'ENVIRONMENT'])

common_config = ConfigReader(config_file_path='etc/common.conf').get_configuration()
output_folder_name = common_config.get('general', 'outputs_file')

# create environment.properties file

if ('RESULTS_FOLDER' in os.environ.keys()) and (os.environ['RESULTS_FOLDER'] is not None):
    output_folder_name = os.environ['RESULTS_FOLDER'].lower()

FileUtils.create_folder(output_folder_name)
BaseLogger.write('Confirmed {} directory exists.'.format(output_folder_name))

out_properties_folder = '{}/{}'.format(output_folder_name, os.environ['TEST_TYPE'])
outPropertiesPath = '{}/environment.properties'.format(out_properties_folder)

FileUtils.clean_directory('{}/*'.format(out_properties_folder), 'history')
BaseLogger.write('Cleaned {}/* directory.'.format(out_properties_folder))

FileUtils.create_folder('{}'.format(out_properties_folder))
BaseLogger.write('Confirmed {}/* directory exists.'.format(out_properties_folder))

# create environment.properties file

FileUtils.save_txt_file(outPropertiesPath, '')
BaseLogger.write('Saved empty {} file.'.format(outPropertiesPath))

