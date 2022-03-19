import subprocess
import sys
import vdf
import json

def check_args(args):
    if len(args) != 2 or not args[1].isnumeric():
        print("Must have a single command parameter which is the appid of the steam app you want info from.\nExample: python get_steam_app_info.py 1180760")
        exit(1)
        
def get_vdf_from_string_array(non_filtered_output):
    start_line_index = -1
    end_line_index = -1

    current_index = 0
    for line in non_filtered_output:
        is_start_of_vdf = line.startswith("{")
        is_end_of_vdf = line.startswith("}")
        
        if is_start_of_vdf:
            start_line_index = current_index
        elif is_end_of_vdf:
            end_line_index = current_index
    
        current_index += 1
        
    if start_line_index == -1 or end_line_index == -1:
        print("Error while parsing input")
        print("".join(non_filtered_output))
        exit(1)
        
    return non_filtered_output[start_line_index - 1:end_line_index + 1]
    
def byte_array_to_string_array(byte_array, encoding = "utf-8"):
    return [line.decode(encoding) for line in byte_array]
        
def get_app_info(appid):
    bytes_output = subprocess.Popen(f'./steamcmd.sh +login anonymous +app_info_update 1 +app_info_print {appid} +quit', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.readlines()
    return get_vdf_from_string_array(byte_array_to_string_array(bytes_output))

check_args(sys.argv)
    
appid = sys.argv[1]

steamcmd_output = get_app_info(appid)

steamcmd_output = "".join(steamcmd_output)

vdf_data = vdf.loads(steamcmd_output)

print(json.dumps(vdf_data))
