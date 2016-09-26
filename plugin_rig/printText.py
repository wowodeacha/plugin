import custom_global_function as cgf
CAS = cgf.CustomAttrSetCla()
PLUGIN_PATH = CAS.get_cur_dir_path_fun()
DATA_PATH = PLUGIN_PATH + "datafile/headbasebonedata.json"
FACE_JNT_PIV_DIR = CAS.load_data(DATA_PATH)
CAS.write_data(DATA_PATH,FACE_JNT_PIV_DIR)